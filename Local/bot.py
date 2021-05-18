import json
import requests

TELE_TOKEN = "<YOUR TOKEN>"
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)
respuestas = {
    '/tutorias': {'description': '¿Cómo ordenar una tutoria? 📝', 'text': '''Las tutorías deben agendarse por medio de la mesa de ayuda: 🌐🔗https://mda.uis.edu.co/, seleccionando el tema de ayuda "MISION TIC/ agendar tutoría"

Los horarios establecidos para el tutor 9 (Gabriel Vega) son: 
    * 8AM - 10AM
    * 4PM - 6PM
    * 6PM - 8PM
    '''},
    '/codigo': {'description': 'Ver el código de este bot {</>}', 'text': '''El código de este bot se puede encontrar en el repositorio 🌐https://github.com/ga-vo
    
Este bot está soportado utilizando AWS Lambda Functions: 🌐https://aws.amazon.com/es/lambda/features/'''},
    '/contacto': {'description': 'Cómo ponerse en contacto con el tutor 🕶',
                  'text': ''' Puedes ponerte en contacto con el tutor a través de 📧misiontic.tutor9.uis.edu.co '''}
}


def update(offset):
    # Llamar al metodo getUpdates del bot, utilizando un offset
    respuesta = requests.get(URL + "getUpdates" + "?offset=" + str(offset))
    # Telegram devolvera todos los mensajes con id IGUAL o SUPERIOR al offset
    # Decodificar la respuesta recibida a formato UTF8
    mensajes_js = respuesta.content.decode("utf8")

    # Convertir el string de JSON a un diccionario de Python
    mensajes_diccionario = json.loads(mensajes_js)

    # Devolver este diccionario
    return mensajes_diccionario


def read_message(message):
    chat_id = message['message']['chat']['id']
    message_id = message['message']['message_id']
    persona = message['message']['from']['first_name']
    me = message['message']['text']
    type_chat = message['message']['chat']['type']
    isGroup = type_chat == 'group'
    id_update = message["update_id"]
    isCommand = False
    try:
        varia = message['message']['entities']
        print(type(varia))
        print(varia)
        isCommand = varia[0]['type'] == 'bot_command'
    except Exception as e:
        print("Error entities")
        print("Error", str(e))

    return chat_id, message_id, persona, me, isGroup, isCommand,id_update


def send_message(text, chat_id):
    final_text = text
    url = URL + "sendMessage?text={}&chat_id={}".format(final_text, chat_id)
    requests.get(url)


def reply_message(text, chat_id, message_id):
    final_text = text
    url = URL + "sendMessage?text={}&chat_id={}&reply_to_message_id={}".format(
        final_text, chat_id, message_id)
    requests.get(url)


def handle_command(text, chat_id):
    flag = False
    for i in respuestas:
        if(i in text.lower()):
            reply = respuestas[i]['text']
            send_message(reply, chat_id)
            flag = True
            break

    if("/commands" in text.lower()):
        reply = "Los comandos disponibles son:"
        for i in respuestas:
            reply += "\n"+i+" - "+respuestas[i]['description']
        send_message(reply, chat_id)
    elif(not flag):
        reply = "Comando no reconocido, use /commands para ver la lista de comandos disponibles"
        send_message(reply, chat_id)


# Variable para almacenar la ID del ultimo mensaje procesado
ultima_id = 0

while(True):
    mensajes_diccionario = update(ultima_id)
    for message in mensajes_diccionario["result"]:

        try:
            chat_id, message_id, persona, me, isGroup, isCommand,id_update = read_message(message)
            if id_update > (ultima_id-1):
                ultima_id = id_update + 1

            if(not isGroup):
                send_message("Debes estar en un grupo para usar este bot", chat_id)
            # Si la ID del mensaje es mayor que el ultimo, se guarda la ID + 1
            
            if("Hola" in me):
                reply = "Hola "+persona + "! 😁"
                reply_message(reply, chat_id, message_id)
            else:
                if(isCommand):
                    if(isGroup):
                        handle_command(me, chat_id)

            print(message['message'])
        except Exception as e:
            print("E")
            print("Error", str(e))

        

    # Vaciar el diccionario
    mensajes_diccionario = []
