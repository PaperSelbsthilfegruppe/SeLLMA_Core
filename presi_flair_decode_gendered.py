import json
import argparse
from cryptography.fernet import Fernet
import regex as re

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--text", type=str, help="Please input the text you want its contained piis to be detected and encrypted.")
args = parser.parse_args()
input_text = args.text

def pii_hash_decrypt(input_text, filename):
    with open(f'./.HashPairs/Gendered/test_{filename}.json', 'r') as file:
        data = json.load(file)
    output_text=input_text
    for pii, hash in data.items():
        a = pii
        b = hash.__str__()
        output_text = re.sub(b, re.escape(a), output_text)
    return(output_text)

