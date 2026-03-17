import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import load_pem_private_key


def load_private_key(path):

    with open(path, "rb") as f:
        return load_pem_private_key(f.read(), password=None)


def sign_packet(private_key, payload: bytes):

    signature = private_key.sign(
        payload,
        ec.ECDSA(hashes.SHA256())
    )

    return base64.b64encode(signature).decode()