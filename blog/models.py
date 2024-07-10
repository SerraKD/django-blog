from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """ A class for Post model """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        """ A meta class for meta data, posts are listed from newest to oldest creation time """
        ordering = ["-created_on"]

    def __str__(self):
        # str dunder method to return a string for use in the admin panel #
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    """ A class for Comments model """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        """ A meta class for meta data, posts are listed from oldest tone west  creation time """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body}  by {self.author}"
