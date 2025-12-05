# Mostar-index-calculator

A Python script that computes the **Mostar index** of an undirected simple graph using BFS.
This repository contains a clean, easy-to-read implementation and a minimal command-line interface for reading a graph and printing its Mostar index.

---

## 📌 What Is the Mostar Index?

The **Mostar index** of a graph measures how asymmetric the distances to the endpoints of each edge are across all vertices.

For each edge `(u, v)`:

* Count how many vertices are closer to `u` than to `v`
* Count how many vertices are closer to `v` than to `u`
* The edge contributes:
  **`abs(n_u - n_v)`**

The **Mostar index of the graph** is the sum of this value over all edges.

---

## 📂 Files

* `mostar.py` — main implementation using BFS repeatedly per edge.
* *(Optional)* `mostar_improved.py` — suggestion for faster all-pairs BFS version.

---
## Requirements
[View the PDF](./recom.pdf)

## ⚙️ Requirements

* Python **3.7+**
* Uses only standard library (`collections`)

---

## 🚀 Usage

### Input format

```
n m
u1 v1
u2 v2
...
um vm
```

Where:

* `n` — number of nodes
* `m` — number of edges
* `ui vi` — undirected edge

**Recommended:** Use non-interactive input for batch runs.

### Example

`example.txt`:

```
4 3
1 2
2 3
3 4
```

Run:

```bash
python mostar.py < example.txt
```

Output:

```
Mostar Index: 4
```

---

## 🧪 Improved `read_graph()` (recommended)

```python
def read_graph():
    """Reads a graph from stdin as an adjacency list.
    Expects: first line 'n m', followed by m lines with 'u v' (1-based node labels).
    """
    import sys
    lines = sys.stdin.read().strip().split()
    if not lines:
        return {}
    it = iter(lines)
    n = int(next(it))
    m = int(next(it))
    graph = {i: [] for i in range(1, n+1)}
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        graph[u].append(v)
        graph[v].append(u)
    return graph
```

---

## ⏱️ Complexity Analysis

### Current implementation (baseline)

For every edge `(u, v)`:

* 2 BFS runs → `O(n + m)` each
* `m` edges → total **O(m · (n + m))**

For sparse graphs → ~`O(n²)`
For dense graphs → ~`O(n³)`

### Suggested improvement

* Run BFS from every vertex once: `n` BFS runs
* Compare distances per edge in `O(n)`

Total: **O(n(n + m))**, typically much faster.

---

## 🧠 Recommended Improvements

* Precompute all BFS distances (`n × n` table)
* Add support for isolated nodes (already included in improved reader)
* Add unit tests for known graphs (path, star, cycle, complete)
* Add CLI using `argparse`
* Optimize speed for large graphs

---

## 🔍 Example Test Cases

| Graph          | Input                      | Expected Mostar Index   |
| -------------- | -------------------------- | ----------------------- |
| Path `P4`      | `1-2-3-4`                  | **4**                   |
| Star `S4`      | `1` center, leaves `2,3,4` | Known value (good test) |
| Complete `K_n` | fully connected            | **0**                   |
| Single node    | no edges                   | **0**                   |

---

## 🤝 Contributing

Pull requests for:

* Optimized version
* Added test suite
* Benchmarks
* Documentation updates

are welcome!

---

## 📄 License

Recommended: **MIT License**

---


