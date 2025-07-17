from langchain_ollama import ChatOllama


# LangChain is a framework that just makes it a lot easier for us to work with LLMs.
# Ollama is a tool that allows us to run LLMs locally.
# We can use Ollama to run a local LLM and LangChain to interact with it.
# create a new llm or model
model = ChatOllama(model="llama3.2")

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = model.invoke(messages)
print(ai_msg.content)
