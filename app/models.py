from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Services(models.Model):
    name=models.CharField(max_length=20,verbose_name='Service Name')
    price=models.IntegerField()
    pdetail=models.CharField(max_length=300 , verbose_name='service Detail')
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.pdetail



class Cart(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE ,db_column='uid')
    pid=models.ForeignKey('Services',on_delete=models.CASCADE, db_column='pid')
    qty=models.IntegerField(default=1)


class Order(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE ,db_column='uid')
    pid=models.ForeignKey('Services',on_delete=models.CASCADE, db_column='pid')
    qty=models.IntegerField(default=1) 
    amt=models.IntegerField() 








           


 



