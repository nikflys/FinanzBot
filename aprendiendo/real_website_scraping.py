from bs4 import BeautifulSoup
import requests

#usamos timesjobs, pagina la cual es para buscar trabajos
#usamos requests para descargar el html de la pagina

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=")

#print(html_text) #si el codigo q devuelve es 200, significa que la pagina se descargo correctamente

soup = BeautifulSoup(html_text.text, "lxml") #lxml es un parser más rápido. parser es el analizador sintáctico
# soup es el objeto BeautifulSoup que contiene el árbol de análisis del HTML

job = soup.find("li", class_="clearfix job-bx wht-shd-bx") 

#print(job) #imprime el primer trabajo que encuentra
company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ","") #con esto dentro de job, extraigo el nombre de la empresa
skills = job.find("div", class_="srp-skills").text.replace(" ","") #con esto dentro de job, extraigo las habilidades requeridas
print(company_name) #imprime el nombre de la empresa

experience = job.find("li", class_="srp-icons experience").text.replace(" ","") #con esto dentro de job, extraigo la experiencia requerida

print(experience)




