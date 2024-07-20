def verify(card):
    reverse = card[::-1]
    odd = 0
    for i in reverse[::2]:
        odd += int(i)
    even = 0
    for i in reverse[1::2]:
        num = int(i)*2
        if num >= 10:
            num = num//10+num%10
        even += num
    total = odd+even
    return total%10 == 0
def main():
    num = (input("\nWrite a Card Number: "))
    if verify(num):
        print(num+" is VALID!")
    else:
        print(num+" is INVALID!")
while True:
    main()
    