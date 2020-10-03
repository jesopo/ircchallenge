from base64  import b64decode, b64encode
from hashlib import sha1
from typing  import Optional

from cryptography.hazmat.backends   import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

def _read_key(keyfile: str):
    with open(keyfile, "r") as f:
        return f.read()
def _load_key(
        key:      str,
        password: Optional[str]
        ) -> rsa.RSAPrivateKey:
    password_b: Optional[bytes] = None
    if password is not None:
        password_b = password.encode("utf8")

    return serialization.load_pem_private_key(
        key.encode("utf8"),
        password=password_b,
        backend=default_backend()
    )
def _compute(
        ciphertext: bytes,
        key:        rsa.RSAPrivateKey,
        ) -> str:

    plain = key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )

    return b64encode(sha1(plain).digest()).decode("ascii")

class Challenge(object):
    def __init__(self,
            key:      Optional[str] = None,
            keyfile:  Optional[str] = None,
            password: Optional[str] = None):
        if key is None:
            if keyfile is not None:
                key = _read_key(keyfile)
            else:
                raise ValueError("must provide either 'key' or 'keyfile'")
        self._key = _load_key(key, password)
        self._buf = ""

    def push(self, data: str):
        self._buf += data

    def finalise(self):
        buf = b64decode(self._buf)
        self._buf = ""
        return _compute(buf, self._key)
