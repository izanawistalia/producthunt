from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    icon = models.ImageField(upload_to='images/')
    url = models.TextField()
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_dated(self):
        return self.pub_date.strftime( '%A %e, %Y' )

    def __str__(self):
        return self.title
