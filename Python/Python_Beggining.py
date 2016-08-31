Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=5:
	
SyntaxError: invalid syntax
>>> a=5
>>> while (a>0){
	
SyntaxError: invalid syntax
>>> set path=%path%;C:\python35

SyntaxError: invalid syntax
>>> the_world=true
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    the_world=true
NameError: name 'true' is not defined
>>> a=True
>>> if a:
	print("Hello World.")

	
Hello World.
>>> #This File/Program is firt time use if python and
>>> #testing how to use it.
>>> 2+2
4
>>> 50*2
100
>>> 5/2
2.5
>>> #compared to netbeans the float is already in the system
>>> 100/2
50.0
>>> 17/3
5.666666666666667
>>> 17//3
5
>>> # use // to stop the float
>>> 5/3
1.6666666666666667
>>> 5//3
1
>>> 5%3
2
>>> 5*2+2+3
15
>>> 5+5*2
15
>>> 5**2
25
>>> n
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> 5*2.5
12.5
>>> 17/3
5.666666666666667
>>> round(_,2)
5.67
>>> "spam"
'spam'
>>> 'spam'
'spam'
>>> 'spam\'t'
"spam't"
>>> 'don't'
SyntaxError: invalid syntax
>>> 'dont\'t'
"dont't"
>>> "don't"
"don't"
>>> #fro sting use " so that in words like
>>> #don't the ' will apperare and requier
>>> #and will keep you from not making a
>>> #mistake with \'
>>> s="who are you"
>>> s
'who are you'
>>> print(s)
who are you
>>> print('C:\some\name'
      )
C:\some
ame
>>> print(r'C:some\name')
C:some\name
>>> "this is how you \n make a new line
SyntaxError: EOL while scanning string literal
>>> "This is how you \n make a new line"
'This is how you \n make a new line'
>>> print("This is how you \n print a new line")
This is how you 
 print a new line
>>> print("""\
usage; thing [OPTIONS]
	-h
	-H somthing
""")
usage; thing [OPTIONS]
	-h
	-H somthing

>>> 3*'a'+'ndrew'
'aaandrew'
>>> pre ='py'
>>> pre+'thon
SyntaxError: EOL while scanning string literal
>>> pre
'py'
>>> pre+'thon'
'python'
>>> word[-1]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    word[-1]
NameError: name 'word' is not defined
>>> word='python'
>>> word[0]
'p'
>>> word[5]
'n'
>>> word[0;1]
SyntaxError: invalid syntax
>>> word[0:1]
'p'
>>> word[0:2]
'py'
>>> word[2:5]
'tho'
>>> word
'python'
>>> word[:5}
SyntaxError: invalid syntax
>>> word[:5]
'pytho'
>>> word[-6]
'p'
>>> word[-2:]
'on'
>>> word[-6:-3}
SyntaxError: invalid syntax
>>> word[-6:-3]
'pyt'
>>>  word[-6:3]
 
SyntaxError: unexpected indent
>>> word[-6:3]
'pyt'
>>> word[20]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    word[20]
IndexError: string index out of range
>>> word[0]=J
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    word[0]=J
NameError: name 'J' is not defined
>>> word[0]='J'
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    word[0]='J'
TypeError: 'str' object does not support item assignment
>>> word[0]="J"
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    word[0]="J"
TypeError: 'str' object does not support item assignment
>>> word[2:]
'thon'
>>> 'J'+word[1:]
'Jython'
>>> s=thelangthofthisword
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    s=thelangthofthisword
NameError: name 'thelangthofthisword' is not defined
>>> s='howlongisthisword'
>>> len(s)
17
>>> squares=[0,1,2,3,4,5]
>>> squares
[0, 1, 2, 3, 4, 5]
>>> squares[2]
2
>>> squares+[6,7,8]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> squares[6]
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    squares[6]
IndexError: list index out of range
>>> square[2]=3
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    square[2]=3
NameError: name 'square' is not defined
>>> squares[2]=3
>>> squares
[0, 1, 3, 3, 4, 5]
>>> 
