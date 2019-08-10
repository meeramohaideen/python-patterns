a=int(input())
b=a*3

first=int((b-3)/2)
second=3
for i in range(1,a,2):
    print('-'*first+'.|.'*i+'-'*first)
    first=first-3

z=int((b-7)/2)
print('-'*z+'WELCOME'+'-'*z)

for j in range(a-2,0,-2):
    print('-'*second+'.|.'*j+'-'*second)
    second = second + 3
