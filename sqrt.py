def bisect(target,tolerance=1e-7,max_iter=100):
    root = None

    if target < 0 :
        raise ValueError("Negative Bad!")
    if target == 1:
        root = 1
    elif target == 0:
        root = 0
    else:
        high = target
        low = 0
        for _ in range(max_iter):
            mid = (high+low)/2
            sqr_mid = mid**2
            if abs(sqr_mid-target) <= tolerance:
                root = mid
            elif sqr_mid<target:
                low = mid
            else:
                high = mid
        if root is None:
            print(f"{max_iter} was not enough!")
    return root

loop = True
print("\nWelcome! Would you like to find the square root of numbers by bisecting them?")
while loop:
    num = int(input("\nEnter number: "))
    square_root = bisect(num,1e-9,1000000)
    print(f"\nThe square root of {num} is approximately {square_root}")