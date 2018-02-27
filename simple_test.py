from flow import Apparatus, Protocol
from components import Tube, Vessel, ViciValve, Component

a = Component(name="a")
b = Component(name="b")
c = Component(name="c")
# input_vessel = Vessel("`glucose`, `indium(iii) bromide`, and `triflic acid` in a 50/50 mix of `chloroform` and `acetonitrile`", resolve=False)
test = ViciValve(name = "test_1", mapping = dict(a = 1, b = 2, c = 3))

A = Apparatus()
A.add(a, test, Tube("1 foot", "1/16 in", "2/16 in", "PVC"))
A.add(b, test, Tube("1 foot", "1/16 in", "2/16 in", "PVC"))
A.add(c, test, Tube("1 foot", "1/16 in", "2/16 in", "PVC"))


P = Protocol(A)
P.add(test, setting = "a", start_time="3 secs", stop_time="4 secs")
P.add(test, setting = "b", start_time="4 secs", stop_time="5 secs")
P.add(test, setting = "c", start_time="5 secs", stop_time="6 secs")
print(P.json())
P.execute("http://127.0.0.1:5000/submit_protcol")