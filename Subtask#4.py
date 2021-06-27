def max_equal_split_flow_upgrade(graph, source, sink):
  edge_flow = {(edge.tail,edge.head): 0 for edge in graph.edges}
  edge_capacity = {(edge.tail,edge.head): edge.capacity for edge in graph.edges}

  for node in graph.vertices:
    out_edges = graph.out_edges(node)
    
    if node == source: 
      for edge in out_edges:
        edge_flow[edge.tail, edge.head] = 1/len(out_edges)
    elif node != sink:
      in_edges = graph.in_edges(node)
      total_in = 0
      for neighbor in in_edges:
        total_in += edge_flow[neighbor.tail,neighbor.head]
      for neighbor in out_edges:
        edge_flow[neighbor.tail,neighbor.head] = total_in/len(out_edges)
  
  max_equal_flow = float('inf')
  max_equal_node = 0
  for edge in graph.edges:
    bottleneck = edge.capacity/edge_flow[edge.tail,edge.head]
    if max_equal_flow > bottleneck:
      max_equal_flow = bottleneck
      max_equal_node = (edge.tail,edge.head)
  
  edge_capacity[max_equal_node] += 1
 
  upgraded_flow = []
  for edge in graph.edges:
    if edge_capacity[max_equal_node] == edge.capacity:
      upgraded_flow.append(edge.capacity/edge_flow[edge.tail,edge.head])
  return min(upgraded_flow)

  raise NotImplementedError('You must implement the function without changing the function name and argument list.')