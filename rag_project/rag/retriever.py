from .vector_store import collection #periovusly we have created these 
from .embedding import model # we have used an model to encode 

def search_documents(query,document_id,n=3):
    query_embedding=model.encode([query]).tolist()#suer question here chahges into embeeding bec for more info view embeding
    results=collection.query(
        
        query_embeddings=query_embedding,#thes is right one is quesiton embedding and it means Take this question vector and search against the vectors already stored in this collection 
        where={"document_id": str(document_id)}, #based on id  and quesiton give the context ot llm
        n_results=n #its for giving the best like k=3 we have seen
        
        
    )
    print("SEARCHING DOCUMENT ID:", document_id)
    print("RESULT METADATA:", results["metadatas"])
    return results