def add(*args):
    sum=0
    for n in args:
        sum = sum + n
        print(f"+ {n}" )
    print(f"= {sum}")

def calculate(**kwargs):
    print(kwargs)
    print(kwargs["add"])
    print(kwargs["multiply"])

calculate(add=3, multiply=5)

