from presi_flair_decode import pii_hash_decrypt
from presi_flair_encode import presi_flair_encryption


text = """

Das ist ein Beispiel Text. Keine Ahnung.
Name ist irgendwas mit Bernd. Bernd Schmidt.

"""

a = presi_flair_encryption(text)
print(a)
b = pii_hash_decrypt(a)
print(b)