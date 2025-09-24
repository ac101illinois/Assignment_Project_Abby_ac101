from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Student, CoffeeShop


#HttpResponse Version
def student_list_view(request):
    student_list_query = Student.objects.all()
    template = loader.get_template('student_list.html')

    context = {'students' : student_list_query}
    output = template.render(context)

    return HttpResponse(output)

#Render Version

def coffeeshop_list_render(request):
    coffeeshops = CoffeeShop.objects.all()
    return render(request, 'coffeeshop_list.html', {'coffeeshops' : coffeeshops})


