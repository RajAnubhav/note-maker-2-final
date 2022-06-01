from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField  # this is to import the text-editor

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # this will associate these two models
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    insta_url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)

class Post(models.Model):
# <<<<<<< HEAD
    title=models.CharField(max_length=255)
    # date - 21/05/2022 : added the image uploadation for the user to its profile
    header_image = models.ImageField(null=True, blank=True, upload_to='images/') # this will allow the user without the images to its profile
    # set the destination of the image 
    '''
        we should not store the image to the database, instead we must use aws and other services and store the link of the image
        this will save the space of the database. Heroku wouldn't let you upload the images to the database.
        ------------------------------------------------------------------------------------------------------------------------
        Steps to install the images
        \----> install the pillow using the command 'pip install Pillow'
        \----> 
    '''


# =======
    title = models.CharField(max_length=255)
# >>>>>>> ad80553527f81c5b7a36fe0dc683373f6554c731
    title_tag = models.CharField(max_length=255, default="NotesApp")

    # this is for adding the images by the user on the user's page
    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')
    '''
    For this we need to add the path of the media 
    in the settings.py

    STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

    MEDIA_URL = 'media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

    after this we need to do collectstatic
    
    '''

    # date - 21/05/2022 : added the snippet to the articles-details.html page
    # snippet = models.CharField(max_length=255, default="Click link above to read notes")

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    # body=models.TextField(max_length=1000000000)

    # date - 21/05/2022 : added the ckeditor to the body of the add_post.html
    body = RichTextField(blank=True, null=True)

    category = models.CharField(max_length=255, default='coding')
    # adding the likes and dislike feature to this project
    likes = models.ManyToManyField(User, related_name='note_post', default='1')

    # adding the privacy feature to the djagno project
    # visible = models.OneToOneField(User, related_name='private', default='0', on_delete = models.CASCADE)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("article-detail", args={str(self.id)})
