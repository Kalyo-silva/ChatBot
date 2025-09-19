import streamlit as st
from src.settings.settings_api import API
from src.settings import settings_conf
from src.infra.chatbot import ChatBot

st.set_page_config(
    page_title='ChatBot IA',
    page_icon=settings_conf.PATH_ASSETS / "page_icon.png",
    layout='centered'
)

def main():
    inst_chat = ChatBot()
    st.title('🤖 ChatBot IA',width="content")
    st.divider()
    person_names = ["Alan Turing","Linus Torvalds","Steve Jobs","Grace Hopper","Elon Musk","Bill Gates"]
    tabs__ = st.tabs(person_names)

    try:
        for i, tab in enumerate(tabs__):
            with tab:
                if st.button(f'Iniciar conversa com {person_names[i]}'):
                    inst_chat.setPersonagem(i)
                    st.subheader(f'Olá, você esta conversando com {person_names[i]}')
                    question = st.text_input('Pergunta')
                    st.write(inst_chat.responda(question))
    except Exception as e:
        st.error(f'Ops! Sei la eu o que deu, da teus pulo ai')

if __name__ == '__main__':
    with st.container(border=True):
        main()  