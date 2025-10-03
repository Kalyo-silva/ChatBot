import google.generativeai as genai
from settings.settings_api import API



class ChatBot():
    def __init__(self):
        genai.configure(api_key=API.API_KEY)

        self.model = genai.GenerativeModel('gemini-2.5-flash-lite')
        self.chat = self.model.start_chat(history=[])

    def responda(self, pergunta) -> str:
        return self.chat.send_message(pergunta).text

    def setPersonagem(self, id):
        """ 0 - Alan Turing | 1 - Linus Torvalds | 2 - Steve Jobs | 3 - Grace Hopper | 4 - Elon Musk | 5 - Bill Gates """
        personagens = ['Alan Turing','Linus Torvalds','Steve Jobs','Grace Hopper','Elon Musk','Bill Gates']

        self.resetChat()
        print('teste?')
        self.chat.send_message("Responda todas a's mensagens como se você fosse "+personagens[id]+". ao ser perguntado quem é você ou perguntas pessoas você irá responder com informações relacionadas ao personagem. responda de forma simples e amigável as mensagens que são recebidas, mantendo as respostas curtas.")
        
    def resetChat(self):
        self.chat = self.model.start_chat(history=[])