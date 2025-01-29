from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def write_letter(llm_model, systemprompt, userprompt, tempur=0.9):
    completion = client.chat.completions.create(
            model=f"{llm_model}",
            messages=[
                {"role": "system", "content": f"{systemprompt}"},
                {"role": "user", "content": f"{userprompt}"}
            ],
            temperature=tempur,
        )
    output = completion.choices[0].message.content
    return output