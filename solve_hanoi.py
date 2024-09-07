import hanoi
n = 3
rods = {
    "A":list(range(n,0,-1)),
    "B":[],
    "C":[]
    }

def allow(rod1,rod2):
    forward = False
    if not rod2:
        forward = True
    elif rod1 and rod2[-1] > rod1[-1]:
        forward = True
    if forward:
        rod2.append(rod1.pop())
    else:
        rod1.append(rod2.pop())

def solve(num,start="A",aux="B",end="C"):
    moves = 2**num -1
    for i in range(moves):
        rem = (i+1)%3
        if rem == 1:
            if num%2 == 0:
                allow(rods[start],rods[aux])
            else:
                allow(rods[start],rods[end])
        elif rem == 2:
            if num%2 == 0:
                allow(rods[start],rods[end])
            else:
                allow(rods[start],rods[aux])
        elif rem == 0:
            allow(rods[aux],rods[end])
        hanoi.display(n,rods)
        
hanoi.display(n,rods)
solve(n)
