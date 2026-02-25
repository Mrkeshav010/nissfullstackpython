print("enter two number")
num1= int(input())
num2= int(input())
print("enter your choice\n1.add\2sub\3mult")
ch= int(input())
if ch==1:
	print("sum=",num1+num2)

elif ch==2:
	print("sub=",num1-num2)
elif ch==3:
	print("mult=",num1*num2)

else:
	print("not valid")