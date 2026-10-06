from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load API credentials and other settings from the local .env file.
load_dotenv()

# Create the chat model used to answer each question.
model = ChatOpenAI(model="gpt-5-mini")

# Keep system, user, and assistant messages so each turn has conversation context.
conversation = []
conversation.append(SystemMessage(content="You are a senior data engineer. Answer the user question in 3 to 4 sentences."))

# Continue accepting questions until the user enters "exit".
while True:
    query = input("Ask a question: ")
    if query.lower() == "exit":
        break

    # Add the question, send the full message history, and retain the reply.
    conversation.append(HumanMessage(content=query))
    response = model.invoke(conversation)
    conversation.append(AIMessage(content=response.content))

    # Display the latest reply and the accumulated conversation history.
    print(response.content)
    print(conversation)