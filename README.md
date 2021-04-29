# count_lines
Write a function

Input: file written in language x

Output: number of lines of code (skip empty lines and comment lines)
 
definition of comment line in language x:

1) Any line begins with '^' and ends with '$'

2) Nested comments are not supported ('^^ $' is valid comment but '^ ^ $ $' is not)

3) Multi-line comment is not supported

 
Assume all lines of code are valid and you don't need to care about the syntax

 
Examples:

// Comment line

^abcdefg$

^^lol$

 
// Not comment line

^^^^^^abcedfg

a = a + b

^^def lol$$
