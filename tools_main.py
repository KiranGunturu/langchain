
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tools import get_engine, get_stock_price, get_tables, get_schema


# Load API credentials and other settings from the local .env file.
load_dotenv()

model = ChatOpenAI(model="gpt-5-mini")

my_tools = [get_engine, get_stock_price, get_tables, get_schema]

model_tools = model.bind_tools(my_tools)

result = model_tools.invoke("show me all the tables in the database")

#print(result)

for tool_call in result.tool_calls:
    print(f"Calling tool '{tool_call['name']}' with arguments {tool_call['args']}")
