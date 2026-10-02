# Project 1 Report: Intelligent Search Visualizer

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Selected Region:**`, `**Live Deployment URL:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.

---

## Student Information 
- **Name:** Shravani Bhase
- **UID (netID):** sbhas24
- **UIN:** 668167086

---

## Section 1: Selected City Region
- **Selected Region:** Chicago metro area, Illinois, USA (Chicago and 19 suburbs around it)

---

## Section 2: Map Graph Configuration
- **Total Cities Configured:** 20
- **Total Connection Edges:** 25
- **Graph Fully Connected:** Yes

---

## Section 3: Local Verification & Search Algorithms
*Check the algorithms you successfully ran and verified on your local development server by placing an `x` in the brackets (e.g., `[x]`):*
- [x] Breadth-First Search (BFS)
- [x] Depth-First Search (DFS)
- [x] Uniform Cost Search (UCS)
- [x] Iterative Deepening Search (IDS)
- [x] Greedy Best-First Search (Greedy)
- [x] A* Search (A*)

---

## Section 4: Deployed and Presentation Information
- **Deployment Platform:** Render
- **Live Deployment URL:** https://ai-search-project-1ye9.onrender.com/
- **Video Presentation Link:** https://drive.google.com/file/d/13TQMLeC2ql7Dkk43grFhiUE-IPzxW81L/view?usp=sharing

---

## Section 5: Discussion
- **Which search algorithm is best for this route finding problem?** 
I think A* is the best one for this problem. When you're driving, you want the shortest distance, and only UCS and A* always found it on my map. For example, going from Northbrook to Cicero, BFS picked a route with only 5 roads, but it was 62.03 km. UCS and A* found a route with 11 roads that was only 54.96 km. So fewest roads doesn't mean shortest trip. A* is better than UCS because it uses the straight-line distance to the goal to decide where to look next, so it wastes less time. The straight-line distance is also never longer than the real road distance, so A* still gives the shortest route.

- **Search Efficiency (Nodes expanded/time taken comparison):** 
I tested all six on Berwyn to Wilmette. BFS expanded 10 nodes, DFS 6, UCS 19, IDS 43, Greedy 13, and A* 14. IDS expanded way more than the others because it restarts from Berwyn every time the depth limit goes up. A* found the same 46.31 km route as UCS but expanded 14 nodes instead of 19, so the heuristic really helped. DFS and Greedy were fast but gave worse routes: DFS came out to 48.8 km, and Greedy went all the way around through 12 towns for 58.21 km because it just kept picking whatever was closest to Wilmette. Every algorithm finished in under a millisecond since there are only 20 places, so the node counts showed the differences better than the times did. On a real map with way more places, I think the difference would be a lot bigger.

- **Link the idea of search algorithm to today Generative AI.** 
Generative AI also does a kind of search. A chatbot writes its answer one word (token) at a time, and each time it has to pick the next word out of thousands of options, kind of like picking which node to expand next. If it always takes the single most likely word, that's like Greedy search: it's fast, but it can end up with a worse answer overall, the same way Greedy took the long way on my map. Beam search keeps a few of the best options going at the same time instead of just one. The model's probabilities work kind of like a heuristic, since they point it toward good choices so it doesn't have to try everything. It's the same tradeoff I saw in this project: looking at more options usually gives a better answer, but it takes more time and memory.