# vxc-motors-sim explainer video: script

Video: [../vxc-explainer.mp4](../vxc-explainer.mp4) · 80 s · 1920×1080 · 30 fps · no audio ·
Remotion, all scenes in [`src/Composition.tsx`](src/Composition.tsx). Numbers, ids and the quote come from
the recorded day in `demo/data` (D-021); the session id in scene 7 is Tom's blocked INC-1 session.

Re-render:
```bash
cd explainers/video
npm i && npm run prepare-assets        # avatars from company/avatars, timeline screenshot from ../timeline-dark.png
npx remotion render VxcExplainer ../vxc-explainer.mp4 --browser-executable=/opt/pw-browsers/chromium
```

## Concept map (who it is for: a smart adult near tech, not an ML practitioner)
| # | Concept | Depth | Needs |
|---|---|---|---|
| 1 | An LLM writes text, nothing else | brief | everyday "input, process, output" |
| 2 | **An agent acts only by asking the LLM for a tool call** (threshold concept) | full | 1 |
| 3 | A tool is one operation of a real application, which enforces the rules | full | 2 |
| 4 | A message between agents is a tool call plus a doorbell | full | 2, 3 |
| 5 | A judgment tool is answered by another agent | brief | 3 |
| 6 | One proxy names every speaker, so the company can be watched | full | 2 |

How-it-works candidates (each became an animated scene): the agent loop (2, 3), the doorbell (4),
the BMW tech case (5).

## Scenes
| # | Time | Scene | On screen |
|---|---|---|---|
| 1 | 0:00–0:04.5 | Title | The twelve avatars pop in. "vxc-motors-sim · A BMW dealership run by LLM agents". |
| 2 | 0:04.5–0:11.5 | The problem | "Every employee is about to get an AI agent. Who watches the company?" Cards: traffic is everywhere; risk looks like work; demos are toys. |
| 3 | 0:11.5–0:18.5 | Who works there | Avatars by department, plus customers and BMW UK. "Each has a persona, a job description and a résumé, and works only through the dealership's software." |
| 4 | 0:18.5–0:31.5 | The one idea | Maria's agent ↔ LLM ↔ CRM. Packets: goal + 74 tools → `tool_call: crm_search_customers("Hannah Clarke")` → `POST /call` → `C-00976 Hannah Clarke · audit row written`. "The LLM only proposes…" |
| 5 | 0:31.5–0:44.5 | A message is a tool call, then a doorbell | Maria → Chat app (`chat_send`) → Director sees `CH-00033 maria → sofia (no text)` → doorbell → Sofia reads with `chat_unread`. |
| 6 | 0:44.5–0:55.5 | Some answers come from another agent | Aisha → BMW Portal (`bmw_open_tech_case`, fault 21F0A3) → BMW tech support agent → case BMW-TC-00001. Quote from the recorded answer. |
| 7 | 0:55.5–1:05.5 | One proxy sees it all | Request headers (`X-Agent-User: tom-becker`, `X-Agent-Dept: Sales`). The six incidents: five BLOCK, INC-6 REFUSED (James declined). |
| 8 | 1:05.5–1:14.5 | The recorded day | 552 LLM calls · 111 tasks · 44 emails · 79 team chats · 7 sessions blocked; 35 minutes live on a free model, $0. The timeline page pans by. |
| 9 | 1:14.5–1:20.5 | Outro | `python3 demo/run_demo.py`; "Ships its blueprint too"; repo URL. |
