from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    campus_address = models.CharField(max_length=200)
    major = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CoffeeShop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.location})"

class Visit(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    shop = models.ForeignKey(CoffeeShop, on_delete=models.PROTECT)
    visit_date = models.DateField()
    study_duration = models.IntegerField(default=0)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'shop', 'visit_date'], name='unique_visit_date')
        ]
        ordering = ['visit_date']

    def __str__(self):
        return f"{self.student} visited {self.shop} on {self.visit_date}"

class Review(models.Model):
    rating_choices = [
        (1, "1 star"),
        (2, "2 stars"),
        (3, "3 stars"),
        (4, "4 stars"),
        (5, "5 stars"),
    ]
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=rating_choices)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Review {self.rating}/5 for {self.visit.student}"


