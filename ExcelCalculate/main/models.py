from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length= 20)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length = 100)
    user_validate = models.BooleanField(default = False)


# class Item(models.Model):
#     item_name = models.CharField(max_length = 20)
#     item_price = models.IntegerField()
#     item_content = models.TextField(max_length = 200)