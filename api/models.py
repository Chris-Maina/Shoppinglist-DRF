from django.db import models

# Create your models here.
class Shoppinglist(models.Model):
    """ Shoppinglist model """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Display in a human readable manner """
        return "{}".format(self.name)
