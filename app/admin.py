from django.contrib import admin
from .models import Student, CoffeeShop, Visit, Review
from datetime import date
# Register your models here.
admin.site.register(Student)
admin.site.register(CoffeeShop)
admin.site.register(Visit)
admin.site.register(Review)

#Student rows
student1 = Student.objects.create(first_name='Abby', last_name='Circe', campus_address='123 University Street', major='Information Sciences')
student2 = Student.objects.create(first_name='Mary', last_name='Brown', campus_address='456 Main Street', major='Psychology')
student3 = Student.objects.create(first_name='John', last_name='Smith', campus_address='789 College Road', major='Math')
student4 = Student.objects.create(first_name='Olivia', last_name='Johnson', campus_address='453 Illini Way', major='Chemistry')
student5 = Student.objects.create(first_name='Nate', last_name='Barnes', campus_address='213 Alma Drive', major='English')

#Coffee Shop Rows
shop1 = CoffeeShop.objects.create(name='Cafe Paradiso', location='East Campus', capacity=100)
shop2 = CoffeeShop.objects.create(name='Espresso Royale', location='South Campus', capacity=100)
shop3 = CoffeeShop.objects.create(name='Brewlab', location='Central Campus', capacity=50)

#Visit Rows
visit1 = Visit.objects.create(student=student1, shop=shop1, visit_date=date(2025, 9, 10), study_duration=120)
visit2 = Visit.objects.create(student=student2, shop=shop2, visit_date=date(2025, 9, 11), study_duration=60)
visit3 = Visit.objects.create(student=student3, shop=shop3, visit_date=date(2025, 9, 12), study_duration=120)

#Review Rows
Review.objects.create(visit=visit1, rating=5, comment="I had a great time studying here!")
Review.objects.create(visit=visit2, rating=4, comment="The coffee was great and there was some seating open.")
Review.objects.create(visit=visit3, rating=3, comment="It was louder in the shop today.")
