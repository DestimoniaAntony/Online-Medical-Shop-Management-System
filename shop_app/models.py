from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)
    
class Medicine(models.Model):
    med_name = models.CharField(max_length=100,null=True)
    image = models.ImageField( upload_to="media",null=True)
    description = models.CharField(max_length=10000,null=True)
    price = models.CharField(max_length=1000,null=True)
    Tquantity = models.CharField(max_length=1000,null=True)
    directions = models.CharField(max_length=1000,null=True)
    side_effects = models.CharField(max_length=1000,null=True)
    warnings = models.CharField(max_length=1000,null=True)
    consume_type = models.CharField(max_length=1000,null=True)
class Pharmacy(models.Model):
    pharmacy = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    phar_name = models.CharField(max_length=500 , null=True )
    location =  models.CharField( max_length=1000 , null=True )
    phone = models.CharField( max_length=1000 , null=True )
    email = models.EmailField(max_length=254, null=True)
    password = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to="media", null=True)
class Consumer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    con_name = models.CharField( max_length=1000 , null=True )
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField( max_length=10 , null=True )
    address = models.CharField( max_length=1000 , null=True )
    password = models.CharField( max_length=1000 , null=True )
class Cart(models.Model):
    consumer = models.ForeignKey(Consumer,on_delete=models.CASCADE,null=True)
    medicine = models.ForeignKey(Medicine,on_delete=models.CASCADE,null=True)
    pharmacy = models.ForeignKey(Pharmacy,on_delete=models.CASCADE,null=True)
    req_qnty = models.CharField( max_length=1000 , null=True )
    status = models.CharField(max_length=150, null=True)
    payment = models.CharField(max_length=150, null=True)
    med_name = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=1000,null=True)
    Tquantity = models.CharField(max_length=1000,null=True)
class Assign(models.Model):
    pharmacy = models.ForeignKey(Pharmacy,on_delete=models.CASCADE,null=True)
    consumer = models.ForeignKey(Consumer,on_delete=models.CASCADE,null=True)
    medicine = models.ForeignKey(Medicine,on_delete=models.CASCADE,null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=150, null=True)
    price = models.CharField(max_length=1000,null=True)
    req_qnty = models.CharField( max_length=1000 , null=True )
class Feedbacks(models.Model):
    consumer = models.ForeignKey(Consumer,on_delete=models.CASCADE,null=True)
    service = models.CharField(max_length=150, null=True)
    message = models.CharField(max_length=1050, null=True)