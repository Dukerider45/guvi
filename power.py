def func(du,ke):
    if(ke==1):
        return(du)
    if(ke!=1):
        return(du*func(du,ke-1))
du=int(input())
ke=int(input())
print(func(du,ke))
