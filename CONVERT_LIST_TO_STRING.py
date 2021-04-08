#CONVERT LIST INTO STRING
def ListToString(LIST):
    s=""
    for item in LIST:
        s+=item
        s+=" "
    return s
L=["MANJEET","SINGH","SALAL"]
print(ListToString(L))