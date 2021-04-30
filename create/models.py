from django.db import models
# Create your models here.
class Lounge(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=200, unique=True, null=True, blank=True)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    isYoutube = models.BooleanField(default=False)
    isAmazon = models.BooleanField(default=False)
    isBitcoin = models.BooleanField(default=False)
    isTiktok = models.BooleanField(default=False)
    isSpotify = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Reddit(models.Model):
    lounge = models.ForeignKey(Lounge,on_delete=models.CASCADE, related_name="reddit")
    name = models.CharField(max_length=200)


class Videos(models.Model):
    lounge = models.ForeignKey(Lounge,on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=500)
    src = models.CharField(max_length=500)
    alt = models.CharField(max_length=500)





# class Youtube(models.Model):
#     id = models.IntegerField(primary_key=True)
#     page = models.ForeignKey(LoungePage, on_delete=models.CASCADE, related_name="youtubeVideos")
#     nameOfVid = models.CharField(max_length=500)
#     idOfVideo = models.CharField(max_length=500)

# class Amazon(models.Model):
#     id = models.IntegerField(primary_key=True)
#     page = models.ForeignKey(LoungePage, on_delete=models.CASCADE, related_name="Amazon")
#     nameOfAmazon = models.CharField(max_length=500)

# class Bitcoin(models.Model):
#     id = models.IntegerField(primary_key=True)
#     page = models.ForeignKey(LoungePage, on_delete=models.CASCADE, related_name="youtubeVideos")
#     name = models.CharField(max_length=500)
