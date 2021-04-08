def counting(string1):
    counts=0
    for i in string1:
        if (i=='s'):
            counts+=1
    return(counts)
string1=input("\nENTER YOYR STRING HERE...")
print(counting(string1))