"""def show(a):
    print("hii")
    return a * 3

print(f"bye {2*3+5} ok")
print(f"bye {show(5)} ok")"""

"""def show(a):
    return a,a+5,23  
a,b,c=show(7)  #
print(a,b,c)"""

"""def show():
   print("show funcation") #show funcation
s=show
res=s
show()
s()
res()   """

"""s=lambda :print("hii")
res=s        # lambda is a Nameless d=funcation
s()
res() """

# Lambda funcation| single line funcation
#syntax
"""lambda paramiter:exeprsion"""
"""def square(x):
   return x*x
res =square(3)# with out funcation
print(res)
"""
#with funcation
"""res = lambda x:x*x  #multiplication
print(res(3))"""
"""res =lambda no1,no2:no1+no2  #Addition
print(res(4,5))"""
"""res =lambda p,r,t:p*r*t/100
print(res(50,40,30))""" #simple intrest
res =lambda p,r,t:p*r*t/100
print("enter p,r and t")
print(res(int(input())))