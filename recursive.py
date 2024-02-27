# Factorial function 
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
# Main Function
def main():
    n = int(input("Please enter a non negative integer? "))
    factorial_ans = factorial(n)
    print(f"The factorail of {n} is {factorial_ans}")

# Calls Function
main()
    
