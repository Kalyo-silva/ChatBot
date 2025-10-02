import streamlit as st
from settings.settings_api import API
from settings import settings_conf
from infra.chatbot import ChatBot

st.set_page_config(
    page_title='ChatBot IA',
    page_icon=settings_conf.PATH_ASSETS / "page_icon.png",
    layout='centered'
)


def main():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    inst_chat = ChatBot()
    st.title('🤖 ChatBot IA',width="content")
    st.divider()
    person_names = ["Alan Turing","Linus Torvalds","Steve Jobs","Grace Hopper","Elon Musk","Bill Gates"]
    tabs__ = st.tabs(person_names)

    try:
        for i, tab in enumerate(tabs__):
            with tab:
                for message in st.session_state.messages:
                    with st.chat_message(message["role"], avatar=message["avatar"]):
                        st.markdown(message["content"])

                PATH_IMAGE = f'{settings_conf.PATH_ASSETS / person_names[i]}.jpeg' 
                # st.image(image=str(PATH_IMAGE),caption=f'{person_names[i]}')

                if inst_chat.setPersonagem(i):
                    st.session_state.messages = []

                st.subheader(f'Olá, você esta conversando com {person_names[i]}')
                
                if prompt := st.chat_input("What is up?", key=f"{person_names[i]}"):
                    st.chat_message("user").markdown(prompt)
                    st.session_state.messages.append({"role": "user", "content": prompt, "avatar" : "user"})
                    
                    response = inst_chat.responda(prompt)

                    with st.chat_message(f'{person_names[i]}',avatar=f"{PATH_IMAGE}"):
                        st.markdown(response)
                    
                    st.session_state.messages.append({"role": f"{person_names[i]}", "content": response, "avatar": f"{PATH_IMAGE}"})
                # question = st.text_input('Pergunta', key=f'question_{i}')
                # if st.button(label='Enviar', key=f'send_{i}'):
                #     with st.chat_message('assistant'):
                #         st.write(inst_chat.responda(question))

    except Exception as e:
        st.error(f'Ops! Sei la eu o que deu, da teus pulo ai --> Error {e}')

if __name__ == '__main__':
    # with st.container(border=True):
    main()  