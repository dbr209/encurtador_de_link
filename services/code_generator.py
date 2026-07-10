import string
import secrets
from database.repository import url_exist

CHARS = string.ascii_letters + string.digits

def gerar_code(size=6):
    while True:
        code = "".join(secrets.choice(CHARS) for _ in range(size))

        if not url_exist(code):
            return code