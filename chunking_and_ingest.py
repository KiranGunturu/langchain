from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from langchain_text_splitters import CharacterTextSplitter, TextSplitter, RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_chroma import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

# Load API credentials and other settings from the local .env file.
load_dotenv()

# Use the same embedding model and dimensions for indexing and later retrieval.
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)

# Load the policy PDF as a single Markdown-formatted document.
loader = PyMuPDF4LLMLoader("docs/Bank_HR_Policy.pdf", mode="single")

# Alternative loader configuration that uses the loader's default mode.
#loader = PyMuPDF4LLMLoader("docs/Bank_HR_Policy.pdf")

# Read the PDF contents into LangChain documents.
docs = loader.load()

# Split the document at Markdown headings and retain heading text as metadata.
splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
)
chunks = splitter.split_text(docs[0].page_content)

# Connect to the persistent Chroma collection for HR policy documents.
vector_store = Chroma(collection_name="hr_policies",
                      embedding_function=embeddings,
                      persist_directory="./chroma_db")

# Embed and store the document chunks in the vector database.
vector_store.add_documents(chunks)