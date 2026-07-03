a = 5 
b = 6

#Arithmetic Operators
print(a+b)
print(a-b)
print(a*b)
print(a/b) # gives answer in float. No typecasting required
print(a%b) # remainders
print(a**2) # a^2

#Relational Operators
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

#Assignment Operators
ans1 = 10 
ans1 += a 
ans2 = 4 
ans2 -= a 
ans3 = 7 
ans3 *= a 
ans4 = 3 
ans4 /= a 
ans5 = 8 
ans5 %= a 
ans6 = 2 
ans6 **= a 
print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
print(ans6)

#Relational Operators
print("NOT Operator:", not(a<b))
print("AND Operator:", (a<b) and (a==b))
print("OR Operator:", (a<b) or (a>b))