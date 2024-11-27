# tutorial4

name=input("What is your name?")


a=int(input("What is a?"))

b=int(input("What is b?"))

c=int(input("What is c?"))

d=int(input("What is d?"))

def solvecubic(a,b,c,d):

    A=-(b**3)/(27*(a**3))+(b*c)/(6*a**2)-(d/2*a)
    B=(c)/(3*a)+(-b**2)/(9*a**2)
    C=b/(3*a)
    x=(A+(A**2+B**3)**(1/2))**(1/3)+(A-(A**2+B**3)**(1/2))**(1/3)-C
    P="The root of the cubic is"+x
    return(P)

print("Hello "+name+", I can slove the cubic")

print(solvecubic(a,b,c,d))

quit()
