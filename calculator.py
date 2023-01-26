print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
''')
num1=int(input("Enter the value:"))
num2=int(input("Enter the value:"))
opr=input("Enter the opr..")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num2/num2)
else:
    print("invailid opr...")
# + ADD
# - SUBTRACT
# * MULTIPLY
# / DIVIDE
#
# Enter the value:11
# Enter the value:11
# Enter the opr..+
# 22
