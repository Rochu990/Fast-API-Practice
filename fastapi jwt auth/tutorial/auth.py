from pathlib import Path
from cryptography.x509 import load_pem_x509_certificate
import jwt


def decode_and_validate_token(acces_token):
    unverified_headers = jwt.get_unverified_headers(acces_token)
    public_key = load_pem_x509_certificate(
        (Path(__file__).parent / 'public_key.pem').read_text()
    ).public_key()
    return jwt.decode(
        acces_token,
        key=public_key,
        algorithms=unverified_headers["alg"],
        audience="http://127.0.0.1:8000/todo"
    )