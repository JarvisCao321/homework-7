number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))

plus = number1 + number2
minus = number1 - number2
multiply = number1*number2
divide = number1 / number2

print(plus)
print(minus)
print(multiply)
print(divide)

def calc_lcm (x, y):

              if x > y:

                             greater = x

              else:

                             greater = y

              while (True):

                             if ((greater % x == 0) and (greater % y == 0 )):

                                            lcm = greater 

                                            break 

                             greater += 1

              return lcm 

print("The LCM of the provided two numbers is", calc_lcm (number1, number2))