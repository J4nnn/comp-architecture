from Dmux import dmux
from Not import not_gate

def dmux4way(sel1, sel2, input):
    """
    Routes a single input to one of four outputs based on a 2-bit select signal.
    """
    # First split
    a, b = dmux(sel1, input)
    # Second split
    q1, q2 = dmux(sel2, a)
    q3, q4 = dmux(sel2, b)
    return int(q1), int(q2), int(q3), int(q4)

    # return dmux(sel2, dmux(sel1, input)[0])[0], dmux(sel2, dmux(sel1, input)[0])[1], dmux(sel2, dmux(sel1, input)[1])[0], dmux(sel2, dmux(sel1, input)[1])[1]

# Testing, it works
# print("sel1=0, sel2=0, input=1 ->", dmux4way(0, 0, 1)) 
# print("sel1=0, sel2=1, input=1 ->", dmux4way(0, 1, 1)) 
# print("sel1=1, sel2=0, input=1 ->", dmux4way(1, 0, 1)) 
# print("sel1=1, sel2=1, input=1 ->", dmux4way(1, 1, 1))