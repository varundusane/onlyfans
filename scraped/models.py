from django.db import models


# Create your models here.
class Details(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    thumbnail_img = models.CharField(max_length=200, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        if self.title == None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return str(self.title)


class image(models.Model):
    author = models.ForeignKey(Details, on_delete=models.CASCADE, related_name='images')
    # content = models.TextField()
    image = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        if self.author == None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return str(self.author)


class Video(models.Model):
    author = models.ForeignKey(Details, on_delete=models.CASCADE, related_name='videos')
    video = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        if self.author == None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return str(self.author)