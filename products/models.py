from django.db import models
from django.contrib.auth.models import User
# Create your models here.

## Product class
class Product(models.Model):
    #title
    title = models.CharField(max_length = 225)
    #url
    url = models.TextField()
    #pub_date
    pub_date = models.DateTimeField()
    #body
    body = models.TextField()
    #image
    image = models.ImageField(upload_to='images/')
    #icon
    icon = models.ImageField(upload_to='images/')
    #votes_total
    votes_total = models.IntegerField(default = 1)
    #hunter
    hunter = models.ForeignKey(User , on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

        #pub_date_pretty
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
