from bs4 import BeautifulSoup

with open("aprendiendo\\basics_web_scraping\\example.html", "r", encoding="utf-8") as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, "lxml") #lxml es un parser más rápido. parser es el analizador sintáctico
    # soup es el objeto BeautifulSoup que contiene el árbol de análisis del HTML
    # .text extrae solo el texto, sin las etiquetas HTML
    courses_cards = soup.find_all("div", class_="card") #find_all encuentra todas las coincidencias, find solo la primera. class_ es porque class es una palabra reservada en Python
    for course in courses_cards:
        course_name = course.h5.text #h5 es la etiqueta HTML que contiene el nombre del curso
        course_price = course.a.text.split()[-1] #a es la etiqueta HTML que contiene el precio del curso. split()[-1] toma el último elemento después de dividir el texto por espacios
        print(f"Curso: {course_name}, Precio: {course_price}")
        
    




