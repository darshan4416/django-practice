from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    isbn = models.CharField(max_length=30)
    pages = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
    
