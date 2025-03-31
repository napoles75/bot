from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables de entorno (.env)

app = Flask(__name__)

# Configura tu API Key de OpenAI (https://platform.openai.com/api-keys)
openai.api_key = os.getenv("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")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data.get('query', '')  # Mensaje del usuario desde Dialogflow/WhatsApp
    
    # Llamada a OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    
    bot_response = response.choices[0].message['content']
    
    return jsonify({
        "fulfillmentText": bot_response  # Respuesta para Dialogflow
    })

if __name__ == '__main__':
    app.run()
