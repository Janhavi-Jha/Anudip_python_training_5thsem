#Accept a number from user nd determine whether it is a prime number or not. If it is a prime number, then print the factors of that number.    
num = int(input("Enter a number: "))
#validating the number
if num < 0:
    print("Negative numbers are not prime numbers.")
    #verifying if the number is 0 or 1
elif num == 0 or num == 1:
    print(num, "is not a prime number.")
#verifying whether prime or not
if num > 1:
    for i in range(2, num//2 + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print("Factors of", num, "are:")
            #printing factors of the number
            for j in range(1, num + 1):
                if (num % j) == 0:
                    print(j)
            break
    else:
        print(num, "is a prime number")
        