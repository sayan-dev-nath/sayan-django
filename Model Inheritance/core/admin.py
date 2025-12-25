from django.contrib import admin
from .models import (
    Student,
    Teacher,
    Contractor,
    Candidate,
    ExamCenter,
    Product,
    DiscountedProduct,
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "fees"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "salary", "join_date"]


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "payment", "join_date"]


@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ["id", "center_name", "center_city"]


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "roll"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "stock"]


@admin.register(DiscountedProduct)
class DiscountedProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "stock"]
