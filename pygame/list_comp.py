tbl = range(10)
new = [str(x/2) if x%2 == 0 else str(3*x+1) for x in tbl]
string = "_".join(new)
print(string)
