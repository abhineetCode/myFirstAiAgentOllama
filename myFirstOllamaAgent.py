from langchain_ollama.llms import OllamaLLM
# langchain_ollama provides inftrastructure for interacting with 
# Ollama service.
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# LangChain is a framework that just makes it a lot easier for us to work with LLMs.
# Ollama is a tool that allows us to run LLMs locally.
# We can use Ollama to run a local LLM and LangChain to interact with it.
# create a new llm or model
model = OllamaLLM(model="llama3.2")

template = """
You are an exeprt in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break

    #result = chain.invoke({"reviews": 4, "question": "what is the best pizza place in town?"}) # 
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    
    print(result)
