from Wrappers.iter_warp import iter_wrap as iw
from Wrappers.flair_wrapper_lar import flair_wrap as fw
import json
from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider
import argparse
from cryptography.fernet import Fernet
import regex as re

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--text", type=str, help="Please input the text you want its contained piis to be detected and encrypted.")
args = parser.parse_args()
input_text = args.text

key = open('./.gitignore/.encry_env', 'r').read()
cipher_suite = Fernet(key)

configuration = {
    "nlp_engine_name": "spacy",
    "models": [
        {"lang_code": "de", "model_name": "de_core_news_lg"},
    ],
}

provider = NlpEngineProvider(nlp_configuration=configuration)
nlp_engine_with_german = provider.create_engine()
analyzer = AnalyzerEngine(
    nlp_engine=nlp_engine_with_german, supported_languages=["de"]
)
def presi_flair_encryption(input_text, filename):
    fw_i = fw(input_text)['keys']
    results = analyzer.analyze(
        text=input_text,
        entities=[],  # Leave empty to detect all entities
        language="de"  # Language of the text
        )
    pii_list = [input_text[result.start:result.end] for result in results]
    pii_list += fw_i
    pii_list = [word for s in pii_list for word in s.split()]
    hash_list = [cipher_suite.encrypt(x.encode())  for x in pii_list]
    pii_hash_dict = {pii_list[num]: hash_list[num] for num in range(len(pii_list))}

    decoded_dict = {key: value.decode('utf-8') for key, value in pii_hash_dict.items()}
    with open(f'./.HashPairs/Gendered/test_{filename}.json', 'w') as f:
        json.dump(decoded_dict, f)
        f.close()
    output_text = input_text

    for pii, hash in decoded_dict.items():
        a = pii
        b = hash.__str__()
        output_text = re.sub(re.escape(a), b, output_text)
    return(output_text)
