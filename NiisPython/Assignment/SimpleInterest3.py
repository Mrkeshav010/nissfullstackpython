#Return value, No argument
def simple_interest():
    p = float(input("Enter Principal: "))
    r = float(input("Enter Rate: "))
    t = float(input("Enter Time: "))

    return (p * r * t) / 100

si = simple_interest()
print("Simple Interest =", si)