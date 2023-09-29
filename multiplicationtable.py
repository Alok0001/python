def multiplication(num):
    i=1
    m =0
    for i in range(11):
        m= num * i
        print(f"{num} * {i} = {m}")

num = int(input("enter the number for multiplication table:"))
multiplication(num)
