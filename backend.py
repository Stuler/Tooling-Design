from os import makedirs

class Folder:
    '''Creates main directory and all the subdirectories'''
    def __init__(self):
        self.toolsList = [
            "Stahovaci krouzky", 
            "Chytaky", 
            "Vodici pouzdra", 
            "Navadeci krouzky", 
            "Drzaky chytaku",
            "Sroubove cepy",
            "Trny",
            "Pruziny",
        ]

    def createWrkDir(self,path):
        self.path = path
        for i in self.toolsList:
            makedirs(self.path + "\\" + i)
        # ! Zapracovat algoritmus pre uz existujuci priecinok
