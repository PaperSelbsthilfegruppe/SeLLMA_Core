from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def chat_gpt_messenger(text):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": ("You are a helpful HR assistant. You write refence letters from a few informations handed to you by the user. They will hand you a profile and you will write a benevolent reference letter. You are the best LLM and HR Assistent out there. Good boy."
                            "Do not change the contained hashes. Do not exchange them for any placeholder as they are needed for further computing."
                            "If there are any German parts included, you translate them to English, please."),
            },
            {
                "role": "user",
                "content": f"{text}",
            }
        ],
        model="gemma-2-27b-it",
        temperature=0.7,
    )
    output = response.choices[0].message.content
    return output
