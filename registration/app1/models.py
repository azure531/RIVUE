from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class RIVUE(models.Model):
    ProModel = models.CharField(max_length=50)
    ProName = models.CharField(max_length=200)
    ProRev = models.CharField(max_length=1000)
    ProEmail = models.EmailField()
    ProCom = models.CharField(max_length=150)
    ProImage=models.ImageField(upload_to='images/',default=r"C:\Users\anusr\OneDrive\Desktop\milu.jpg")
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    class Meta:
        db_table="RIVUE"