from gliner import GLiNER

def pii_list(text, labels=["work", "booking number", "personally identifiable information", "driver licence", "person", "book", "full address", "company", "actor", "character", "email", "passport number", "Social Security Number", "phone number"]):
    model = GLiNER.from_pretrained("vicgalle/gliner-small-pii")
    entities = model.predict_entities(text, labels)
    piis = [entity['text'] for entity in entities]
    return piis
