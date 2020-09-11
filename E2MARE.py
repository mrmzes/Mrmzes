import requests
import os
import sys
from bs4 import BeautifulSoup as bs
import webbrowser

# Miguel Angel Ramirez Espinosa
try: 
    import webbrowser
except ImportError: 
    os.system('pip install webbrowser')
    print('Installing webbrowser...') 
    print('Ejecuta de nuevo tu script...') 
    exit() 

# Lo que hace el codigo, en primera te da un rango con un inicio y fin en el cual
# busca las siglas de la facultad asignada, si el rango de inicio es mayor que el del fin
# el codigo te invierte el orden para que este de menor a mayor, luego busca la facultad
# asignada en la pagina de las noticias de la UANL, luego por experiencia personal, usa
# lo del html.parser y href para que al momento de abrir la pagina todo se abra bien
print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
    