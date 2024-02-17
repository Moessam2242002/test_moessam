from django.db import models
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name 
class Books(models.Model):
    book_name=models.CharField(max_length=50)
    auther=models.CharField(max_length=50)
    book_image=models.ImageField(upload_to='photos',blank=True,null=True)
    auther_image=models.ImageField(upload_to='photos',blank=True, null=True)
    pages=models.IntegerField(blank=True, null=True)
    price=models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)
    rental_price_day=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    rental_period=models.IntegerField(blank=True, null=True)
    total_rental=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    active=models.BooleanField(default=True)
    x=[('rental','rental'),('sold','sold'),('available','available')]
    status=models.CharField(max_length=50,choices=x)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    def __str__(self):
        return self.book_name