from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def obtener_clima(driver, consulta):
    try:
        # Buscar clima en Google usando la consulta completa
        driver.get(f"https://www.google.com/search?q={consulta}")
        

        # Obtener temperatura
        temperatura = driver.find_element(By.CSS_SELECTOR, "span#wob_tm").text
        
        # Obtener condición climática
        condicion = driver.find_element(By.CSS_SELECTOR, "span#wob_dc").text
        
        # Obtener ubicación
        ubicacion = driver.find_element(By.CSS_SELECTOR, "div#wob_loc").text
        
        return f"El {consulta} es: {temperatura}°C, {condicion}"
        
    except Exception as e:
        return f"No se pudo obtener el clima para la consulta: '{consulta}' en este momento."