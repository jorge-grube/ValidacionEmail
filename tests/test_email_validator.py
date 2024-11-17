import unittest
from emails.validator import EmailValidator

class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        # Inicializa una instancia del validador antes de cada prueba
        self.validator = EmailValidator()

    def test_valid_email(self):
        # Caso: correo válido
        self.assertTrue(self.validator.validar("test@example.com"))

    def test_invalid_email_no_at(self):
        # Caso: correo sin "@" no es válido
        self.assertFalse(self.validator.validar("testexample.com"))

    def test_invalid_email_no_domain(self):
        # Caso: correo sin dominio no es válido
        self.assertFalse(self.validator.validar("test@.com"))

    def test_invalid_email_special_characters(self):
        # Caso: correo con caracteres especiales inválidos
        self.assertFalse(self.validator.validar("test@@example.com"))

    def test_invalid_email_empty_string(self):
        # Caso: cadena vacía no es válida
        self.assertFalse(self.validator.validar(""))

    def test_non_string_input(self):
        # Caso: entrada no es string (debe lanzar excepción)
        with self.assertRaises(TypeError):
            self.validator.validar(12345)

    def test_valid_email_with_subdomain(self):
        # Caso: correo con subdominio válido
        self.assertTrue(self.validator.validar("test@mail.example.com"))

    def test_valid_email_with_dash(self):
        # Caso: correo válido con guión
        self.assertTrue(self.validator.validar("test-user@example.com"))

if __name__ == "__main__":
    unittest.main()
