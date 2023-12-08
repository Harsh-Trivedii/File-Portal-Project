from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UploadedFile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.FileField(upload_to='media/')
    upload_date=models.DateTimeField(auto_now_add=True)
    shared_with=models.ManyToManyField(User,related_name='shared_files')
    shared=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username}-{self.file.name}"