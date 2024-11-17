import re
import logging
import os


# Obtener la ruta absoluta del archivo de logs
current_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(current_dir, '../logs/email_validator.log')

# Configuración de logging
logging.basicConfig(
    filename=log_path,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class EmailValidator:
    def __init__(self):
        # Expresión regular para validar correos electrónicos
        self.regex = re.compile(r'([A-Za-z0-9]+[._-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


    def validar(self, correo: str):
        try:
            # Verifica que la entrada sea un string
            if not isinstance(correo, str):
                raise TypeError("El correo debe ser un string")

            # Devuelve True si el correo es válido, False en caso contrario
            if re.fullmatch(self.regex, correo):
                return True
            else:
                return False

        except Exception as e:
            # Registra errores en el archivo de logs
            logging.error(f"Error al validar el correo: {correo}. Error: {str(e)}")
            raise
