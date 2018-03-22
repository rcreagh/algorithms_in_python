#! usr/bin/python3

"""This program implements union-find as per Sedgewick's 'Algorithms'. This
implementation takes a list of pairs of nodes which must be integers. These
pairs of nodesvrepresent edges between two vertices in a graph. It assumes that
each number between 0 and n exists in the graph, ie. whatever the graph holds,
each node is represented by a number.

This implementation is 'weighted quick-union'. Path compression is not
implemented here."""

def union_find(n, pairs_of_nodes):
  """Functiont that takes in a total number of nodes, and a list of edges in
  a graph and returns the amount of connected components in the graph.

  Args:
    n: int - The total number of nodes in the graph.
    pairs_of_nodes: list - a list of graph edges
  """
  id = [] # The root node in the connected component tree for node.
  size = [] # The size of the connected component tree for node.
  # Total number of components. Starts at n, as each node is its own connected
  # component.
  count = n

  def connected(p, q):
    """Checks if p & q are in the same connected component (out of the
    components we have connected to date)."""
    return id[p] == id[q]

  def union(p, q):
    """Joins two nodes into a single component."""
    root_p = find(p) # Find the root node of p.
    root_q = find(q) # Find the root node of q.
    # Join the smaller tree onto the larger one.
    if size[root_p] < size[root_q]:
      id[root_p] = root_q
      size[root_q] += size[root_p]
    else:
      id[root_q] = root_p
      size[root_p] = size[root_q]

  def find(p):
    """Returns the root node of p, by traversing the tree of its connected
    component until it reaches the root node."""
    while p != id[p]:
      p = id[p]
    return p

  # Set the root of each node to itself initially, and the size of each
  # component to 1.
  for i in range(n):
    id.append(i)
    size.append(1)

  for p, q in pairs_of_nodes:
    if connected(p, q):
      continue
    else:
      union(p, q)
      count -= 1

  return count