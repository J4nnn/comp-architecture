from And import and_gate
from Not import not_gate

def dmux(sel, input):
    """
    Routes the input to output 'a' if 'sel' is False (0) and to output 'b' if 'sel' is True (1).
    """
    return and_gate(input, not_gate(sel)), and_gate(input, sel)

# Testing the 1:2 DEMUX
# print("sel = 0, input  = 0 -> ", dmux(0, 0))
# print("sel = 0, input  = 1 -> ", dmux(0, 1))
# print("sel = 1, input  = 0 -> ", dmux(1, 0))
# print("sel = 1, input  = 1 -> ", dmux(1, 1))