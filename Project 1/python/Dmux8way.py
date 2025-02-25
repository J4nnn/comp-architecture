from Dmux import dmux
from Dmux4way import dmux4way

def dmux8way(sel1, sel2, sel3, input):
    """
    Routes a single input to one of eight outputs based on a 3-bit select signal.
    """
    # First split
    a, b = dmux(sel1, input)
    # Second split
    c, d, e, f = dmux4way(sel2, sel3, a)
    g, h, i, j = dmux4way(sel2, sel3, b)
# 
    return c, d, e, f, g, h, i, j
    # return dmux4way(sel2, sel3, dmux(sel1, input)[0])[0], dmux4way(sel2, sel3, dmux(sel1, input)[0])[1], dmux4way(sel2, sel3, dmux(sel1, input)[0])[2], dmux4way(sel2, sel3, dmux(sel1, input)[0])[3], dmux4way(sel2, sel3, dmux(sel1, input)[1])[0], dmux4way(sel2, sel3, dmux(sel1, input)[1])[1], dmux4way(sel2, sel3, dmux(sel1, input)[1])[2], dmux4way(sel2, sel3, dmux(sel1, input)[1])[3]

# Testing, it works
# print("sel=000, input=1 -> ", dmux8way(0, 0, 0, 1))
# print("sel=001, input=1 -> ", dmux8way(0, 0, 1, 1))
# print("sel=010, input=1 -> ", dmux8way(0, 1, 0, 1))
# print("sel=011, input=1 -> ", dmux8way(0, 1, 1, 1))
# print("sel=100, input=1 -> ", dmux8way(1, 0, 0, 1))
# print("sel=101, input=1 -> ", dmux8way(1, 0, 1, 1))
# print("sel=110, input=1 -> ", dmux8way(1, 1, 0, 1))
# print("sel=111, input=1 -> ", dmux8way(1, 1, 1, 1))