def user_move(rod1,rod2):
    if not rod1:
        print("\nMove not Allowed!")
        return
    if rod2 and rod2[-1] < rod1[-1]:
        print("\nMove not Allowed!")
        return
    rod2.append(rod1.pop())

def display(n,rods,char="_",offset = 4):
    lines = []
    base = n*2-1
    rod_off = int((base-1)/2)
    new_rods = {
        rod:[] for rod in rods
    }
    for rod in new_rods:
        copy = rods[rod][:]
        copy.reverse()
        new_rods[rod]=[0 for x in range(n-len(copy))]
        new_rods[rod].extend(copy)
    for i in range(n):
        lines.append("")
        for rod in new_rods:
            disk = new_rods[rod][i]
            if disk == 0:
                lines[i] += rod_off*" "+"|"+(rod_off+offset)*" "
            else:
                disk_size = (disk*2-1)
                disk_off = int((base-disk_size)/2)
                lines[i] += disk_off*" "+char*disk_size+(disk_off+offset)*" "
    string = 50*"\n"+"\n".join(lines)
    print(string)

def valid(command):
    if len(command) != 2 or not command.isalpha():
        print(f"{command} is not valid!\tPlease try again!")
        return False
    valid_letters = ["A","B","C"]
    if valid_letters.count(command[0]) == 0 or valid_letters.count(command[1]) == 0:
        print(f"{command} is not valid!\tPlease try again!")
        return False
    return True

def game(n,rods):
    print("\nSpecify the start and the end like this [AB] to move the top disk from A and put it in B") 
    while True:
        display(n,rods)
        if len(rods["C"]) == n:
            return True
        command = input("\nWhat's your next move? ")
        if valid(command):
            user_move(rods[command[0]],rods[command[1]])

if __name__ == "__main__":
    while True:
        print("\nWelcome to the Terminal Hanoi puzzle game! made by Alex")
        command = input("\nHow many disks would you like to play with? ")
        if not command.isnumeric:
            print(f"{command} is not a number!\tPlease try again!")
            continue
        n = int(command)
        rods = {
            "A":list(range(n,0,-1)),
            "B":[],
            "C":[]
            }
        if game(n,rods):
            print(f"\nCongratulations! You solved the Hanoi puzzle with {n} disks")
            retry = input("\nWould you like to play it again? Press [Y] to continue, any other to quit: ")
            if retry != "Y":
                print("\nThanks for playing! Quitting 'hanoi.py' by Alex ...")
                break