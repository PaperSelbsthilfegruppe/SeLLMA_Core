from presi_flair_encode import presi_flair_encryption
from Wrappers.translate_llm import translate_llm
from Wrappers.neutralization import neutralize_text
from Wrappers.send_to_gpt import chat_gpt_messenger
from Wrappers.iter_warp import iter_wrap as iw

source = './Workflow_Neutral/00_Dataset'
for i in iw(source):
    #print(i)
    text = i['Content']
    filename = i['Filename']
    print(filename)
    text = text.replace('*','')
    encrypt = presi_flair_encryption(text, filename=filename)
    with open(f'./Workflow_Neutral/01_Encryption/Encrypt_{filename}','w') as f:
        f.write(encrypt)
        f.close()
    encrypt_translated = translate_llm(encrypt)

    with open(f'./Workflow_Neutral/02_Encryption_Translation/Encrypt_Translated_{filename}','w') as f:
        f.write(encrypt_translated)
        f.close()

    encrypt_translated_neutral = neutralize_text(encrypt_translated)

    with open(f'./Workflow_Neutral/03_Encryption_Translation_No_Gender/Encrypt_Translated_Neutral_{filename}','w') as f:
        f.write(encrypt_translated_neutral)
        f.close()

    outside_llm = chat_gpt_messenger(encrypt_translated_neutral)

    #print(outside_llm)

    output = outside_llm
    with open(f'./Workflow_Neutral/04_ChatGPT/ChatGPTAnswer_Neutral_{filename}','w') as f:
        f.write(output)
        f.close()