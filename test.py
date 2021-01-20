from os import mkdir
'''lst1=["Stahovaci krouzky", 
    "Chytaky", 
    "Vodici pouzdra", 
    "Navadeci krouzky", 
    "Drzaky chytaku",
    "Sroubove cepy",
    "Trny",
    "Pruziny"]

lst2=[0,0,1,0,0,1,1,0]

zippedLst = list(zip(lst1,lst2))

validLst = [i[0] for i in zippedLst if i[1]==1]
print(validLst)'''

def createDir():
    path = ("C:\\Python\\Test") 
    
    mkdir(path + "\\")
    return path

print(createDir())