from Wrappers.send_to_gpt import chat_gpt_messenger
from Wrappers.iter_warp import iter_wrap as iw
from Wrappers.translate_llm_enger import translate_llm_enger

source = './Workflow_No_SeLLMA/00_Dataset'
for i in iw(source):
    text = i['Content']
    filename = i['Filename']
    outside_llm = chat_gpt_messenger(text)
    output = outside_llm
    with open(f'./Workflow_No_SeLLMA/01_ChatGPT/ChatGPTAnswer_{filename}','w') as f:
        f.write(output)
        f.close()
    translated = translate_llm_enger(output)

    with open(f'./Workflow_NO_SeLLMA/02_Translated/Translation_{filename}','w') as f:
        f.write(translated)
        f.close()