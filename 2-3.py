Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=14
>>> while a:
	print (a),
	a-=1
	print ("roshan")

	
14
(None,)
roshan
13
(None,)
roshan
12
(None,)
roshan
11
(None,)
roshan
10
(None,)
roshan
9
(None,)
roshan
8
(None,)
roshan
7
(None,)
roshan
6
(None,)
roshan
5
(None,)
roshan
4
(None,)
roshan
3
(None,)
roshan
2
(None,)
roshan
1
(None,)
roshan
>>> user_input = raw_input("enter a integer:")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    user_input = raw_input("enter a integer:")
NameError: name 'raw_input' is not defined
>>> def squared(s):
	t=s**s
	print(s,"raised to the power is",s,"is",t)
	return t

>>> result = squared(3)
3 raised to the power is 3 is 27
>>> result
27
>>> import math
>>> math.pi
3.141592653589793
>>> a="sds"!
SyntaxError: invalid syntax
>>> roshan = "1+2"
>>> print (rosgan)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print (rosgan)
NameError: name 'rosgan' is not defined
>>> x=raw_input("enter a number")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x=raw_input("enter a number")
NameError: name 'raw_input' is not defined
>>> x=input("enter a number : ")
enter a number : 23
>>> x*2
'2323'
>>> x**2
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> 
