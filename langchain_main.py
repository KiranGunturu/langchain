from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatOpenAI(model="gpt-5-mini")

# user_message = input("What is the capital of France?")
# context = []

prompt = PromptTemplate(template="""

tell me about {topic} in 10 words
""")

input = prompt.invoke({"topic": 'ai agents'})

result = model.invoke(input)

print(result.text)