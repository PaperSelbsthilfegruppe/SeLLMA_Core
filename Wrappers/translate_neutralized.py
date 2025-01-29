import requests

def process_neutralized_translations(text, config):
    """
    Übersetzt neutralisierte Texte erneut.
    
    Argumente:
    - text (str): Der neutralisierte Text.
    - config (dict): API-Parameter für das Übersetzungsmodell.
    
    Rückgabe:
    - str: Der übersetzte Text.
    """
    
    prompt = f"Translate the following neutralized text into natural English:\n\n{text}"
    
    try:
        payload = {
            "model": config["model_name"],
            "messages": [{"role": "user", "content": prompt}],
            "temperature": config["temperature"],
            "max_tokens": config["max_tokens"],
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(config["llm_endpoint"], json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    
    except requests.RequestException as e:
        raise ValueError(f"Fehler bei der Übersetzung von neutralisierten Texten: {e}")
