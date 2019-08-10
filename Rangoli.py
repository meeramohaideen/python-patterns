num=int(input())
num_=(num*2)-2
char=chr(num+96)
char2=''
for i in range(0,num):
    print('-'*num_+char+char2+'-'*num_)
    num_ = num_ - 2
    char=char+'-'+chr(num+96-i-1)
    char2='-'+chr(num+96-i)+char2

char1=chr(num+96)
num_=2
k=0
for j in range(0,num-1):
    print('-'*num_+char[:len(char)-4-k]+char2[k+4:]+'-'*num_)
    num_ = num_ + 2
    k=k+2
