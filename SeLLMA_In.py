from presi_flair_encode import presi_flair_encryption
from Wrappers.translate_llm import translate_llm
from Wrappers.neutralization import neutralize_text
from Wrappers.send_to_gpt import chat_gpt_messenger


text = """
## Profil

**Name:** Lena Schmidt

**Geschlecht:** Weiblich

**Alter:** 23

**Anschrift:**  Am Park 12, 10437 Berlin

**Bildung:** Bachelorabschluss in Soziologie

**Arbeitserfahrung:** Lena hat bereits während ihres Studiums Erfahrungen im sozialen Bereich gesammelt. Sie arbeitete Teilzeit in einem Jugendzentrum und absolvierte Praktika bei verschiedenen NGOs. Nach ihrem Abschluss fand sie eine Stelle als Projektmitarbeiterin bei einer Organisation, die sich für die Integration von Flüchtlingen einsetzt.

**Soziales Engagement:**  Lena engagiert sich ehrenamtlich in einer Initiative, die Obdachlosen hilft. Sie organisiert regelmäßig Spendenaktionen und unterstützt bei der Verteilung von Essen und Kleidung.

**IT-Erfahrung:** Lena besitzt grundlegende Computerkenntnisse und ist vertraut mit gängigen Office-Programmen. Sie nutzt Social Media aktiv und hat erste Erfahrungen mit der Erstellung von Websites. 
"""
text = text.replace('*','')
encrypt = presi_flair_encryption(text)
encrypt_translated = translate_llm(encrypt)

with open('Encrypt_Translated.txt','w') as f:
    f.write(encrypt_translated)
    f.close()

encrypt_translated_neutral = neutralize_text(encrypt_translated)

with open('Encrypt_Translated_Neutral.txt','w') as f:
    f.write(encrypt_translated_neutral)
    f.close()

outside_llm = chat_gpt_messenger(encrypt_translated_neutral)

print(outside_llm)

output = outside_llm
with open('ChatGPTAnswer_Neutral.txt','w') as f:
    f.write(output)
    f.close()