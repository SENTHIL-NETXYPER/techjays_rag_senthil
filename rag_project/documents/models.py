from django.db import models

# Create your models here.
class Document(models.Model):
    title=models.CharField(max_length=200)
    file=models.FileField(upload_to="documents/")
    uploaded_at=models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.title

class ChatMessage(models.Model):#storing coversations
    document=models.ForeignKey(Document,on_delete=models.CASCADE,
                               related_name="messages")
    question=models.TextField()
    answer=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question
