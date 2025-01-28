#!pip3 install presidio_analyzer presidio_anonymizer
#!python3 -m spacy download de_core_news_lg

from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine, DeanonymizeEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider
from presidio_anonymizer.entities import RecognizerResult, OperatorResult, OperatorConfig
from presidio_anonymizer.operators import Decrypt
import json

# Configuration
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

def presidio_wrapper(input_text, crypto_key = "WmZq4t7w!z%C&F)J"):

    results = analyzer.analyze(text=input_text, language="de")
    ano = AnonymizerEngine()
    anonymized_text = ano.anonymize(text=input_text, analyzer_results = results)
    operators={}
    for i in anonymized_text.items:
        if i.entity_type in operators.keys():
            continue
        else:
            operators[i.entity_type] = OperatorConfig("encrypt", {"key": crypto_key})
    engine = AnonymizerEngine()
    anonymize_result = engine.anonymize(
        text=input_text,
        analyzer_results=results,
        operators=operators,
    )
    anon_results = json.loads(anonymize_result.to_json())
    anon_results['detector'] = results
    return anon_results