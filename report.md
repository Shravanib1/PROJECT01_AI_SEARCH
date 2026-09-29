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
- **Selected Region:** Chicago metropolitan area, Illinois, USA (Chicago plus 19 nearby suburbs)

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
- **Deployment Platform:** Renderr
- **Live Deployment URL:** https://ai-search-project-1ye9.onrender.com/
- **Video Presentation Link:** [Provide an accessible link to your 5–7 minute video presentation]

---

## Section 5: Discussion
- **Which search algorithm is best for this route finding problem?** 
    A* is the best choice for this problem. What a driver actually cares about is the shortest road distance, and only UCS and A* guarantee that. Between those two, A* usually gets there with fewer expansions because the straight-line distance to the goal pulls the search in the right direction instead of spreading out evenly like UCS does. The heuristic is also safe to use here: a road can never be shorter than the straight line between two towns, so it never overestimates and A* stays optimal. BFS and IDS find the route with the fewest roads, which isn't the same as the shortest one, and DFS and Greedy can return noticeably longer routes.

- **Search Efficiency (Nodes expanded/time taken comparison):** When I compared the algorithms on the same start and destination, IDS expanded the most nodes by far, because every time it raises the depth limit it starts over from the start and re-expands the shallow places again. BFS and UCS came next, since they both spread out in every direction before reaching the goal. A* expanded fewer nodes than UCS while still returning the same shortest distance. DFS and Greedy often expanded the fewest nodes, but that speed came at a price: their routes were sometimes longer than the optimal one. Runtime was well under a millisecond for every algorithm because the graph only has 20 places, so on a map this size the node counts show the difference between algorithms much better than the timings do. On a real road network with millions of intersections, that gap in expanded nodes is exactly what would make A* practical and IDS or BFS far too slow.

- **Link the idea of search algorithm to today Generative AI.** 
    Generative AI models also have to search, just through a much bigger space. A language model writes one token at a time, and at each step it is choosing among thousands of possible next tokens, which is a lot like choosing which node to expand next. Methods like greedy decoding work the same way as Greedy Best-First Search: take whatever looks best right now, which is fast but can lead to a worse overall answer. Beam search keeps several of the best partial answers at once, similar to a frontier in best-first search with a limited size. The model's probabilities act a bit like a heuristic, guiding it toward promising continuations instead of trying everything. Newer reasoning models go further and explore several possible solution paths, check them, and back up when one fails, which is very close to the tree search ideas in this project. The same tradeoff shows up in both places: exploring more options gives better answers but costs more time and memory.

