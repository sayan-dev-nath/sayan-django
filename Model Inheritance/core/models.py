from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    join_date = models.DateField()

    class Meta:
        abstract = True


class Student(BaseModel):
    join_date = None
    fees = models.IntegerField()


class Teacher(BaseModel):
    salary = models.IntegerField()


class Contractor(BaseModel):
    join_date = models.DateTimeField()
    payment = models.IntegerField()


# Multi Table Inheritance
class ExamCenter(models.Model):
    center_name = models.CharField(max_length=50)
    center_city = models.CharField(max_length=50)


class Candidate(ExamCenter):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()


# Proxy Model
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()


class DiscountedProduct(Product):
    class Meta:
        proxy = True
        ordering = ["id"]
