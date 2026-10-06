from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

#model = ChatOpenAI(model="gpt-5-mini")
#model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm)

response = model.invoke("tell me about ai agents in 10 words?")

print(response.content)