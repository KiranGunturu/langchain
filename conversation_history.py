from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5-mini")

conversation = []
conversation.append(SystemMessage(content="You are a senior data engineer. Answer the user question in 3 to 4 sentences."))
while True:
    query = input("Ask a question: ")
    if query.lower() == "exit":
        break
    conversation.append(HumanMessage(content=query))
    response = model.invoke(conversation)
    conversation.append(AIMessage(content=response.content))
    print(response.content)
    print(conversation)