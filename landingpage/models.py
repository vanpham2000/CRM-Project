from django.db import models

# Create your models here.
# models.py in your app directory
from django.db import models

class MyAccountModel(models.Model):
    userID = models.CharField(max_length=256,primary_key=True)
    email = models.CharField(max_length=256,unique=True)
    password = models.CharField(max_length=256)
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    role = models.CharField(max_length=256)
    role = models.CharField(max_length=256)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False  # This tells Django not to manage this table's creation or modifications
        db_table = 'user'  # Replace with the actual table name in your database


class CustomerAccount(models.Model):
    accountID = models.CharField(max_length=256, primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.PositiveIntegerField()
    birthdate = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.accountID  # Use accountID as the string representation

    class Meta:
        managed = False
        db_table = 'account'  # Set the table name to match your database table

class Sale(models.Model):
    saleID = models.CharField(max_length=256, primary_key=True)
    accountID = models.CharField(max_length=256)
    email = models.EmailField()
    product_or_service = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.saleID

    class Meta:
        managed = False
        db_table = 'sale'

class OrderDetail(models.Model):
    orderID = models.CharField(max_length=256, primary_key=True)
    saleID = models.CharField(max_length=256)
    total = models.DecimalField(max_digits=60, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.orderID

    class Meta:
        managed = False
        db_table = 'OrderDetail'
