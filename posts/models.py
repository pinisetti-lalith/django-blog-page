from django.db import models
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absoulte_url(self):
        return '/post/%s/' % (self.id)
