# Campus Reachability and Emergency Route Audit

This Python program models campus locations as vertices in an undirected graph
and walkways as edges. It reports connected components, deterministic DFS and
BFS traversals from an emergency station, and shortest routes to requested
destinations.

## Requirements

- Python 3.10 or later

## Input format

Provide the following values in order. Values may be separated by spaces or
newlines.

1. Number of vertices `n` and edges `m`
2. `m` undirected edges, each as `u v` (vertices are numbered `0` through `n-1`)
3. Source vertex `s` and number of route queries `q`
4. `q` target vertices

The program sorts every adjacency list, so DFS and BFS visit neighbors in
increasing numerical order. Each component is labeled with its smallest
numbered vertex. BFS supplies the minimum-edge routes.

## Example

Input:

```text
6 5
0 2
0 1
1 3
2 3
4 5
0 3
3
5
0
```

Output:

```text
COMPONENTS 2
LABELS 0 0 0 0 4 4
DFS 0 1 3 2
BFS 0 1 2 3
ROUTE 3 2 0 1 3
ROUTE 5 UNREACHABLE
ROUTE 0 0 0
```

## Run

From the repository folder, run the program and enter the input:

```powershell
py .\DAA.py
```

Press `Ctrl+Z`, then `Enter` to finish input in Windows PowerShell.

Alternatively, save the input in `input.txt` and run it from Command Prompt:

```powershell
cmd /c "py DAA.py < input.txt"
```

The accompanying `explanation.PDF` contains the project explanation and
additional test cases.
