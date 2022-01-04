from dataAccess import csv
import pandas as pd
class Animals(csv):
    def __init__(self,name,age,gender,problem):
        self.name=name
        self.age=age
        self.gender=gender
        self.problem=problem
        
    def addAnimals(self,arg):
        self.addAnimals_csv(arg)
    def oku(self):
    
        liste=self.read()
        return liste

    def find(self,a):
        self.a =a 
        
        liste=self.read()
        for i in range(len(liste[0])): 
            if self.a == liste[0][i]:
                return(liste[0][i],liste[1][i],liste[2][i],liste[3][i])
        
        
    def deleteAnimal(self,a):
        self.a=a
        liste=self.read()
        
        for i in range(len(liste[0])):
            if self.a == liste[0][i]:
                new=pd.DataFrame(liste)
                new.drop(new.columns[[i]], axis=1, inplace=True)
                liste=new.values.tolist()           
                break # w ? 
        with open("C:\\python36\\Lib\\site-packages\\PyQt5\\project\\data.csv","w",encoding = "utf-8") as file:
            for i in range(len(liste[0])):
                s=liste[0][i]+","+liste[1][i]+","+liste[2][i]+","+liste[3][i]
                file.writelines(s)
                
        