from django.db import models
from django.contrib.auth import get_user_model
# from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from django.urls import reverse


mymodel = get_user_model()

BLOG_CATEGORY = (
    ('python','PYTHON'),
    ('machine_learning','MACHINE LEARNING'),
    ('javascript','JAVASCRIPT'),
    ('react','REACT'),
)

class Post(models.Model):
    author = models.ForeignKey(mymodel,on_delete=models.CASCADE)
    category = models.CharField(max_length=30,choices=BLOG_CATEGORY,default='python')
    title=  models.CharField(max_length=50)
    # image = models.ImageField(blank=True,null=True)
    synopsis = models.CharField(max_length=100,default=None)
    content = HTMLField(blank=True,null=True)
    # content = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'post by {self.author.username} on {self.title}'
    
    def get_absolute_url(self):
        return reverse('postdetail',args=[str(self.id)])


