from networkx.utils.backends import _dispatchable

@_dispatchable
def is_graphical(sequence, method: str = "eg"): ...
@_dispatchable
def is_valid_degree_sequence_havel_hakimi(deg_sequence): ...
@_dispatchable
def is_valid_degree_sequence_erdos_gallai(deg_sequence): ...
@_dispatchable
def is_multigraphical(sequence): ...
@_dispatchable
def is_pseudographical(sequence): ...
@_dispatchable
def is_digraphical(in_sequence, out_sequence): ...
