from langchain_chroma import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

# Load API credentials and other settings from the local .env file.
load_dotenv()

# Configure embeddings to match those used when indexing the policy documents.
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)
# Connect to the persisted Chroma collection containing the indexed policies.
vector_store = Chroma(collection_name="hr_policies",
                      embedding_function=embeddings,
                      persist_directory="./chroma_db")

# Find the two documents most similar to the remote-work question.
similar_docs = vector_store.similarity_search("What is the policy on remote work?", k=2)

# Display the retrieved documents and their metadata.
print(similar_docs)