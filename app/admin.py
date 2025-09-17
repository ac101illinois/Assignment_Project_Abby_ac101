from django.contrib import admin
from .models import Student, CoffeeShop, Visit, Review
from datetime import date
# Register your models here.
admin.site.register(Student)
admin.site.register(CoffeeShop)
admin.site.register(Visit)
admin.site.register(Review)

