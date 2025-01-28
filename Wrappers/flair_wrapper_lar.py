from flair.data import Sentence
from flair.nn import Classifier

def flair_wrap(text, ner_classifier = 'de-ner-large'):
    sentence = Sentence(text)
    tagger= Classifier.load(ner_classifier)
    tagger.predict(sentence)
    #sentence.get_labels() Useless?
    #sentence.get_spans('ner') Useless?
    dic = sentence.to_dict()
    handler = {}
    for i in dic['entities']:
        handler[i['text']] = list(i['labels'][0].values())[0]
    keys = list(handler.keys())
    values = list(handler.values())
    test = {}
    test['dict'] = handler
    test['keys'] = keys
    test['values'] = values
    return test