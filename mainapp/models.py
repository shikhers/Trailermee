from django.db import models
from django.utils import timezone
#For main page for data.........................
class Video(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,)
    videotitle = models.TextField()
    videourl = models.TextField()
    details = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.videotitle
#End Here..................................

#For Hollywood page.......................
class Hollywood(models.Model):
    hollyvideo = models.TextField()
    hollyurl = models.TextField()
    hollydetails = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.hollyvideo
#End Here............................

#For Bollywood page................
class Bollywood(models.Model):
    bollyvideo = models.TextField()
    bollyurl = models.TextField()
    bollydetails = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.bollyvideo
#End Here............................

#For cartoon page............................
class Cartoon(models.Model):
    cartoonvideo = models.TextField()
    cartoonurl = models.TextField()
    cardetails = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cartoonvideo


#End Here..............................
