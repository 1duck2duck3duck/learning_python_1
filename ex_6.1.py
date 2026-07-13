
def cube(x, y):
    """Возводит х в тепень у (в данном случае 3)"""
    product_cube = x ** y
    return product_cube

x = int(input("Please enter char x:  "))
y = 3

print(cube(x, y))


def greet(name):
    """Возвращает Hello <name>!"""
    print(f"Hello, {name}!")

name = input("Please enter name:  ")
print(greet(name))
