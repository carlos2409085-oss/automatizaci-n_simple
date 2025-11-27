from unidecode import unidecode    
import unicodedata
def sanitizar(text):
    
    # Convertir a minúsculas
    text = text.lower()
    
    # Normalizar y eliminar tildes
    text = unicodedata.normalize('NFKD', text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    
    # Eliminar caracteres especiales, mantener solo letras, números y espacios
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    
    return text
