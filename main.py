from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

# Load API credentials and other settings from the local .env file.
load_dotenv()

# Alternative chat models that can be used instead of the Hugging Face model.
#model = ChatOpenAI(model="gpt-5-mini")
#model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Create a text-generation endpoint for the selected Hugging Face model.
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task="text-generation",
)
# Wrap the endpoint with the chat interface expected by LangChain.
model = ChatHuggingFace(llm=llm)

# Send a prompt to the model and print the generated response.
response = model.invoke("tell me about ai agents in 10 words?")

print(response.content)