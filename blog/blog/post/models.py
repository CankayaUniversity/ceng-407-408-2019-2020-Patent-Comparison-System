from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=120)
    text=models.TextField()
    publishing_date=models.DateTimeField()

    def __str__(self):
        return self.title
        #postun basligi neyse bize onu gosterecek