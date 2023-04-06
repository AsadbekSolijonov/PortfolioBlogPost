from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    # Kerakli maydon 
    title = models.CharField(max_length=255)
    
    # Bazada titlega nima yozilgani ko'rinib turishi uchun
    def __str__(self):
        return self.title

    # Sarlavhani doim capitalize() formatda saqlash
    def save(self, *args, **kwargs):
        if self.title:
            self.title = self.title.title().replace(' ', '-')
        super().save(*args, **kwargs)

class Post(models.Model):
    # Bitta Post ko'pgina Categoriyaga tushushi mumkin va Bitta Kategoriya Ko'pgina Postlarga tushishi mumkin.
    category = models.ManyToManyField('Category', related_name='posts')
    # Kerakli maydonlar
    title = models.CharField(max_length=255)
    body = RichTextField()
    # Post yozilishi bilan avtomatik vaqtni bazaga yozish uchun
    created_on = models.DateTimeField(auto_now_add=True)
    # Post o'zgartirilishi bilan avtomatik vaqtni bazaga o'zgartirilgan vaqtini yozish uchun
    last_modified = models.DateTimeField(auto_now=True)

    # Bazada titlega nima yozilgani ko'rinib turishi uchun
    def __str__(self):
        return self.title

class Comment(models.Model):
    # Bitta Postga Ko'pgina Kommentaraiya yozish mumkin.
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    # Kerakli maydonlar
    author = models.CharField(max_length=25)
    body = models.TextField()
    # Comment yozilishi bilan avtomatik vaqtni bazaga yozish uchun
    created_on = models.DateTimeField(auto_now_add=True)
