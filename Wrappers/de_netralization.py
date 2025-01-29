from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def gender_text(text):
    completion = client.chat.completions.create(
            model="gemma-2-2b-it",
            messages=[
                {"role": "system", "content": (f"Please add gender-specific pronouns to the text, given the context:{text}"
                                               "If you find any placeholder, add the probable name given the context"
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