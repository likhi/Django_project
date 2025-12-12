from django.db import models
from django.contrib.auth.models import User
from PIL import Image  #pillow package  => pip install pillow
# Create your models here.

class profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default="default.jpg", upload_to='profile_pics')

    def __str__(self):
        return f'(self.user)profile'
    

    #python code to resize the image
    #why we need to resize the image...to decrease the storage space
    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
        super().save()
        image=Image.open(self.image.path)
        if image.width>300 and image.height>300:
            size=(300,300)
            image.thumbnail(size)
            image.save(self.image.path)