#coding:utf-8

def sayHello():
	print 'Hello World'
	
sayHello()

def printMax(a,b):
	if a > b:
		print a,'is maximum'
	else:
		print b,'is maximum'
		
printMax(3,4)
x=5
y=7
printMax(x,y)

def func(x):
	print 'x is',x
	x=2
	print 'changed local x to',x
	
x=50
func(x)		#2
print 'x is still',x  #50

def func():
	global x
	print 'x is',x
	x=2
	print 'changed local x to',x

x=50
func() #50
print 'Value of x is',x #2

#默认参数
def say(message,times=1):
	print message * times
	
say('Hello')
say('world',5)


#关键字参数
def func(a,b=5,c=10):
	print 'a is',a,'and b is',b,'c is is',c
	
func(3,7)
func(25,c=23)
func(c=50,a=100)


#可变参数 元组		在函数以一个tuple中处理
def foo(*tuple_arg):
	for each_additional_arg in tuple_arg:
		print "additional_arg: ",each_additional_arg
		
foo(1,2,3,4,)

#可变参数 字典   在函数以一个字典来处理
def foo(**kwargs):
	print kwargs
	
foo(aaa=2000,bbb=3000,ccc=400000)

def power(x):
	return x * x

power(5)

#思考算法实现
def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
	
power(5,2)

#默认参数
def enroll(name,gender):
	print 'name:',name
	print 'gender:',gender
	

def enroll(name,gender,age=6,city='Beijing'):
	print 'name:',name
	print 'gander:',gender
	print 'age',age
	print 'city',city
	

enroll('Scrah','F')
enroll('Bob','M',7)
enroll('Bob','M',city='tianjin')


def add_end(L=[]):
	L.append('END')
	return L
	
add_end([1,2,3])
add_end(['x','y','z'])
add_end()
add_end() #err

#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
#如果改变了L的内容，则下次调用时，默认参数的内容就变了，
#不再是函数定义时的[]了。

#默认参数必须指向不变对象
def add_end(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L
	
def cacl(*numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum
	

nums=[1,2,3]
cacl(*nums)


def person(name,age,**kw):
	print 'name :',name,'age：',age,'other',kw
	

person('MIcheal',30)
person('Adam',45,gender='m',job='engineer')
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)

def func(a, b, c=0, *args, **kw):
	print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
	
func(1, 2, 3, 'a', 'b', x=99)
args = (1, 2, 3, 4)
w = {'x': 99}
func(*args, **kw)



def maximun(x,y):
	if x>y:
		return x
	else:
		return y
	
print maximun(2,3)


def someFunction():
	pass
	
	
def printMax(x,y):
	'''prints the maximun of two numbers.
	
	The two values must be ingegers.'''
	x=int(x)
	y=int(y)
	if x > y:
		print x,'is maximum'
	else:
		print y,'is maximun'
		
printMax(3,5)
print printMax.__doc__