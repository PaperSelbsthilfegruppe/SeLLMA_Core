from presi_flair_encode_gendered import presi_flair_encryption
from Wrappers.translate_llm import translate_llm
from Wrappers.send_to_gpt import chat_gpt_messenger
from Wrappers.iter_warp import iter_wrap as iw

source = './Workflow/00_Dataset'
for i in iw(source):
    #print(i)
    text = i['Content']
    filename = i['Filename']
    print(filename)
    text = text.replace('*','')
    encrypt = presi_flair_encryption(text, filename=filename)
    with open(f'./Workflow/01_Encryption/Encrypt_{filename}','w') as f:
        f.write(encrypt)
        f.close()
    encrypt_translated = translate_llm(encrypt)

    with open(f'./Workflow/02_Encryption_Translation/Encrypt_Translated_{filename}','w') as f:
        f.write(encrypt_translated)
        f.close()

    outside_llm = chat_gpt_messenger(encrypt_translated)

    #print(outside_llm)

    output = outside_llm
    with open(f'./Workflow/03_ChatGPT/ChatGPTAnswer_{filename}','w') as f:
        f.write(output)
        f.close()