from senha import API_KEY
import requests 
import json

link = "https://api.openai.com/v1/chat/completions"
headers = {"Authorization":f"Bearer {API_KEY}","Content-Type":"application/json"}
id_model = "gpt-3.5-turbo-16k"

user_quest = input("Pergunte o que quiser para sair digite [s]: ").lower()
if user_quest == 's':
        print('você saiu da conversa')

else:
    while True:
        body_message = {
                    "model":id_model,
                    "messages": [{"role": "user", "content": user_quest}]
                }
        body_message = json.dumps(body_message)

        response = requests.post(link, headers=headers,data=body_message)
        

        respota = response.json()
        message = respota["choices"][0]["message"]["content"]
        print(message)  
        print('_____________________________________________________________________')
        user_quest = input("Pergunte o que quiser / para sair digite [s]: ").lower()
        

        


        
    
