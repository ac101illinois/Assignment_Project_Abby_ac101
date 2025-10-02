from django.contrib import admin
from django.urls import path

from students.views import (student_list_view, coffeeshop_list_render, VisitListView, StudentBaseView,
                            ReviewListView, StudentDetailView)

app_name = "students"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', student_list_view),
    path('coffeeshops/', coffeeshop_list_render),
    path('visits/', VisitListView.as_view(), name='visit_list'),
    path('students/base/', StudentBaseView.as_view(), name='student-base'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('students/<int:primary_key>/', StudentDetailView.as_view(), name='student-detail'),
]

