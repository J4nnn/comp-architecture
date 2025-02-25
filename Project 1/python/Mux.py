from And import and_gate
from Or import or_gate
from Not import not_gate

def mux (sel, input1, input2):
    """
    Returns 'a' if 'sel' is True (1) and returns 'b' if 'sel' is False (0).
    """
    return or_gate(and_gate(input1, not_gate(sel)), and_gate(input2, sel))

# Testing
# print("sel = 0, input1 = 0, input2 = 0 -> ", mux(0, 0, 0))
# print("sel = 0, input1 = 0, input2 = 1 -> ", mux(0, 0, 1))
# print("sel = 0, input1 = 1, input2 = 0 -> ", mux(0, 1, 0))
# print("sel = 0, input1 = 1, input2 = 1 -> ", mux(0, 1, 1))

# print("sel = 1, input1 = 0, input2 = 0 -> ", mux(1, 0, 0))
# print("sel = 1, input1 = 0, input2 = 1 -> ", mux(1, 0, 1))
# print("sel = 1, input1 = 1, input2 = 0 -> ", mux(1, 1, 0))
# print("sel = 1, input1 = 1, input2 = 1 -> ", mux(1, 1, 1))