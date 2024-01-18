import os
import uuid

from dotenv import load_dotenv, find_dotenv
from qdrant_client import QdrantClient
from langchain.embeddings import HuggingFaceEmbeddings

cwd = os.getcwd()

load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

ERROR_MESSAGE = 'We are facing technical issue at this moment.'

QDRANT_URL = 'http://localhost:5102'
client = QdrantClient(
    host='localhost',
    port=5102
)
COLLECTION_NAME = f'{uuid.uuid1()}'

'''Embeddings config
'''
EMBEDDING_FUNCTION = HuggingFaceEmbeddings(
    model_name='sentence-transformers_all-mpnet-base-v2',
    model_kwargs={'device': 'cuda'}
)


DOWNLOAD_DIR = 'arxiv_pdfs'
DOWNLOAD_DIR_PATH = os.path.join(
    cwd,
    DOWNLOAD_DIR
)
os.makedirs(DOWNLOAD_DIR_PATH, exist_ok=True)
