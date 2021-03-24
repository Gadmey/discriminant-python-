import math
a = input("Enter the coefficient a: ")
b = input("Enter the coefficient b: ")
c = input("Enter the coefficient c: ")

if a == "0":
    print("The coefficient a cannot be equal to 0")

elif b == "0":
    print("The coefficient b cannot be equal to 0")

elif c == "0":
    print("The coefficient c cannot be equal to 0")

else:
    print("discriminant formula: D=b^2 -4*a*c")


dis = pow(int(b), 2) -4*int(a)*int(c)
print ("D= "+str(dis))


if dis > 0:
    x1 = (-int(b) - math.sqrt(dis)) / (2 * int(a))
    x2 = (-int(b) + math.sqrt(dis)) / (2 * int(a))
    print ("x1=" + str(x1))
    print ("x2=" + str(x2))

elif dis == 0:
    x1 = (-int(b)) / (2 * int(a))
    print ("x1 =" + str(x1))

elif dis < 0:
    print ("no roots")