#Accept a number from user nd determine whether it is a prime number or not. If it is a prime number, then print the factors of that number.    
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print("Factors of", num, "are:")
            for j in range(1, num + 1):
                if (num % j) == 0:
                    print(j)
            break
    else:
        print(num, "is a prime number")