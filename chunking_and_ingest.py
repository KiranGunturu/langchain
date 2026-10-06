from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from langchain_text_splitters import CharacterTextSplitter, TextSplitter, RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_chroma import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)

loader = PyMuPDF4LLMLoader("docs/Bank_HR_Policy.pdf", mode="single")

#loader = PyMuPDF4LLMLoader("docs/Bank_HR_Policy.pdf")

docs = loader.load()

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
)
chunks = splitter.split_text(docs[0].page_content)

vector_store = Chroma(collection_name="hr_policies",
                      embedding_function=embeddings,
                      persist_directory="./chroma_db")

vector_store.add_documents(chunks)