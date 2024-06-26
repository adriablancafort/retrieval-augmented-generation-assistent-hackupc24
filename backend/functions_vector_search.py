import os
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain_iris import IRISVector


def get_embedding_function():
    """
    Initialize and return the OpenAI embeddings model.
    """
    embeddings_model = OpenAIEmbeddings()
    return embeddings_model


def docs_to_chunks(document_text: str|list) -> list[Document]:
    """
    Convert a document string into chunks.

    Args:
    - document_text (str): The input document text.

    Returns:
    - list[Document]: A list of Document objects representing chunks of the input document.
    """
    splitter = RecursiveCharacterTextSplitter(
        separators=None,
        keep_separator=True,
        is_separator_regex=False,
        chunk_size=400,
        chunk_overlap=80,
        length_function=len,
    )

    if type(document_text) == str:
        chunks = splitter.split_text(document_text)
        chunks = [Document(page_content=chunk) for chunk in chunks]
    else:
        chunks = splitter.split_documents(document_text)
    return chunks


def save_database(document_text: str|list) -> None:
    """
    Save chunks of a document into a database with their embeddings.

    Args:
    - document_text (str): The input document text.
    """
    chunks = docs_to_chunks(document_text)
    embedding = get_embedding_function()

    # Database connection parameters
    username, password = 'demo', 'demo'
    hostname = os.getenv('IRIS_HOSTNAME', 'localhost')
    port, namespace = '1972', 'USER'
    CONNECTION_STRING = f"iris://{username}:{password}@{hostname}:{port}/{namespace}"

    

    # Initialize IRISVector instance
    db = IRISVector(
        embedding_function=embedding,
        dimension=1536,
        connection_string=CONNECTION_STRING,
    )

    # Clear existing collection
    db.delete_collection()

    # Store chunks into the database
    db = IRISVector.from_documents(
        embedding=embedding,
        documents=chunks,
        connection_string=CONNECTION_STRING,
    )


def nearest_vector(query: str, threshhold: float = 1) -> list[str]:
    """
    Find the nearest vectors to a given query string in the database.

    Args:
    - query (str): The query string.

    Returns:
    - list[str|None]: A list of strings representing the nearest vectors to the query.
    """
    embedding = get_embedding_function()

    # Database connection parameters
    username, password = 'demo', 'demo'
    hostname = os.getenv('IRIS_HOSTNAME', 'localhost')
    port, namespace = '1972', 'USER'
    CONNECTION_STRING = f"iris://{username}:{password}@{hostname}:{port}/{namespace}"

    # Initialize IRISVector instance
    db = IRISVector(
        embedding_function=embedding,
        dimension=1536,
        connection_string=CONNECTION_STRING,
    )

    # Perform similarity search on the database
    query_results = db.similarity_search_with_relevance_scores(query, k=4)
    # Filter results based on relevance score
    filtered_results = [chunk.page_content for chunk, score in query_results if score < threshhold]

    return filtered_results
