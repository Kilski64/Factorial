while True:
    n = int(input("Insert number: "))

    if n < 0:
        print("Error: Negative numbers are not allowed.")
    else:
        result = 1

        for number in range(n, 0, -1):
            result *= number

        print(f"!{n} = {result}")


  

    