import numpy as np

a=np.array([0,1,0,1,0])
b=np.array([1,0,1,0,1])
a*b

a=np.array([0,1])
b=np.array([1,0])
np.dot(a,b)
a=np.array([1,1,1,1,1])
a+10
A='1234567'
A[1::2]
Name="Michael Jackson"
Name.find('el')
A='1'
B='2'
A+B

F="You are wrong"
F.upper()
tuple1=("A","B","C" )

tuple1[-1]
A=((11,12),[21,22])
A[1]
'1,2,3,4'.split(',')
A=[1,'a']
B=[2,1,'d']

A+B
a=set(A)
V={'A','B'}
V.add('C')
V
V={'A','B','C' }
V
x="Go"

if(x!="Go"):

    print('Stop')

else:

    print('Go ')

print('Mike')
x="Go"

if(x=="Go"):

    print('Go ')

else:

    print('Stop')

print('Mike')
for n in range(3):

    print(n)
for n in range(3):

    print(n+1)
A=['1','2','3']

for a in A:

    print(2*a)
def Add(x,y):
    z=y+x
    return(y)
Add('1','1')

class Points(object):

    def __init__(self,x,y):

        self.x=x

        self.y=y

def print_point(self):

    print('x=',self.x,'y=',self.y)
class Points(object):

    def __init__(self,x,y):

        self.x=x

        self.y=y

    def print_point(self):

        print('x=',self.x,' y=',self.y)
p1=Points(1,2)
p1.print_point()

class Points(object):

    def __init__(self,x,y):

        self.x=x

        self.y=y

    def print_point(self):

        print('x=',self.x,' y=',self.y)
p2=Points(1,2)

p2.x=2

p2.print_point()
