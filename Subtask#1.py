def check_constraints(graph, source, sink, flow):
  for flow_value in flow:
    if flow[flow_value] <= 0:
      return False

  visited = {node: False for node in graph.vertices }

  stack = [source]

  while (len(stack)):
    s = stack[-1]
    stack.pop()
    
    in_degree = graph.in_edges(s)
    out_degree = graph.out_edges(s)

    if visited[s] == False:
      visited[s] = True
    # C1
    if s != source:
      for neighbor in in_degree:
        if flow[(neighbor.tail, neighbor.head)] > neighbor.capacity:
          return False
    
    # C2
    if s != source: 
      total_in = 0
      total_out = 0
      for neighbor in in_degree:
        total_in += flow[(neighbor.tail, neighbor.head)]
      for neighbor in out_degree:
        total_out += flow[(neighbor.tail, neighbor.head)]
      if is_equal(total_in,total_out) == False  and s != sink:
        return False
    
    # C3
    if s != sink:
      same_edge = -1
      for neighbor in out_degree:
        if same_edge < 0:
          same_edge = flow[(neighbor.tail, neighbor.head)]
        elif is_equal(same_edge,flow[(neighbor.tail, neighbor.head)]) == False:
          return False 

    for node in graph.out_edges(s):
      if (not visited[node.head]):
        stack.append(node.head)

  return True

  raise NotImplementedError('You must implement the function without changing the function name and argument list.')