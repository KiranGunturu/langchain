from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Load API credentials and other settings from the local .env file.
load_dotenv()

class SQLOutput(BaseModel):
    query: str = Field(description="The generated SQL query.")
    explanation: str = Field(description="A brief explanation of the SQL query.")

model = ChatOpenAI(model="gpt-5-mini")
model_structured = model.with_structured_output(SQLOutput)

response = model_structured.invoke("give me sql to get top 5 products by sales from orders table")

print(response.query)
print(response.explanation)