print("My Calculator application")
a,b=map(int,input("Please enter only two numbers:").split()) #getting input values
ch=input("Enter your operation choice(+,-,*,/,%,//):").strip()  #enter your arithmetic choice within the list
result=0
if ch=="+":     #add
    result=a+b
    print("The answer is",result)

elif ch=="-":    #subtract    
    result=a-b
    print("The answer is",result)

elif ch=="*":  #multiply
    result=a*b
    print("The answer is",result)

elif ch=="/":  #divide
    try:
        result=a/b
    except ZeroDivisionError:
        print("Try to enter different value")
    else:
       print("The answer is","{:.2f}".format(result))

elif ch=="//":   #floor division
    try:
       result=a//b
    except ZeroDivisionError:
        print("Try to enter different value")
    else:
        print("The answer is",result)

elif ch=="%":    #reminder
    try:
      result=a%b
    except ZeroDivisionError:
        print("Try to enter different value")
    else:
       print("The answer is",result)

else:
    print("Next time please enter the operator listed above")

print("THANK YOU FOR USING ME!!")