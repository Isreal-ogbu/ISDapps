from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about """
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        """Return string representation of the models"""
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        """return a string representation of the text"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        elif len(self.text) >= 0:
            return self.text
