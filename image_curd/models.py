from django.db import models

class images(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images")

    def __str__(self):
      return str(self.title)
