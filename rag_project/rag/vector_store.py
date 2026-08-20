import chromadb
#we are creating chroma db and named as coleciton
client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_or_create_collection(name="ai_documents")#Chroma's collection names cannot contain spaces.

def store_embeddings(chunks,embeddings,document_name,document_id):
    #give every chunk a document-specific ID.
    ids=[
        f"{document_name}_chunk_{i}"
        for i in range(len(chunks))]#we are crating id based on length of our total chunk size
    metadatas=[#for new filtering for suer uplods history to use
        {
            "document_id":str(document_id),
            "document_name":document_name,
            "chunk_index":i
        }
        for i in range(len(chunks))
    ]
    collection.add(#into the collection we are adding all storable things
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas


    )
    return ids #I returned ids mainly so we could verify how many records we stored.
def delete_document(document_id):
    collection.delete(where={"document_id": str(document_id)} #for deleteing the id based persons

    )