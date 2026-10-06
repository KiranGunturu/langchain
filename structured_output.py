from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Load API credentials and other settings from the local .env file.
load_dotenv()

# Define the fields and descriptions expected in the model's structured response.
class SQLOutput(BaseModel):
    query: str = Field(description="The generated SQL query.")
    explanation: str = Field(description="A brief explanation of the SQL query.")

# Create the chat model and constrain its output to the schema above.
model = ChatOpenAI(model="gpt-5-mini")
model_structured = model.with_structured_output(SQLOutput)

# Ask for a SQL query and receive the result as an SQLOutput instance.
response = model_structured.invoke("give me sql to get top 5 products by sales from orders table")

# Print the generated query and its explanation separately.
print(response.query)
print(response.explanation)