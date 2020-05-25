# 1.Write a program to Add, Subtract, Multiply, and Divide 2 numbers
a=30
b=20
Add=a+b
Sub=a-b
Mul=a*b
Div=a/b
print("Addition Value: ",Add)
print("Subtraction Value: ",Sub)
print("Multiplication Value: ",Mul)
print("Division Value: ",Div)

# 2.Write a program to find the biggest of 3 numbers (Use If Condition)
a=int(input("Enter 1st No: "))
b=int(input("Enter 2nd No: "))
c=int(input("Enter 3rd No: "))
if a>b and a>c:
  print("The Biggest no is: ",a)
elif b>a and b>c:
  print("The Biggest no is: ",b)
else:
  print("The Biggest no is: ",c)
  
# 3.Write a program to find given number is odd or Even
num=int(input("Enter a No: "))
if num%2==0 :
    print("The number",num,"is even")
else :
    print("The number",num,"is odd")
    
# 4.Write a program to find the number is Prime or not.
num=7
if num > 1 :
  for n in range(2, num):
    if  (num % n) == 0 :
      print(num,"is not a Prime Number")
      break
  else:
    print(num,"is a Prime Number")    
else:
  print(num,"not a Prime Number") 
  
  
#5.Write a program to receive 5 command line arguments and print each argument separately.
#Example : >> python test.py arg1 arg2 arg3 arg4 arg5
#a) From the above statement your program should receive arguments and print them each of them. 
#L1assignment.py
import sys
arg1,arg2,arg3,arg4,arg5=sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
print ("arg1=",arg1)
print ("arg2=",arg2)
print ("arg3=",arg3)
print ("arg4=",arg4)
print ("arg5=",arg5)

#b) Find the biggest of three numbers, where three numbers are passed as command line arguments.

arg3,arg4,arg5=int(input("Enter 3 numbers: "))
if arg3>arg4 and arg3>arg5:
  print ("the biggest no is",arg3)
elif arg4>arg3 and arg4>arg5:
  print ("the biggest no is",arg4)
else:
  print ("the biggest no is",arg5)
 
    
# 6.Write a program to read string and print each character separately.

strval=input("Enter the string: ")
for character in strval:
  print(character)
  
#a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.  
strval=input("Enter the string: ")
strval2=strval[1:-1]
print ("strval2=",strval2)
print ("strval=",strval)

#b) Repeat the string 100 times using repeat operator *
print ("strval*100 times=",strval*100)

#c) Read string 2 and concatenate with other string using + operator.
strval3=strval+" Hey there "
print ("strval3 =",strval3)


#7.Create a list with at least 10 elements in it 
  #print all elements 
str1=input("Enter the list1: ")
list1=list(str1)
print ("list1=",list1)
list2=list(input("Enter list2 elements: "))
print ("list2= ",list2)

#perform slicing 
print ("list1[1:4]= ",list1[1:4])
print ("list2[1:-2]= ",list2[1:-2])

#perform repetition with * operator 
print ("list1*2=",list1*2)

#Perform concatenation wiht other list.
print ("list1+list2= ",list1+list2)


#8.Create a tuple with at least 10 elements in it 
  #print all elements 
str1=input("Enter the tuple elements: ")
tuple1=tuple(str1)
print ("tuple1=",tuple1)

#perform slicing 
print ("tuple1[2:4]= ",tuple1[2:4])
print ("tuple1[1:-2]= ",tuple1[1:-2])

#perform repetition with * operator 
print ("tuple1*2= ",tuple1*2)

#Perform concatenation wiht other list.
print ("tuple1+(1,2,3,4,5)= ",tuple1+(1,2,3,4,5))


#9.Write program to Add , subtract, multiply, divide 2 complex numbers.
a=2+2j
b=4+4j
print ("Addition of two complex numbers :",a+b)
print ("Subtraction of two complex numbers :",a-b)
print ("Multiplication of two complex numbers :",a*b)
print ("Division of two complex numbers :",a/b)


#10.Using assignment operators, perform following operations Addition, Substation, Multiplication, Division, Modulus, Exponent and Floor division operations

a=4.5
b=7.2
Add=a+b
Sub=b-a
Mul=a*b
Div=b/a
Mod=a%b
exp=a**b
floordiv=b//a
print ("addition is: \n",Add)
print ("subtraction is: \n",Sub)
print ("multiplication is: \n",Mul)
print ("division is: \n",Div)
print ("modulus is: \n",Mod)
print ("Exponent is: \n",exp)
print ("floor division is \n",floordiv)


#11.Read 2 numbers to variable a and b and perform all bitwise operations on that numbers.
a = 30            
b = 50             
c = a & b;       
print ("Value of (a&b) is:",c)
c = a | b;         
print ("Value of (a|b) is:",c)
c = a ^ b;        
print ("Value of (a^b) is:",c)
c = ~a;           
print ("Value of (~a) is:",c)
c = a << 2;       
print ("Value of (a<<2) is:",c)
c = a >> 2;       
print ("Value of (a>>2) is:",c)


#12.Read 10 numbers from user and find the average of all. 
#a) Use comparison operator to check how many numbers are less than average and print them 
#b) Check how many numbers are more than average. 
#c) How many are equal to average.
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
d=int(input("Enter a number: "))
e=int(input("Enter a number: "))
f=int(input("Enter a number: "))
g=int(input("Enter a number: "))
h=int(input("Enter a number: "))
i=int(input("Enter a number:"))
j=int(input("Enter a number: "))

avg=(a+b+c+d+e+f+g+h+i+j)/10
countBig=0
countSmall=0
countEqual=0
print ("Average of the 10 nos is: ",avg)
print ("Numbers smaller than the Average are : ")
if a<avg:
    print ("a=",a)
    countSmall+=1
elif a>avg:
    countBig+=1
else:
    countEqual+=1
    
if b<avg:
    print ("b=",b)
    countSmall+=1
elif b>avg:
    countBig+=1
else:
    countEqual+=1
    
if c<avg:
    print ("c=",c)
    countSmall+=1
elif c>avg:
    countBig+=1
else:
    countEqual+=1
    
if d<avg:
    print ("d=",d)
    countSmall+=1
elif d>avg:
    countBig+=1
else:
    countEqual+=1
    
if e<avg:
    print ("e=",e)
    countSmall+=1
elif e>avg:
    countBig+=1
else:
    countEqual+=1
    
if f<avg:
    print ("f=",f)
    countSmall+=1
elif f>avg:
    countBig+=1
else:
    countEqual+=1
    
if g<avg:
    print ("g=",g)
    countSmall+=1
elif g>avg:
    countBig+=1
else:
    countEqual+=1
    
if h<avg:
    print ("h=",h)
    countSmall+=1
elif h>avg:
    countBig+=1
else:
    countEqual+=1
    
if i<avg:
    print ("i=",i)
    countSmall+=1
elif i>avg:
    countBig+=1
else:
    countEqual+=1
    
if j<avg:
    print ("j=",j)
    countSmall+=1
elif j>avg:
    countBig+=1
else:
    countEqual+=1    
print("the Total count of nos bigger than average is: ",countBig)
print("the total count of nos smaller than average is: ",countSmall)
print("the total count of nos equal to the average is: ",countEqual)


#13.Write a program to find the biggest of 4 numbers. 
#a) Read 4 numbers from user using Input statement. 
#b) extend the above program to find the biggest of 5 numbers. ( PS : Use IF and IF & Else , If and ELIf, and Nested IF )
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
d=int(input("Enter the number:"))
greatest=0
if (a>b)&(a>c)&(a>d):
    print("The greatest no of the first 4 is: ",a)
    greatest=a
elif (b>a)&(b>c)&(b>d):
    print("The greatest no of the first 4 is: ",b)
    greatest=b
elif (c>a)&(c>b)&(c>d):
    print("The greatest no of the first 4 is: ",c)
    greatest=c
else:
    print("the greatest no of the first 4 is: ",d)
    greatest=d

e=int(input("Enter 5th number: "))

if(e>greatest):
    print("The biggest of all 5 nos is: ",e)
    
    
#14.Write a program to create two list A and B such that List A contains Employee Id, List B contains Employee name ( minimum 10 entries in each list ) and perform following operations 

#a) Print all names on to screen 
listEId=[1,2,3,4,5,6,7,8,9,10]
listEName=['Ramesh','Rajesh','John','Guldeep','Kavitha','Sughail','Immanvel','Tapish','Juli','Naser']
print (listEName)

#b) Read the index from the user and print the corresponding name from both list. 
index=int(input("Enter the index to read from: "))
print (listEName[index])
print (listEId[index])

#c) Print the names from 4th position to 9th position 
print (listEName[3:-1])

#d) Print all names from 3rd position till end of the list d) Print all names from 3rd position till end of the list 
print (listEName[2:])

#e) Repeat list elements by specified number of times ( N- times, where N is entered by user) 
ntime=int(input("Enter the no of times you wish to repeat the list: "))
print (listEId*ntime)
print (listEName*ntime)

#f) Concatenate two lists and print the output. 
concatList=listEId+listEName
print (concatList)

#g) Print element of list A and B side by side.( i.e. List-A First element , List-B First element )
for element in range(len(listEId)):
  print ("ListEmpid element:",listEId[element],"and ListEmpName elements: ",listEName[element])
  
 #15.Create a list of 5 names and check given name exist in the List.

#a) Use membership operator ( IN ) to check the presence of an element. 
list1=['John','Kavitha','Tapish','Juli','Naser']

if ('Juli') in list1:
  print("Juli is present in the list")
else:
  print("Juli is not present in the list")

#b) Perform above task without using membership operator. 
for i in list1:
  if (i=='John'):
    print("John is present in the list")
    break
else:
    print("John is not present in the list")

#c) Print the elements of the list in reverse direction.
list1.reverse()
print("the elements of list1 in reverse direction are: ",list1)


# 16.Write program to perform following:
#i) Check whether given number is prime or not.

num=int(input("Enter the number to check for prime: "))
if num==1:
  print ("Number",num,"is not a prime number")
elif num>1:
  for i in range(2,num):
    if num%i==0:
      print ("Number",num," is not a prime number")
      break
  else:
    print ("Number",num,"is a prime number")
    
#ii) Generate all the prime numbers between 1 to N where N is given number.
upper=int(input("Enter the no till which you need to print the prime numbers: "))
print ("The prime numbers between the given range is: ")
for num in range(2,upper+1):
  if num>1:
    for i in range(2,num):
      if(num%i)==0:
        break
    else:
      print (num)

''''17.Write program to find the biggest and Smallest of N numbers. 
PS: Use the functions to find biggest and smallest numbers.'''
num=list(input("Enters the numbers: "))
biggest=max(num)
smallest=min(num)
print ("Maximum is",biggest)
print ("Minimum is",smallest)


'''18.Using loop structures print numbers from 1 to 100. and using the same loop print numbers from 100 to 1.( reverse printing) 
a) By using For loop 
b) By using while loop 
c) Let mystring ="Hello world" print each character of mystring in to separate line using appropriate loop structure.'''
print ("Printing 1 to 100 using for loop")
list1=[]
for i in range(1,101):
  print(i)
  list1.append(i)
list1.reverse()
print ("\nNumbers 1 to 100 in reverse order using the same for loop",list1)

list2=[]
i=1
print ("\nPrinting 1 to 100 using while loop")
while i<=100:
  print(i)
  list2.append(i)
  i+=1
list2.reverse()
print("\nNumbers 1 to 100 in reverse order using the same while loop",list2)

mystring='Hello world'
print ("\nPrinting each character of string Hello world in separate line")
for j in mystring:
  print (j)
  
  
  '''19.Using loop structures print even numbers between 1 to 100. 
a) By using For loop , use continue/ break/ pass statement to skip odd numbers.
i) break the loop if the value is 50 
ii) Use continue for the values 10,20,30,40,50

b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
i) break the loop if the value is 90 
ii) Use continue for the values 60,70,80,90'''

#Using for loop structure to print even numbers between 1 to 100
print("The even numbers from 1 to 100 using for loop is below: " )
for i in range(1,101):
  if i%2==0:
    print (i)
print("\n\n")


#.a) By using For loop , use continue/ break/ pass statement to skip odd numbers.
print("The numbers from 1 to 100 skipping odd numbers using for loop is below: " )
for i in range (1,101):
  if i%2!=0:
    continue
  print (i)
print ("\n\n")


#.i) break the loop if the value is 50 
print("Breaking the for loop i ==50")
for i in range(1,101):
    if i==50:
      break
    print (i)
print ("\n\n")  


#.ii) Use continue for the values 10,20,30,40,50
print("using continue for the values 10,20,30,40,50") 
for i in range (1,101):
  if i==10 or i==20 or i==30 or i==40 or i==50:
    continue
  print (i)
print ("\n")    



#Using while loop structure to print even numbers between 1 to 100
print("The even numbers from 1 to 100 using while loop is below: ") 
i=1
while i<=100:
  if i%2==0:
    print(i)
  i+=1
print("\n\n")


#.a) By using while loop , use continue/ break/ pass statement to skip odd numbers.
print("The numbers from 1 to 100 skipping odd numbers using while loop is below:") 
i=1
while i<=100:
  if i%2!=0:
    i+=1
    continue
  print(i)
  i+=1
print("\n\n")


#.i) break the loop if the value is 50 
print("Breaking the for loop i ==50")
i=1
while i<=100:
  if i==50:
    break
  print(i)
  i=i+1    


#.ii) Use continue for the values 10,20,30,40,50
print("using continue for the values 10,20,30,40,50")
i=1
while i<=100:
  if i==10 or i==20 or i==30 or i==40 or i==50:
    i=i+1
    continue
  print(i)
  i=i+1
print("\n")
  

'''20.Write a program to generate Fibonacci series of numbers. Starting numbers are 0 and 1, new number in the series is generated by adding previous two numbers in the series. Example : 0, 1, 1, 2, 3, 5, 8,13,21,..... a) Number of elements printed in the series should be N numbers, Where N is any +ve integer. b) Generate the series until the element in the series is less than Max number.'''
nterms=int(input("Enter the no of terms: "))
a=0 
b=1
if nterms<=0:
  print("Please enter positive number:")
elif nterms==1:
  print("Fibonacci series: ",a)
elif nterms==2:
  print (a)
  print (b)
else:
  print (a)
  print (b)
  while(nterms>2):
    numnext=a+b
    print (numnext)
    a=b
    b=numnext
    nterms=nterms-1