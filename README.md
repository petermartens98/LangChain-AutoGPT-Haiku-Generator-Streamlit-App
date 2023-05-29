# LangChain-AutoGPT-Haiki-Generator-Streamlit-App

The AutoGPT Haiku Generator is a Streamlit application that utilizes the OpenAI API and GPT-3.5 large language model to generate haikus. It provides an interactive interface for users to input prompts and receive haiku titles and poems as output.

### Functionality
1. Prompt Input: Users can enter their haiku prompt into the text input field provided by the application.
2. Haiku Generation: Upon entering a prompt, the application utilizes the OpenAI GPT-3 language model to generate a haiku title and poem.
3. Haiku Validation: The generated poem is validated to ensure it adheres to the haiku structure, which consists of three lines with syllable counts of 5, 7, and 5 respectively.
4. Output Display: The generated haiku title and poem are displayed to the user within the application.
5. Haiku Highlighting: If the generated poem is determined to be a valid haiku, it is highlighted with success formatting to provide visual emphasis.
### Technical Details
The AutoGPT Haiku Generator is built using the following technologies and components:

1. Python: The code is written in Python programming language.
2. Streamlit: The application utilizes Streamlit, a Python library for building interactive web applications, to create the user interface.
3. OpenAI API and GPT-3.5 model: The OpenAI GPT-3 language model is employed for generating haiku titles and poems based on user prompts.
4. Langchain Package: The langchain package is used for working with language models, prompts, chains, and memory. It provides convenient abstractions for interacting with the OpenAI GPT-3 model.
### Usage
To use the AutoGPT Haiku Generator:

1. Set up the required dependencies by installing the necessary packages and libraries specified in the requirements.txt file.
2. Obtain an OpenAI API key and set it as an environment variable named OPENAI_API_KEY.
3. Run the application by executing the Python script: python main.py.
4. Access the application in your web browser via the provided URL or localhost.

### Example Screenshots
![image](https://github.com/petermartens98/LangChain-AutoGPT-Haiki-Generator-Streamlit-App/assets/87671757/72bf062a-45b7-49e0-a079-46c54b0a595e)
![image](https://github.com/petermartens98/LangChain-AutoGPT-Haiki-Generator-Streamlit-App/assets/87671757/b37d5f86-b54d-4ab3-a3c1-5adaebd9bc36)
![image](https://github.com/petermartens98/LangChain-AutoGPT-Haiki-Generator-Streamlit-App/assets/87671757/bf7f5c89-2618-45a3-8136-ce4e50cd6bb3)

