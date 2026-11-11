


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b    

def multiply(a, b):
    return a * b

# error handling of divide function
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None


x = add(14, 15 )
y = subtract(14, 15 )
z= multiply(14, 15 )
w = divide(14, 15 )

print(x,y,z,w)