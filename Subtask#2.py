def is_feasible(graph, source, sink, flow_value):
  # Use BFS
  visited = {node: False for node in graph.vertices }
  edge_flow = {(edge.tail,edge.head): 0 for edge in graph.edges}

  frontier = []

  flow_value = flow_value/len(graph.out_edges(source))
  
  for neighbor in graph.out_edges(source):
    if flow_value > neighbor.capacity:
      return False
    else:
      edge_flow[source,neighbor.head] = flow_value
  for node in graph.out_edges(source):
    frontier.append(node.head)
  visited[source] = True
  u = 0
  while frontier:
    node = frontier[u]
    in_degree = graph.in_edges(node)
    out_degree = graph.out_edges(node)

    #If node has an in-edge within the same level
    cont = 0
    for neighbor in in_degree:
      if visited[neighbor.tail] == False:
        u += 1
        cont = 1
        break 
    # Immediately jump to after in_degree
    if cont == 1:
      continue
    
    # For n levels
    if node != sink:
      total_in = 0
      for neighbor in in_degree:
        total_in += edge_flow[(neighbor.tail,node)]
      total_in = total_in/len(out_degree)
      for neighbor in out_degree:
        if total_in > neighbor.capacity:
          return False
        elif total_in < neighbor.capacity:
          edge_flow[(node,neighbor.head)] += total_in
          # Append neighbors of node for after iteration of outer loop  
          if neighbor.head not in frontier:
            frontier.append(neighbor.head)

    # Mark node as visited after the iteration
    frontier.pop(u)
    u = 0
    visited[node] = True
    
  return True

  raise NotImplementedError('You must implement the function without changing the function name and argument list.')
