from datetime import datetime
import requests #Esta librería nos permite realizar peticiones a la web
import lxml.html as html #Esta librería nos permite convertir el código html en formato,
#texto a un archivo especial para poder usar las expresiones XPATH
import os, datetime


#Guardamos la URL de la web a scrappear en una constante. 
HOME_URL = 'https://www.larepublica.co'

#Guardamos las expresiones XPATH en constantes que usaremos después.
XPATH_LINK_TO_ARTICLE = '//h2/a/@href'
XPATH_TITLE = '//div[@class="mb-auto"]/h2/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_AUTHOR = '//div[@class="author-article"]/div/button/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'

#La siguiente función se encargará de extraer todos los links de las noticias de la
#página principal 

def parse_home():

    try:
        response = requests.get(HOME_URL)
        print(response.status_code)
        if response.status_code == 200:
            home = response.content.decode('utf8')
            parsed = html.fromstring(home)
            #extraemos los links
            links_noticias = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(links_noticias)

        else:
            raise ValueError(f'Error: {response.status_code}') 

    except ValueError as error:
        print(error)

def run():
    parse_home()

if __name__ == '__main__':
    run()


    


    