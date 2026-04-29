import streamlit as st
from langchain_community.llms import OpenAI

st.title('🦜🔗 Quickstart App')

# 1. El usuario ingresa su clave aquí (se guarda en la variable openai_api_key)
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    # 2. Usamos la variable, NO escribimos la clave real aquí
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm.invoke(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    
    # 3. Validaciones
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
