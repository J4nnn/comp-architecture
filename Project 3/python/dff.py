from functions import *

def dff(clock, input, previous_q=None):
    """
    Simulates a master-slave D flip-flop.

    Args:
        clock: The clock signal (True or False).
        d: The data input (True or False).
        previous_q: The previous output of the DFF (for state).

    Returns:
        The current output of the DFF.
    """
    if previous_q is None:
        previous_q = False #Initial state

    mux1 = mux(clock, input, previous_q)
    mux2 = mux(not_gate(clock), previous_q, mux1)

    return mux2