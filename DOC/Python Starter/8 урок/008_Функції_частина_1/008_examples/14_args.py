def adder(*nums):
    print(type(nums))
    summa = 0

    for n in nums:
        summa += n

    print("Sum: ", summa)


adder(3)
adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)
