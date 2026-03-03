#typecasting
#----implicit typecasting----#
# automatic casting:
# for example:
x=10
y = 3.3
z= x + y
print(z) # changed int to float

#----explicit typecasting----#
# manual casting:
#for example:
a = 10
b= "abc"
c = "3456789"
print(float(a))
print(str(a))
print(bool(a))

print(list(b))
print(list(c))
print(int(c)+a +1 )

#-----input-----#

name = str(input("Enter your name: "))
print(name)