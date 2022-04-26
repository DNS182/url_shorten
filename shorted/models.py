from django.db import models

# Create your models here.
class Shortner(models.Model):
    origna_url = models.URLField(help_text= "Add the original URL that you want to shorten.")
    key = models.CharField(unique = True , max_length=10 ,help_text= "Add something to append at last" )

    def __str__(self):
        return self.origna_url