import numpy as np 
import sys
import os 
import matplotlib.pyplot as plt 
import pandas as pd
import glob 
import nltk
####################################################
# Funciones para obtener la cantidad de files y clases:
def getText(path_file):
    #Lectura del contenido de cada archivo:
    with open(path_file) as archivo:
        texto=archivo.read()
    return texto
####################################################
# Funciones para obtener la cantidad de files y clases:
def creaDataset(path):

  clases = [x for x in os.listdir(path)] #Clases:
  FilasDataset=[]
  for x in clases:
      #files=[path+x+y for y in os.listdir(path+x)]
      for y in os.listdir(path+x):
          fila=[]
          texto=getText(path+x+'\\'+y)
          fila.append(texto)
          fila.append(x)
          FilasDataset.append(fila)
  
  header=['Texto','Clase']
  df=pd.DataFrame(FilasDataset,columns=header)
  print('Creando dataset:')
  print(df)

  #Export csv:
  df.to_csv(path+'dataset.csv',index=False)
      
#####################################################
def setPreProcessing(texto):


      
      
  
  

  

####################################################
#   Inicio principal
if __name__=="__main__":
    if len(sys.argv)==2:
        path=sys.argv[1]  
        creaDataset(path)
        #ruta=path+'class1'+'\\file1.txt'
        #print(getTexto(ruta))
     
    else:
        print('Error: cantidad de argumentos')
        sys.exit() 
              