
# Adding some things from other files
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model): #This line defines our model which is an object
# Bacisally this whole class is declaring the fields in our database aka model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Class is a special keyword that indicates that we are defining an object
    # Post is the name of our model / no special characters or whitespace
    # models.Model means that the post is a Django Model so that Django knows that it will be saved in the database
    # models.CharField is how you define text with a limited number of characters
    # models.TextField is for long text without a limit
    # models.DateTimeField is a date and time
    # models.ForeignKey is a link to another model

    # Getting the time zone for the published_date from the above class?
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # This returns a text string with a post title
    def __str__(self):
        return self.title
    # Django is sensitive to whitespace so making sure that everything is 
    # indented correctly otherwise it wont know that the functions are part of the class


# Create your models here.
