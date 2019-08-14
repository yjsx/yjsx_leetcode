def test(a):
    a  = a.copy()
    a.pop(1)
    return a
a = {1:1,2:2}
b = test(a)
print(a)
print(b)