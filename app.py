import streamlit as st # type: ignore
from langchain import OpenAI
from langchain.chains import LLMChain # type: ignore
from langchain.prompts import PromptTemplate
import os
os.environ["OpenAI_API_KEY"]= "your-api-key-here "

st.title("Story Generator With LangChain")

st.divider()

topic = st.text_input("Enter a topic for your story")

prompt = PromptTemplate(
    input_variables= ["topic"],
    template= "Write a short story about {topic}."
)

llm = OpenAI()

chain = LLMChain(llm = llm, prompt = prompt)

st.divider()

if topic:
    response = chain.run(topic)
    st.write(response)