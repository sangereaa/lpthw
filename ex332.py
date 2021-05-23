def numbersss(s,l):
    i = 0
    numbers = []


    for a in range(0,s):
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + l
        print("Numbers now: ",numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)

   