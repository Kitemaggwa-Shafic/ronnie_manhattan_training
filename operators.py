# Assignment Operator = ie used to assign values or operands to variables
# (#) this is used to identify comments
# (,) is used to separate joint statements ie num1,num2,num3
# Not is a unary operator that takes a single operand and returns its opposite boolean value.

# Using the not operator with boolean values
print(not True)   # Output: False
print(not False)  # Output: True

# Using the not operator with expressions that evaluate to boolean values
x = 5
y = 10
print(not (x < y))  # Output: False

my_list = [1, 2, 3]
print(not my_list)  # Output: False


# Arithmetic Operators or types in Python
'''
1. Mathematical Operators ie + - * /
2. floor division // # read about floor divion
3. Exponential operato ** ie num1 ** num2
4. Modulus (%) a remender after a division, a small value % big value you remain with small value eg 5%10 is 5
5. Comparison operators ie >, < , == (Equal), != (Not Equal), is, is not, >=, <=

'''
# Mathematical and comparison operators 
num3, num4 = 7, 10
print(num3 +  num4)
print(num3 -  num4)
print(num3 *  num4)
print(num3 /  num4)
print(num3 // num4)
print(num3 %  num4)
print(num3 >  num4)
print(num3 <  num4) 
print(num3 == num4)
print(num3 != num4)
print(num3 is num4)
print(num3 is not num4)


# Membership operators ie "in" and "Not in"
'''
# In Python, "in" and "not in" are the membership operators in a sequence (strings, lists, or tuple, set dictionary)
# 1. "in" Returns True if it finds a variable in the specified sequence and false otherwise.
#     (They are used to test whether a value or variable is found in a sequence)
# 2. "not in" Returns True if it does not finds a variable in the specified sequence and false otherwise.
'''
name = "Kitemaggwa"
 
print("a" in name) # prints True, b'se "a" is found in variable name
print('s' not in name) # prints True, b'se "s" is not found in variable name


# Example 2, using a list and membership operators
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]

if ( a in list ):
   print ("Line 1 - a is available in the given list")
else:
   print ("Line 1 - a is not available in the given list")

if ( b not in list ):
   print ("Line 2 - b is not available in the given list")
else:
   print ("Line 2 - b is available in the given list")

a = 2
if ( a in list ):
   print ("Line 3 - a is available in the given list")
else:
   print ("Line 3 - a is not available in the given list")


# Python Logical Operators
'''
Logical operators are used to combine conditional statements:
1. "and"    Returns True if both statements are true / both operands True
2. "or"     Returns True if one of the statements is true / one operand True 	  
3. "not"    Reverse the result, returns False if the result is true not  /True if the operand is False and VV
'''

a=5
b=20
print(a and b)  # will print value of b,  
'''
In Python, the (and) operator returns the first operand if it is falsy or of not above 0, otherwise, it returns the second operand.
Python first evaluates a in the expression (a and b). 
Since a is a non-zero integer, which is a truthy value in Python, a is returned. 
In summary, the expression (a and b) evaluates to b because both (a and b) are truthy values, 
and the (and) operator returns the second operand (b) when both operands are truthy.
'''
print(b and a)  # will print value of a,  

print(a or b)   # will print value of a, 
''' 
In Python, the logical operator (or) returns the first truthy value it encounters or the last operand if all operands are falsy. 
In this case, a is truthy because its value is non-zero, so (a or b) evaluates to (a) which has a value of 5.
'''
print(b or a)   # will print value of b,  

# Profic summary: (with "and" it considers last value, "or" considers the first variable if all are truly non-zero)



# logical operators of "and" continued using strings

name_1 = "Shafic"
name_2 = "Audrie"
# prints out value of name_2 (Audrie) bcoz  both are truthy values because they are non-empty strings,
print(name_1 and name_2)

