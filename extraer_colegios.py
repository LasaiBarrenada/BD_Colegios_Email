# -*- coding: utf-8 -*-
"""
Codigo para la union de los correos electronicos disponibles en buscocolegio.com con el listado
de colegios en el registro estatal. 
Autor: Lasai Barreñada Taleb 
"""
import urllib
import pandas as pd
import requests
from bs4 import BeautifulSoup


# =============================================================================
# 1. Descarga los datos de los colegios de la web estatal
# =============================================================================
listado = pd.read_excel('Listado.xls')
listado['email'] = 0

# =============================================================================
# 2. Para cada codigo de centro educativo se consulta la web de buscocolegio 
#    y se añade el correspondiente e-mail siempre que este disponible 
#    La ejecucion de este proceso es lenta debido a la gran cantidad de centros 
# =============================================================================
for i,codigo in enumerate(listado['Código']):
    try:
        URL = 'https://www.buscocolegio.com/Colegio/detalles-colegio.action?id=' + str(codigo)
        page = requests.get(URL)
    
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(itemprop="email")
        if type(results) == type(None):
            listado['email'].iloc[i] = 'No disponible'
        else:
            
            listado['email'].iloc[i] = results.find('strong').text
    except Exception as e:
        listado['email'].iloc[i] = e
        print(e)
# =============================================================================
# 3. Se guarda el archivo resultante en el formato deseado
# =============================================================================
listado.to_excel('listado_emails.xlsx', index = False) #Excel
listado.to_csv('listado_emails.xlsx', index = False) #CSV separado por comas

