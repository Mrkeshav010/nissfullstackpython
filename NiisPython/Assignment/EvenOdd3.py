#Return value, No argument
def check():
    n = int(input("Enter number: "))
    return n % 2

if check() == 0:
    print("Even")
else:
    print("Odd")