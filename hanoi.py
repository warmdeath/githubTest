
rods = {
    'A': list(range(3, 0, -1)),
    'B': [],
    'C': []
}


def move(start,end):
    disk1 = rods[start][len(rods[start])-1]
    rods[end].append(disk1)
    rods[start].remove(disk1)
    pass


print(rods)
move("A","B")
print(rods)
