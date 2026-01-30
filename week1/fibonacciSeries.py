print("fibonacci series")
def febnocci_series(n):
    a,b=0,1   
    while a<n:
        print(a,end=" ")       
        a,b=b,a+b
   # print()
febnocci_series(1000)    