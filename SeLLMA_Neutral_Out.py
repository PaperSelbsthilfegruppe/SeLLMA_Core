from presi_flair_decode import pii_hash_decrypt
from Wrappers.de_netralization import gender_text
from Wrappers.translate_llm_enger import translate_llm_enger
from Wrappers.iter_warp import iter_wrap as iw

source = './Workflow_Neutral/04_ChatGPT'
for i in iw(source):
    #print(i)
    text = i['Content']
    filename = i['Filename'][22:]
    print(filename)
    text = text.replace('*','')
    decrypt = pii_hash_decrypt(text, filename)
    with open(f'./Workflow_Neutral/05_Decryption/decrypt_{filename}','w') as f:
        f.write(decrypt)
        f.close()

    decrypted_gender = gender_text(decrypt)

    with open(f'./Workflow_Neutral/06_Decryption_Gender/decrypted_Gender_{filename}','w') as f:
        f.write(decrypted_gender)
        f.close()

    decrypted_gender_translated = translate_llm_enger(decrypted_gender)

    with open(f'./Workflow_Neutral/07_Decryption_Gender_Translation/decrypted_Gender_Translation_{filename}','w') as f:
        f.write(decrypted_gender_translated)
        f.close()