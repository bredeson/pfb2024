Programming For Biology 2017
===========================


Instructors
============
Simon Prochnik  
Sofia Robb  
    
***

Table of Contents
 * [Big Picture](#big-picture)
 * [Unix](#unix)
     * [Unix Overview](#unix-overview)
     * [Getting Around](#getting-around)  
     * [Getting things done](#getting-things-done)
     * [Text Editors](#text-editors)
     * [Git for Beginners](#git-for-beginners)
  * [AWS](#aws)
     * [AWS Overview](#aws-overview)
  * [Python](#python)
     * [Python Overview](#python-overview)
     * [Running Python](#running-python)
     * [Syntax](#syntax)
     * [Data Types and Variables](#data-types-and-variables)
     * [Operators](#operators)
     * [Truth](#truth)
     * [Logic: Control Statements](#logic-control-statements)
     * [Numbers](#numbers)
     * [Strings](#strings) 
     * [Tuples and Lists](#tuples-and-lists)
     * [Loops](#loops)
     * [Files: I/O](#files-io)
     * [Dictionaries and Sets](#dictionaries-and-sets)
     * [Functions](#functions)
     * [Modules](#modules)
     * [Exceptions](#exceptions)
     * [Classes](#classes) 
     * [Datastructures](#datastructures)
 * [BioPython](#biopython)
    * [BioPython Overview](#biopython-overview)
    * [BioPython Subtopic 1](#biopython-subtopic-1)
    * [BioPython Subtopic 2](#biopython-subtopic-2)
 * [My Questions](#my-questions)
 * [Bioinformatic Analysis and Tools](#bioinformatic-analysis-and-tools)
   * [Bioinformatic Analysis and Tools Overview](#bioinformatics-analysis-and-tools-overview)
   * [Sequence Search and Alignments](#sequence-search-and-alignments)
   * [Assembly](#assembly)
   * [NGS](#ngs)
   * [Variant Calling](#variant-calling)
   * [Ontology](#ontology)

  
  
***  


Big Picture
=======================
Why is it important for Biologists to learn to program?

What are our tips for being successful in your efforts to learn to program?
1. Practice, practice, practice. Please, spend as much time possible actually coding.
2. Write only a line or two of code, then test it. If you write too many lines, it becomes more difficult to debug if there is an error.
3. Errors are not failures. Every error you get is a learning opportunity. Every single error you debug is a major success. Fixing errors is how you will cement what you have learned.
4. Don't spend too much time trying to figure out a problem. We are here to help. It is important for you to try and solve an isssue on your own but not for you to waste your time. We want to help you to independently solve your problem.
5. Lectures are important, but the practice is more important.
6. Review sessions are important, but practice is more important.
6. It is essential that we help you to learn how to find solutions on your own.

***
# Unix
***

Unix Overview
=============



Getting Around  
==============
 - ls  
 - cd  
 - cp  
 - rm  
 - cat  
 - less/more  
 - grep  
 - wc
 - ssh
 - scp 


Getting things done
==================
 - sort
 - uniq
 - awk
 - sed
 - perl
 - for

Text Editors
============


Git for Beginners
=================


***
# AWS
***  



AWS Overview
============

Note: I think it would work nicely if we can get prepaid visa credit cards for each student, $50 maybe. Then we can have each of them 

- create an account
- log in
- create and launch an instance
- ssh into instance

  
  

***
# Python
***
  
  


Python Overview
===============
 * We are teaching the simplest form of the language, no 'clever' stuff.
 * We can expand on this in subsequent years

Functions and statements we are NOT covering
`assert`

Language basics: 3.x, interpreted, slow, python notebook eg jupyter


Python has 
- data types
- objects
- classes
- functions
- methods

__Data types__ are just different types of data which are discussed in more detail later. Examples of data types are integers and strings.  

__Objects__ are a organized collection of predefined data and code to act on that data

__Classes__ is an instance of an object that you can create and will usually add a specific piece of data to.

__Funtions__ are a grouping of code that does something specific. There are functions that are built into Python. You can create your own functions. 

__Methods__ is a function that belongs to an object and can only work on the data stored in the object.




Running Python
==============  


Interactive Interpreter
-----------------------
Python can be run one line at a time in an interactive interpreter.  
To lauch the interpreter type the following into your terminal window:  
  
`$ python`    
Note: '$' indicates the command line prompt  

First Python Script:
```bash
$ python
```  


```python
>>> print ("Hello, PFB2017!")
Hello, PFB2017!
```  

> Note: `print` is a function.



Script Programming
-----------------------
Calling the python commnad with a script name as an argument will cause the execution of the script.  

__Python Script__
* The same code from above is typed into a text file. 
* This file will have the extension .py. 

File Contents:  
```python
#!/usr/bin/python3
print ("Hello, PFB2017!")
```  

Execute the Python script:
```bash
$ python test.py 
```

This produces the following result:
```bash
Hello, PFB2017!
```






Syntax
=======

@sep example code, statements, functions(), tab spacing, interactive interpreter, debugger

__Python Identifiers__: 
A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).

Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive programming language. Thus, seq_id and seq_ID are two different identifiers in Python.

__Naming conventions for Python Identifiers__: 
 * 1st character is lowercase, unless it is a name of a Class. Classes should begin with an uppercase characters. (ex. seq)
 * Private identifiers begin with an underscore. (ex. \_private)
 * Strong private identifiers begin with two underscores. (ex. \_\_private)
 * Language-defined special names begin and end with two underscores. (ex.\_\_special\_\_)

__Reserved Words__: 
The following is a list of Python keywords. These are special words that already have a purpose in python and therefore cannot be used in indentifier names.

```
and         exec        not
as          finally     or
assert      for         pass
break       from        print
class       global      raise
continue    if          return
def         import      try
del         in          while
elif        is          with
else        lambda      yield
except
```

__Lines and Indentation__: 
Python does not use braces({}) to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation. Incorrect line spacing and indention will cause an error to be reported.

The number of spaces in the indentation need to be consistent but a specific number is not required. All lines of code, or statements, within a single block must be indented in the same way. For example:


__Comments__: 
Comments are a good programming practice. Making a note of what a line or block of code is doing will help the writer and readers of the code.

__#__ : 
The pound or hash symbol is used to prepend a comment. All characters after the # and to the end of the line are apart of the comment and it will not be interpreted. 
```python
#!/usr/bin/python3

# this is my first script
print ("Hello, PFB2017!") # this line prints
```


__Blank Lines__: 
Blank lines are also important for increasing the readability of the code. Blank lines are ignored by the interpreptor


__Python Options__: 
```bash
$ python -h
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser (also PYTHONDEBUG=x)
-E     : ignore environment variables (such as PYTHONPATH)
-h     : print this help message and exit
```






Data Types and Variables
========================
sep note:  overview of all types: start with constants: numbers, strings '' "" ''' ''' r'' = raw strings, + for concat, * for repeat
iterable, string, int, float, tuple, list, dictionary, set  

This is our first look at the 5 data types and variables. Each will be discussed in more detail in subsequent sections. 

- Variables enable you to store a value in memory. 
- Simply use the equal sign, '=', to assign a value to a variable.  


For Example:  
```python
first_variable = 5
```  

Differnt types of data can be assigned to variables, i.e., intergers, floats, and strings.
  
For Example:
```python
count   = 10     # this is an integer
average = 2.5    # this is a float
message = "Welcome to python" # this is a string
```  

10, 2.5, and "Welcome to python" are singular pieces of data being stored in an indivudual variables.  
  
Collections of data can also be stored in an individual variable, i.e., lists, tuples, and dictionaries.  
 
 <p>&nbsp;</p>
  
__List__  
- Lists are used to store an ordered, *indexed* collection of data.
- Values are separated by commas
- Values are enclosed in square brackets '[]'
- Lists can grown and shrink
- Values are mutatable
  
  
```python
codons = [ 'atg' , 'aaa' , 'agg' ]
```  
  
  
Index | Value
------|-------
0 | atg
1 | aaa
2 | agg

  <p>&nbsp;</p>
  
__Tuple__
- Tuples are similar to lists and contain ordered, *indexed* collection of data.
- Items are separated by commas
- **Items are enclosed in parenthesis '()'**
- **Tupels cannot change in size**
- **Values are immutable**
  
  
```python
months = ( 'Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun' , 'Jul' , 'Aug' , 'Sep' , 'Oct' , 'Nov' , 'Dec' )
```
  
  
Index | Value
------|-------
0 | Jan
1 | Feb
2 | Mar
3 | Apr
4 | May
5 | Jun
6 | Jul
7 | Aug
8 | Sep
9 | Oct
10 | Nov
11 | Dec

<p>&nbsp;</p>
  
__Dictionary__
- Dictionaries are unordered collections of key/value pairs.
- Sets of Key/Value pairs are separated by commas 
- A key and value are grouped with a colon
  
  
```python
genes = { 'TP53' : 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC' , 'BRCA1' : 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' }
```  
  
  
Key | Value
------|-------
TP53 | GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC
BRCA1 | GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA

  
   <p>&nbsp;</p>
   
__Type Conversion__
Sometimes you may need to convert data into a specific type. Here are some examples of functions that will help you to do this.
  
  
Function | Description
---------|------------
int(x) | Converts x to an integer.
float(x) | Converts x to a floating-point number.
str(x) | Converts x to a string.
chr(x) | Converts an integer to a character.
tuple(s) | Converts s to a tuple.
list(s) | Converts s to a list.
set(s) | Converts s to a set.
dict(d) | Creates a dictionary. d must be a sequence of (key,value) tuples.



__Should we include these??? I think they are too complicated__   

Function | Description
---------|------------
eval(str) | Evaluates a string and returns an object.
complex(real [,imag]) | Creates a complex number.
repr(x) | Converts x to an expression string.
frozenset(s) | Converts s to a frozen set.
unichr(x) | Converts an integer to a Unicode character.
ord(x) | Converts a single character to its integer value.
hex(x) | Converts an integer to a hexadecimal string.
oct(x) | Converts an integer to an octal string.


  
  

Operators
==========
@sep These depend on the type of variable, so revisit the most relevant ones in subsequent sections
include // floor division and % modulus
  
  
<p>&nbsp;</p>  

__Arthmetic Operators__  


Operator | Description | Example | Result
---------|-------------|---------|-------   
\+        | Addition    | 3+2     |  5
\-        | Subtraction | 3-2     |  1
\*        | Multiplication | 3\*2 | 6
\/        | Division    | 3/2     | 1.5
\%        | Modulus (divides left operand by right operand and returns the remainder)    | 3%2     | 1
\*\*       | Exponent    | 3\*\*2  | 9
\//       | Floor Division (result is the quotient with digits after the decimal point removed. If one of the operands is negative, the result is floored, i.e., rounded away from zero | 3//2  ; -11//3 | 1 ; -4

<p>&nbsp;</p>  

__Assignment Operators__  

Operator | Equivalent to | Example | result evaluates to 
---------|---------------|---------|---------------------
\=       | a = 3         | 	result = 3 |  3
\+= | result = result + 2 | result = 3 ; result += 2 | 5
\-= | result = result - 2 | result = 3 ; result -= 2 | 1
\*= | result = result * 2| result = 3  ; result \*= 2 | 6
/=  | result = result / 2 | result = 3 ; result /= 2 | 1.5
%=  | result = result % 2 | result = 3 ; result %= 2 | 1 	
\*\*= | result = result \*\* 2 | result = 3 ; result \*\*= 2 | 9 
//=  | result = result // 2 | result = 3 ; result //= 3 | 1 

<p>&nbsp;</p>  



__Comparison Operators__  

These operators compare two values and returns true or false.  


Operator | Description | Example | Result
---------|-------------|---------|-------   
==       | equal to    | 3 == 2  | False
!=       | not equal   | 3 != 2  | True
\>        | greater than | 3 \> 2  | True
\<        | less than   | 3 \< 2  | False
\>=       | greater than or equal   | 3 \>= 2  | True
\<=       | less than or equal  | 3 \<= 2  | False

<p>&nbsp;</p>  

__Logical Operators__
 
Operator | Description | Example | Result
---------|-------------|---------|--------
and | True if left operand is True and right operand is True | bool(3>=2 and 2<3) | True
or | TRUE if left operand is Treu or right operand is True | bool(3==2 or 2<3) | True
not | Reverses the logical status | bool(not False)  | True

<p>&nbsp;</p>  

__Membership Operators__  

Operator | Description
---------|-------------
in      | True if a value is included in a list, tuple, or string  
not in  | True if a value is absent in a list, tuple, or string

For Example:  
```python
>>> dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
>>> 'TCT' in dna
True
>>>
>>> 'ATG' in dna
False
>>> 'ATG' not in dna
True

```

<p>&nbsp;</p> 

__Operator Precedence__

Operators are listed in order of precedence. Highest listed first. Not all the operators listed here are mentioned above. 

Operator | Description	
---------|------------
\*\* | Exponentiation (raise to the power)
\~ \+ \- | Complement, unary plus and minus (method names for the last two are +@ and -@)
\* / % // | Multiply, divide, modulo and floor division
\+ \- | Addition and subtraction
\>> \<< | Right and left bitwise shift
\& |  Bitwise 'AND'
\^ \| | Bitwise exclusive 'OR' and regular 'OR'
\<= < > >= | Comparison operators
\<> == != | Equality operators	
\= %= /= //= -= += \*= \*\*= | Assignment operators
is is not | Identity operators
in not in |  Membership operators
not or and | Logical operators


Truth
======
Lets take a step back, What is truth?  

Everything is true, except for:  
- 0
- None
- False
- '' (empty string)
- [] (empty list)
- () (empty tuple)
- {} (empty dictionary)

Which means that these are True
- '0'
- 'None'
- 'False'
- 'True'
- ' ' (string of one blank space)

<p>&nbsp;</p>  

__Use bool() to test for truth__  

```python
>>> bool(True)
True
>>> bool('True')
True
>>>
>>>
>>> bool(False)
False
>>> bool('False')
True
>>>
>>>
>>> bool(0)
False
>>> bool('0')
True
>>>
>>>
>>> bool('')
False
>>> bool(' ')
True
>>>
>>>
>>> bool(())
False
>>> bool([])
False
>>> bool({})
False
```

<p>&nbsp;</p>





Logic: Control Statements
=========================
@sep while, if, elif, else, break, continue, 
@sep ugh: else in while loop

Control Statements are used to direct the flow of your code and create the oportunity for decision making. Control statements foundation is build on truth.

__If Statement__
- Use the If Statement to test for truth and to execute lines of code if true.  
- When the expression evaluates to true each of the statements indented below the if statment, also known as the nested statement block, will be executed.

If Statement Syntax:  
```python
if expression :
  statement
  statement
```

For Example:  
```python
dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
if 'AGC' in dna:
  print('found AGC in your dna sequence')
```
Returns:  
```
found AGC in your dna sequence
```
  

__If/Else Statement__
- The If portion of the if/else statement behave as before. 
- When the if statement is true the if nested statement block will be executed. 
- When the if statement is false the else nested statement block will be executed.

```python
dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
if 'ATG' in dna:
  print('found ATG in your dna sequence')
else:
  print('did not find ATG in your dna sequence')
```
Returns:  
```
did not find ATG in your dna sequence
```


__if/elif__
- The If portion of the if/else statement behave as before. 
- When the if statement is true the if nested statement block will be executed.
- When the if statement is false, the first elif expression will be tested. 
- When the first elif statement is true, the first elif statement block will be executed. 
- When the if and all the elif statements are false, the nested else statement block will be executed.
- The if and every elif statement are tested in order. 
- The first if/elif statement found to be true is the last statement tested. 
- All subsequent elif statements will not be tested. 
- When the if and every elif statements are false the else nested statement block will be executed  

```python
count = 60
if count < 0:
  message = "is less than 0"
  print(count, message)
elif count < 50:
  message = "is less than 50"
  print (count, message)
elif count > 50:
  message = "is greater than 50"
  print (count, message)
else:
  message = "must be 50"
  print(count, message)
```
Returns:  
```
60 is greater than 50
```

Let's change count to 20, what statement block gets executed?  

```python
count = 20
if count < 0:
  message = "is less than 0"
  print(count, message)
elif count < 50:
  message = "is less than 50"
  print (count, message)
elif count > 50:
  message = "is greater than 50"
  print (count, message)
else:
  message = "must be 50"
  print(count, message)
```
Returns:  
```
20 is less than 100
```

What happens when count is 50?  

```python
count = 50
if count < 0:
  message = "is less than 0"
  print(count, message)
elif count < 50:
  message = "is less than 50"
  print (count, message)
elif count > 50:
  message = "is greater than 50"
  print (count, message)
else:
  message = "must be 50"
  print(count, message)
```
Returns:  
```
50 must be 50
```




Numbers
========
Python recognizes 3 types of numbers, integers, float point numbers, and complex numbers. 

__integer__
- konwn as an int
- an int can be positve or negative
- and **does not** contain a decimal.

__floating point number__
- known as a float
- a floating point number can be positve or negative
- and **does** contain a decimal

__complex number__
- known as complex
- is in the form of a+bi where i is the imaginary part.

__Conversion functions__

function | Description
---------|------------
int(x)   | to convert x to a plain integer
float(x) | to convert x to a floating-point number
complex(x) | to convert x to a complex number with real part x and imaginary part zero
complex(x, y) | to convert x and y to a complex number with real part x and imaginary part y

```python
>>> int(2.3)
2
>>> float(2)
2.0
>>> complex(2.3)
(2.3+0j)
>>> complex(2.3,2)
(2.3+2j)
```


__Numeric Functions__



function | Description
---------|------------
abs(x) | The absolute value of x: the (positive) distance between x and zero.
round(x [,n]) |  x rounded to n digits from the decimal point. round(0.5) is 1.0 and round(-0.5) is -1.0.
max(x1, x2,...) | The largest positive argument is returned
min(x1, x2,...) | The smallest argument is returned

```python
>>> abs(2.3)
2.3
>>> abs(-2.9)
2.9
>>> round(2.3)
2
>>> round(2.5)
2
>>> round(2.9)
3
>>> round(-2.9)
-3
>>> round(-2.3)
-2
>>> round(-2.009,2)
-2.01
>>> max(4,-5,5,1,11)
11
>>> min(4,-5,5,1,11)
-5
```

<p>&nbsp;</p>
Many numeric functions are not built into the Python core and need to be included in our script if we want to use them. To include them at the tip of the script type: 
`import math`
<p>&nbsp;</p>
These next functions are found in the math module and need to be imported. To use these function, prepend the function with the moudule name, i.e, math.ceil(15.5)  
<p>&nbsp;</p>

math.function | Description
--------------|------------
ceil(x) | The smallest integer not greater than x is returned
floor(x) | the largest integer not greater than x is returned.
exp(x) | The exponential of x: e<sup>x</sup> is returned
log(x) | the natural logarithm of x, for x > 0 is returned
log10(x) | The base-10 logarithm of x for x > 0 is returned
modf(x) | The fractional and integer parts of x in a two-item tuple are returned.
pow(x, y) | The value of x\*\*y is returned
sqrt(x) | The square root of x for x > 0 is returned


```python
>>> import math
>>>
>>> math.ceil(2.3)
3
>>> math.ceil(2.9)
3
>>> math.ceil(-2.9)
-2
>>>
>>>
>>> math.floor(2.3)
2
>>> math.floor(2.9)
2
>>> math.floor(-2.9)
-3
>>>
>>>
>>> math.exp(2.3)
9.974182454814718
>>> math.exp(2.9)
18.17414536944306
>>> math.exp(-2.9)
0.05502322005640723
>>>
>>>
>>> math.log(2.3)
0.8329091229351039
>>> math.log(2.9)
1.0647107369924282
>>> math.log(-2.9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>>
>>>
>>> math.log10(2.3)
0.36172783601759284
>>> math.log10(2.9)
0.4623979978989561
>>>
>>>
>>> math.modf(2.3)
(0.2999999999999998, 2.0)
>>> math.modf(2.9)
(0.8999999999999999, 2.0)
>>> math.modf(-2.9)
(-0.8999999999999999, -2.0)
>>>
>>>
>>> math.pow(2.3,1)
2.3
>>> math.pow(2.3,2)
5.289999999999999
>>> math.pow(-2.3,2)
5.289999999999999
>>> math.pow(2.3,-2)
0.18903591682419663
>>>
>>>
>>> math.sqrt(25)
5.0
>>> math.sqrt(2.3)
1.51657508881031
>>> math.sqrt(2.9)
1.70293863659264
```

<p>&nbsp;</p>

A useful yet depricated function in Python 3 is cmp(x,y).  
It is used to compare two numbers.  

- if x<y -1 is returned
- if x>y 1 is returned
- x == y 0 is returned

Use this instead:  
```python
cmp = (x>y)-(x<y)
```


Strings
========
@sep
>.format()
>strip()


- Strings are collections of characters and are always surrounded by quotes.
- Strings are an example of a Python Sequence. A sequence is a positionally ordered set. A list is also a sequence. 

__Quotation Marks__
- Single (')
- Double (") 
- Triple (''' or """)   

Notes about quotes:
- Single and double quotes are the same.
- a variable will not be interpolated if placed inside of quotes.
- Triple quotes are used to span the string across multiple lines.  

Use of quotation examples:  

```python
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
```

__Strings and the print() function__
You saw examples of 
`print()`
earlier. Lets talk about it a bit more.  

print is a function that takes one or more comma separated arguments. 

Let's use the print() function to print a string:  
```python
>>>print("ATG")
ATG
```
> We get ATG printed to the screen like we expect.


Let's assign a string to a variable and print the variable
```python
>>>dna = 'ATG'
ATG
>>> print(dna)
ATG
```
> We get ATG printed to the screen


What happens if we put the variable in quotes?  
```python
>>>dna = 'ATG'
ATG
>>> print("dna")
dna
```
> The literal value of 'dna' is printed to the screen. The variable called 'dna' is not interpolated when it is inside of quotes.

Let's see what happens when we give print() two literal strings as arguments:  
```python
>>> print("ATG","GGTCTAC")
ATG GGTCTAC
```
> We get the two literal strings printed to the screen separated by a space

What if you do not want your strings separated by a space? Use the concatenation operator to concatenate the two strings before or within the print() function:  
```python
>>> print("ATG"+"GGTCTAC")
ATGGGTCTAC
>>> combined_string = "ATG"+"GGTCTAC"
ATGGGTCTAC
>>> print(combined_string)
ATGGGTCTAC
```
> We get the two strings printed to the screen without being separated by a space


Now, lets give one variable and one literal string:
```python
>>>dna = 'ATG'
ATG
>>> print(dna,"GGTCTAC")
ATG GGTCTAC
```
> We get the value of the variable and the literal string printed to the screen separated by a space

How would we print the two without a space?
```python
>>>dna = 'ATG'
ATG
>>> print(dna + "GGTCTAC")
ATGGGTCTAC
```
> We can use the concatenation operator to get the value of the variable and the literal string printed to the screen without being separated by a space

Let's try to concatenate our variable with a literal string by putting both within quotes:
```python
>>> print("dna GGTCTAC")
dna GGTCTAC
>>> print(dna + "GGTCTAC")
ATGGGTCTAC
>>>
```
> The varialbe 'dna' does not get interpolated when it is inside of quotes

__ERRORS__

Let's look at the typical errors you will encouter when you use the print() function.

What will happen if you forget to close your quotes:
```python
>>> print("GGTCTAC)
  File "<stdin>", line 1
    print("GGTCTAC)
                  ^
SyntaxError: EOL while scanning string literal
```
> We get a 'SyntaxError' if the closing quote is not used

What will happen if you forget to enclose your literal string in quotes:
```python
print(GGTCTAC)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'GGTCTAC' is not defined
```
> We get a 'NameError' when the literal string is not enclosed in quotes. 

Tuples and Lists
===============
append(x), .extend(iter) pop() insert() sort() reverse()
list comprehension 
`squares = [x**2 for x in range(10)]`
zip() -- loop over two lists at the same time
iterators: next(), generators


__Tuples__
The main reason why tuples exist is to get data to and from function calls. 

Loops
=====
for i in list: 
(ugh: else in for loop)
iterators, range()


Files: I/O
==========
with open() as f:
open()
read() readline()
write()
close()


Dictionaries and Sets
======================
for k, v in knights.items():
keys()


Functions
=========
`def, return, positional arguments, keyword arguments, *arguments **keywords`
lambda e.g.
`squares = list(map(lambda x: x**2, range(10)))`


Modules
=======
dir()
import
from bla import boo


The standard library:
os, sys, glob, shutil, math, random, statistics (scipy), zlib, sqlite3 (DB access)? urllib.request 


Regular Expressions
====================



Exceptions
==========
try/except/finally (see with/as)



Classes 
=======
`class`
scope & namespace, 
`global, nonlocal`



Datastructures
==============
import json


***
# BioPython
***


BioPython Overview
==================


BioPython Subtopic 1
--------------------


BioPython Subtopic 2
--------------------


My Questions
============


***
# Bioinformatic Analysis and Tools
***


Bioinformatic Analysis and Tools Overview
========================================
  * What you want to do:
      * tools to do it



Sequence Search and Alignments
==============================



Assembly
========

DNA
----

RNA
----



NGS
===




Variant Calling
===============




Ontology
========

