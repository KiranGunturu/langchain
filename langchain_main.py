from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# Load API credentials and initialize the chat model.
load_dotenv()
model = ChatOpenAI(model="gpt-5-mini")

# Prepare a prompt that asks the model to explain a supplied topic.
prompt = PromptTemplate(template="""

tell me about {topic} in 100 words
""")

# Prepare a prompt that turns an article into five quiz questions.
prompt1 = PromptTemplate(template="""

based on below article, create 5 quiz questions

{article}
""")

# input = prompt.invoke({"topic": 'ai agents'})

# result = model.invoke(input)

# print(result.text)

#chain

#runnables

# Parse model responses as plain text and compose the prompt/model stages.
parser = StrOutputParser()
chain = prompt | model | parser | prompt1 | model | parser

# Run the chain for the selected topic and print its result.
result = chain.invoke({"topic": 'ai agents'})

print(result)


