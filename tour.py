ab=int(input())
print("0" if ab>0 and (ab & (ab-1))==0 else "1")
