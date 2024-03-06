# Get the greatest common divisor of two numbers

# this is the recursive version in getting the
# greatest common divisor of two numbers
def recursiveGCD(a,b):
    if b == 0:
        return a
    else:
        return recursiveGCD(b, a%b)
    
# this is using the Euclidean Algorith to get the
# greatest common divisor of two numbers
def euclideanGCD(a,b):
    while b != 0:
        a, b = b, a%b
    return a

def main():
    a = int(input("Enter first number:\t"))
    b = int(input("Enter second number:\t"))
    
    print("\nUsing Recursion")
    print("The greatest common divisor of", a, "and", b, "is", recursiveGCD(a,b), "\n")
    
    print("Using Euclidean Algorithm")
    print("The greatest common divisor of", a, "and", b, "is", euclideanGCD(a,b))
    
if __name__ == "__main__":
    main()