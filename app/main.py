# Imports
import os
import streamlit as st
import syllables
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory


def is_haiku(poem):
    syllable_counts = [syllables.estimate(s) for s in poem.split()]
    return len(syllable_counts) == 3 and syllable_counts == [5, 7, 5]


def generate_haiku(prompt):
    # Prompt Templates
    title_template = PromptTemplate(
        input_variables=['topic'],
        template='write a haiku poem title about {topic}'
    )

    poem_template = PromptTemplate(
        input_variables=['title'],
        template='write me a haiku based on this title TITLE: {title}, \
        follow these rules: 17 syllables arranged in a 5-7-5 syllable pattern'
    )

    # Memory
    title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
    poem_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

    # LLMs
    llm = OpenAI(temperature=0.9)
    title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
    poem_chain = LLMChain(llm=llm, prompt=poem_template, verbose=True, output_key='poem', memory=poem_memory)

    title = title_chain.run(prompt)
    poem = poem_chain.run(title=title)

    return title, poem


def main():
    st.title('AutoGPT Haiku Generator')
    prompt = st.text_input('Plug in your prompt here')

    if prompt:
        title, poem = generate_haiku(prompt)

        st.write(title)
        st.write(poem)

        if is_haiku(poem):
            st.success("Generated Haiku:")
            st.info("\n".join(poem.split()))


if __name__ == '__main__':
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    main()
