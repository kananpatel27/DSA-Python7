n = int(input("Enter a number: "))

print("Divisors of", n, "are:")

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        print(i, end=" ")
        
        if i != n // i:   
            print(n // i, end=" ")