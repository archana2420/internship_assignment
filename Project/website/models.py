from django.db import models
import uuid

# Create your models here.
class User_info(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    username=models.CharField(max_length=15)
    email=models.EmailField(max_length=32)
    password=models.CharField(max_length=32)
    address=models.CharField(max_length=200)

    