from presi_flair_decode_gendered import pii_hash_decrypt
from Wrappers.translate_llm_enger import translate_llm_enger
from Wrappers.iter_warp import iter_wrap as iw

source = './Workflow/03_ChatGPT'
for i in iw(source):
    #print(i)
    text = i['Content']
    filename = i['Filename'][14:]
    print(filename)
    text = text.replace('*','')
    decrypt = pii_hash_decrypt(text, filename)
    with open(f'./Workflow/04_Decryption/decrypt_{filename}','w') as f:
        f.write(decrypt)
        f.close()

    decrypted_translated = translate_llm_enger(decrypt)

    with open(f'./Workflow/05_Decryption_Translation/decrypted_Translation_{filename}','w') as f:
        f.write(decrypted_translated)
        f.close()