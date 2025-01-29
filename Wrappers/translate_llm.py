from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def translate_llm(text):
    completion = client.chat.completions.create(
            model="gemma-2-2b-it",
            messages=[
                {"role": "system", "content": (f"Translate the following German text to English:{text}"
                                               "Do not add anything."
                                               "Do not remove anything."
                                               "Do not add any commentary."
                                               "Do not change the contained hashes."
                                               "Leave the contained hashes intact."
                                               "Make no changes to the document aside the translation.")},
                {"role": "user", "content": ""}
            ],
            temperature=0.7,
        )
    output = completion.choices[0].message.content
    return output