from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('./.gitignore/.encry_env', 'wb') as f:
    f.write(key)
    f.close()