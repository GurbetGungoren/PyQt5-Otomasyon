import csv
import pandas as pd
class csv:
    pass 
    def addAnimals_csv(self,a):
        with open("C:\\python36\\Lib\\site-packages\\PyQt5\\project\\data.csv","a",encoding = "utf-8") as file:
            s = a.name +","+a.age + "," +a.gender+ ","+a.problem+"\n"
            file.writelines(s)
    def read(self):
        name_liste=[] #boş listeler oluşturdum.
        age_liste=[]
        gender_liste=[]
        problem_liste=[] #klasor !
        with open("C:\\python36\\Lib\\site-packages\\PyQt5\\project\\data.csv","r",encoding="utf-8") as file:
            for satir in file:
                row = satir.split(',')
                name_liste.append(row[0])
                age_liste.append(row[1])
                gender_liste.append(row[2])
                problem_liste.append(row[3])

        return (name_liste,age_liste,gender_liste,problem_liste)