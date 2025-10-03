import streamlit as st
from settings.settings_api import API
from settings import settings_conf
from infra.chatbot import ChatBot

def chat(pessoa, id):
    if st.session_state.personagem != pessoa:
        st.session_state.chat.setPersonagem(id)
        st.session_state.messages = []

    st.session_state.personagem = pessoa

    for message in st.session_state.messages:
                    with st.chat_message(message["role"], avatar=message["avatar"]):
                        st.markdown(message["content"])
    
    PATH_IMAGE = f'assets/{pessoa}.jpeg' 
    if prompt := st.chat_input("What is up?", key=f"{pessoa}"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt, "avatar" : "user"})
        
        response = st.session_state.chat.responda(prompt)

        with st.chat_message(f'{pessoa}', avatar=f"{PATH_IMAGE}"):
            st.markdown(response)
        
        st.session_state.messages.append({"role": f'{pessoa}', "content": response, "avatar": f"{PATH_IMAGE}"})

def intro():
    st.write("# Bem vindo Ao ChatBot IA! 👋")
    st.sidebar.success("Selecione um Personagem para começar a Conversar.")

    st.markdown(
        """
        Converse com personagens históricos da área da computação e técnologia.

        ### O que os personagens podem fazer?

        - Responder perguntas sobre suas vidas ✅
        - Conversar com você com seu estilo de comunicação ✅
        - Ensinar sobre a sua história e sua importância no mundo da técnologia. ✅

        ### Créditos

        Trabalho desenvolvido por [Kalyo Airan da Silva](https://github.com/Kalyo-silva)

        """
    )

def Alan():
    st.write("# Você está conversando com Alan Turing. 👋")
    st.sidebar.image('assets/Alan Turing.jpeg')
    chat('Alan Turing',0)

def Linus():    
    st.write("# Você está conversando com Linus Torvalds. 👋")
    st.sidebar.image('assets/Linus Torvalds.jpeg')
    chat('Linus Torvalds',1)
    
def Steve():
    st.write("# Você está conversando com Steve Jobs. 👋")
    st.sidebar.image('assets/Steve Jobs.jpeg')
    chat('Steve Jobs',2)
    
def Grace():
    st.write("# Você está conversando com Grace Hopper. 👋")
    st.sidebar.image('assets/Grace Hopper.jpeg')
    chat('Grace Hopper',3)
    
def Elon():
    st.write("# Você está conversando com Elon Musk. 👋")
    st.sidebar.image('assets/Elon Musk.jpeg')
    chat('Elon Musk',4)

def Bill():
    st.write("# Você está conversando com Bill Gates. 👋")
    st.sidebar.image('assets/Bill Gates.jpeg')
    chat('Bill Gates',5)

def main():
    st.set_page_config(
        page_title='ChatBot IA',
        page_icon=settings_conf.PATH_ASSETS / "page_icon.png",
        layout='centered'
    )

    Personagens = {
        "—": intro,
        "Alan Turing": Alan,
        "Linus Torvalds": Linus,
        "Steve Jobs": Steve,
        "Grace Hopper": Grace,
        "Elon Musk": Elon,
        "Bill Gates": Bill,
    }

    userSelect = st.sidebar.selectbox("Escolha um Personagem", Personagens.keys())
    Personagens[userSelect]()

if "messages" not in st.session_state:
        st.session_state.messages = []

if "personagem" not in st.session_state:
    st.session_state.personagem = ""

if "chat" not in st.session_state:
    st.session_state.chat = ChatBot()

main()