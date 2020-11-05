from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=200, null=True)
    total_calories = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sat_fat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    trans_fat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cholesterol = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sodium = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    carbohydrate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fiber_carb = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sugar_carb = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    protiens = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vitamins = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

# class UserMeal(models.Model):
#     user = 