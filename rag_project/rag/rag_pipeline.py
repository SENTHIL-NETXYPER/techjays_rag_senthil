from .retriever import search_documents
from .generator import generate_answer


def ask_question(question,document_id):

    print("QUESTION RECEIVED:", question)#verifying teh quesiton came to 

    results = search_documents(question,document_id) #serch db related documentid

    chunks = results["documents"][0]

    print("\nRETRIEVED CHUNKS:")

    for i, chunk in enumerate(chunks):
        print(f"\n--- CHUNK {i + 1} ---")
        print(chunk)

    context = "\n\n".join(chunks)

    print("\nCONTEXT LENGTH:", len(context))

    answer = generate_answer(question, context)

    return answer