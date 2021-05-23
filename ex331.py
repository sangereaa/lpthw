def numbersss(s,b):
    i = 0
    numbers = []

    while i < s:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + b
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)