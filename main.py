from utils.sanitizar import sanitizar
from selenium import webdriver
from funciones_agentes.obtener_precio_accion import obtener_precio_accion
from funciones_agentes.obtener_clima import obtener_clima
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configuración de Selenium
options = Options()
options.add_argument("--headless=new") # Comentado para ver el navegador y reducir detección
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# User agent más reciente
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
options.add_argument('--disable-blink-features=AutomationControlled')

# Opciones experimentales para ocultar automatización
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Inicialización del driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver = webdriver.Chrome(options=options)

def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return obtener_precio_accion
    return None

palabras_salida = ['salir', 'exit', 'quit', 'terminar', 'finalizar']

print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")
while True:
    user_input = sanitizar(input("---> "))
    
    if any(palabra in user_input.lower() for palabra in palabras_salida):
        print("¡Gracias por usar el programa!")
        break

    funcion_agente = procesar_input(user_input)
    if funcion_agente is None:
        print("No entendí tu solicitud. Intenta nuevamente.")
    else:
        respuesta = funcion_agente(driver, user_input)
        print(f">>> {respuesta}")