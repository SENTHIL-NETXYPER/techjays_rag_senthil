from django.urls import path
from .import views
urlpatterns = [
    path("",views.upload,name="upload"),
    path("documents/", views.document_list, name="document_list"),
    path("chat/<int:document_id>/",views.chat,name="chat"),
    path("delete/<int:document_id>/", views.delete_doc, name="delete_doc"),
    
]
