from datetime import datetime
from urllib import response
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
            today = datetime.date.today().strftime('%d-%m-%y')
            if not os.path.isdir(today):
                os.mkdir(today)
            home = response.content.decode('utf8')
            parsed = html.fromstring(home)
            #extraemos los links
            links_noticias = ['https://www.larepublica.co/economia/desempleo-en-abril-se-redujo-a-11-2-esto-significo-2-7-millones-de-desocupados-3373910', 
            'https://www.larepublica.co/finanzas/los-factores-que-llevan-a-que-el-dolar-vuelva-a-niveles-de-3-800-despues-de-elecciones-3373708', 
            'https://www.larepublica.co/especiales/opa-por-nutresa/opa-por-grupo-argos-esta-10-1-sobre-el-precio-objetivo-de-los-analistas-de-15-027-3373693']#parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(links_noticias)
            print()
            for link in links_noticias:
                print(link)
                print()
                parse_notice(link, today)

        else:
            raise ValueError(f'Error: {response.status_code}') 

    except ValueError as error:
        print(error)

#La siguiente función extraerá la noticia completa de cada link de la página principal y 
#la grabaremos en un archivo de texto. 

def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                print(title)
                title = title.replace('\"','') #Esto elimina las dobles comillas que pueda haber en el texto
                print(title)
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                print(summary)
                body = parsed.xpath(XPATH_BODY)
                print(body)
                author = parsed.xpath(XPATH_AUTHOR)
                print(author)

            except IndexError:
                return

            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as file:
                file.write(title)
                file.write('\n\n')
                file.write(summary)
                file.write('\n\n')
                file.write(author)
                file.write('\n\n')
                
                for p in body:
                    file.write(p)
                    file.write('\n')

        else:
            raise ValueError(f'Error: {response.status_code}')

    except ValueError as ve:
        print(ve)        


def run():
    parse_home()

if __name__ == '__main__':
    run()


    


    