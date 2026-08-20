from django.shortcuts import render,redirect,get_object_or_404
from .forms import Documentform
from rag.rag_pipeline import ask_question #we are proccing the quesiton getiitng it
from .models import Document,ChatMessage
from rag.document_loader import read_pdf,chunk_text
from rag.vector_store import store_embeddings
from rag.embedding import create_embeddings
from rag.vector_store import delete_document

def upload(req):
    if req.method =="POST":
    
    
        form=Documentform(req.POST,req.FILES) #using our form variable called doucment ofrm
        if form.is_valid():
            document=form.save()#assinging our db value into document
            try:
                file_path=document.file.path #users files it stores in file_path and process ot other=steps 
                print("filepath:",file_path)#why file path beacuse after storeing it sotres on place that place path is used by fiz to act to chunking

            #readdocument
                text=read_pdf(file_path)
                if not text.strip():
                    document.delete()
                    return render(
                        req,
                        "documents/upload.html",
                        {
                        "form": form,
                        "error": "Unable to extract text from this PDF. Please upload a text-based PDF."
                        }
                    )
            
            #chunking
                chunks=chunk_text(text)
                if not chunks:
                    document.delete()
                    return render(
                        req,
                        "documents/upload.html",
                        {
                            "form": form,
                            "error": "No usable content was found in this PDF."
                        }
                    )
                print("total chunks",len(chunks))
            #create embedding
                embeddings=create_embeddings(chunks)
            #store in chroma
                document_name=document.title
                ids=store_embeddings(chunks,embeddings,document_name,document.id)
                print("stored chunks:", len(ids))
                return redirect("document_list")
            except Exception as e:

                print("PROCESSING ERROR:", e)

                document.delete()

                return render(
                    req,
                    "documents/upload.html",
                    {
                        "form": form,
                        "error": "Sorry, this document could not be processed. Please try another PDF."
                    }
                )

            
    else:
        form=Documentform()


    return render(req,"documents/upload.html",
                  {"form":form}
                  )
def chat (req,document_id):
    print("current document",document_id)
    ans=None # if no naswer show blacnk
    document=get_object_or_404(Document,id=document_id)#sotring document as passed value of chroma id based convo
    messages=ChatMessage.objects.filter(document=document).order_by("created_at")#storing into message taht filltering out time we take convo
    if req.method=="POST":
        question=req.POST.get("question") #getting teh psot of quesiton inotuesion
        print("QUESTION FROM USER:",question)
        if question:
            ans=ask_question(question,document_id)#and passing to llm and passed to anser that results are
            print("ANSWER FROM RAG:", ans)
            ChatMessage.objects.create(#creating db or stroring db
                document=document,
                question=question,
                answer=ans,

            )
    return render(#passing values to html
        req,
        "documents/chat.html",#templated positon
        {"answer":ans,
         "document_id":document_id,
         "messages":messages #we are 
         }
    )  
def delete_doc(req, document_id): #for deleting choroma and dngo db too
    document = get_object_or_404(Document,id=document_id)
    delete_document(document_id)

    document.delete()

    return redirect("upload")
from .models import Document


def document_list(req): #for viewsing doucment lis

    documents = Document.objects.all().order_by("-id")

    return render(
        req,
        "documents/document_list.html",
        {"documents": documents}
    )

