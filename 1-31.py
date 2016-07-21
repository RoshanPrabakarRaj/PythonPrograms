Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print "hello world"
SyntaxError: Missing parentheses in call to 'print'
>>> print "hello world";
SyntaxError: Missing parentheses in call to 'print'
>>> print 1+2
SyntaxError: Missing parentheses in call to 'print'
>>> print("helloe")
helloe
>>> x=5
>>> x
5
>>> print x
SyntaxError: Missing parentheses in call to 'print'
>>> print(x)
5
>>> x="roshan"
>>> x
'roshan'
>>> print(x)
roshan
>>> 1+2
3
>>> _
3
>>> "hello"
'hello'
>>> x=10
>>> _
'hello'
>>> a="roshan"
>>> b=5
>>> print(a,b)
roshan 5
>>> len(a)
6
>>> len(x)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    len(x)
TypeError: object of type 'int' has no len()
>>> x="rdksd"
>>> x
'rdksd'
>>> len(x)
5
>>> x="hai how are you"
>>> x
'hai how are you'
>>> x.split()
['hai', 'how', 'are', 'you']
>>> x=2**5
>>> x
32
>>> y=3*4
>>> print (x+y)
44
>>> 13/3
4.333333333333333
>>> round(10.99)
11
>>> for miles in range(10,70,10)
SyntaxError: invalid syntax
>>> for miles in range(10,70,10):
	km=miles * 1.6
	print("%d miles -> %3.2f miles"%(miles,km))

	
10 miles -> 16.00 miles
20 miles -> 32.00 miles
30 miles -> 48.00 miles
40 miles -> 64.00 miles
50 miles -> 80.00 miles
60 miles -> 96.00 miles
>>> 
 RESTART: C:/Users/prosh/AppData/Local/Programs/Python/Python35-32/samples/startProgram.py 
3
>>> 
 RESTART: C:/Users/prosh/AppData/Local/Programs/Python/Python35-32/samples/startProgram.py 
3
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
 RESTART: C:/Users/prosh/AppData/Local/Programs/Python/Python35-32/samples/startProgram.py 
Traceback (most recent call last):
  File "C:/Users/prosh/AppData/Local/Programs/Python/Python35-32/samples/startProgram.py", line 1, in <module>
    print (a+2);
NameError: name 'a' is not defined
>>> 
 RESTART: C:/Users/prosh/AppData/Local/Programs/Python/Python35-32/samples/startProgram.py 
4
>>> 2 in [1,3,5]
False
>>> 2 in [2]
True
>>> def a():
	print ("roshan");

	
>>> a()
roshan
>>> type(1)
<class 'int'>
>>> type('1')
<class 'str'>
>>> type(['here','how','are'])
<class 'list'>
>>> type(('here','how','are'))
<class 'tuple'>
>>> a=[1,3,4,1,4,2,5,3]
>>> set(a)
{1, 2, 3, 4, 5}
>>> a='roshan'
>>> a.upper()
'ROSHAN'
>>> b='NFDNFEF'
>>> b.lower()
'nfdnfef'
>>> as.upper()
SyntaxError: invalid syntax
>>> 'as'.upper()
'AS'
>>> a=[1,3,5]
>>> a.append(4)
>>> print (a)
[1, 3, 5, 4]
>>> is 3<2
SyntaxError: invalid syntax
>>> 3<2
False
>>> a<c
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a<c
NameError: name 'c' is not defined
>>> 'a'<'c'
True
>>> [1,2,3,4,5]>[1,2]
True
>>> 







