from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    campus_address = models.CharField(max_length=200)
    major = models.CharField(max_length=100, blank=True)

class CoffeeShop(models.Model):
    shop = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)

class Visit(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    visit_date = models.DateField()
    study_duration = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'shop', 'visit_date'], name='unique_visit_date')
        ]
        ordering = ['visit_date']

class Review(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0) # on a scale of 1 to 5
    comment = models.TextField(blank=True)




