from django.db import models


# Create your models here.
class tweet(models.Model) :
    Author = models.CharField(max_length = 40)
    body  = models.TextField(max_length = 140)
    date  = models.DateTimeField(auto_now_add=True, blank=True)
    likes =  models.IntegerField(default=0)
    
    def __unicode__(self):
            return self.Author


    
class Comment(models.Model):
    commentAuthor = models.CharField(max_length=200)
    body = models.TextField()
    comment_date  = models.DateTimeField(auto_now_add=True, blank=True)
    comment_likes =  models.IntegerField(default=0)
    tweet = models.ForeignKey(tweet)
    
    