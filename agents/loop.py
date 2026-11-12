"""The one tool-calling loop every agent with tools runs (staff and outside mail agents alike).

Send the conversation and the tool list to the LLM (through the proxy), run the tool calls it asks
for against the applications (over HTTP), append the results, repeat until it answers in words, the
proxy blocks the session, or `max_turns` model calls have been made.

    answer = tool_loop(client, tools, messages, log, out, max_turns=8, on_event=hook)

`out` is the caller's result dict: this adds to out["calls"] and out["tools"], and sets
out["status"] ("error" or "turn_limit") and out["error"] when the loop does not end with an answer.
"""
from openai import APIError

from llm import chat

TOOL_RESULT_MAX = 4000


def tool_loop(client, tools, messages, log, out, max_turns, on_event):
    session = out["session"]
    for _ in range(max_turns):
        try:
            resp = chat(client, messages, tools=tools.specs, log=log)
        except APIError as e:
            out["status"] = "error"
            out["error"] = f"{type(e).__name__}: {e}"[:300]
            return None
        out["calls"] += 1
        on_event("llm_call", session=session)
        msg = resp.choices[0].message
        messages.append(msg.model_dump(exclude_none=True))
        text = (msg.content or "").strip()
        if log.blocked:
            on_event("blocked", session=session, firewall=log.blocked, text=text[:400])
            return text
        if not msg.tool_calls:
            return text
        for c in msg.tool_calls:
            result = tools.call(c.function.name, c.function.arguments)
            log.tool(c.function.name, c.function.arguments, result)
            out["tools"].append(c.function.name)
            on_event("tool", session=session, tool=c.function.name, args=c.function.arguments, result=result[:300])
            messages.append({"role": "tool", "tool_call_id": c.id, "content": result[:TOOL_RESULT_MAX]})
    out["status"] = "turn_limit"
    return None
