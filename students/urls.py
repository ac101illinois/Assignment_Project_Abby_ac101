from django.contrib import admin
from django.urls import path
from .views import (
    student_list_view,
    coffeeshop_list_render,
    VisitListView,
    StudentBaseView,
    ReviewListView,
    StudentDetailView,
    analytics,
    student_visits_chart,
    ReviewCreateView,
    review_view,
    api_visits,
    CoffeeVisitAPI
)

app_name = "students"

urlpatterns = [
    path("studentlist", student_list_view, name="student-list"),
    path("coffeeshops/", coffeeshop_list_render, name="coffeeshop-list"),
    path("visits/", VisitListView.as_view(), name="visit-list"),
    path("base/", StudentBaseView.as_view(), name="student-base"),
    path("reviews/", ReviewListView.as_view(), name="review-list"),
    path("<int:primary_key>/", StudentDetailView.as_view(), name="student-detail"),
    path("analytics/", analytics, name="analytics_page"),
    path("charts/student_visits.png", student_visits_chart, name="student_visits_chart"),
    path("reviews/add/cbv", ReviewCreateView.as_view(), name="review-add-cbv"),
    path("reviews/add/fbv", review_view, name="review-add-fbv"),
    path("api/visits/", api_visits, name="visits_api"),
    path("api/shops/visits/", CoffeeVisitAPI.as_view(), name="coffee_shop_visit_api"),

]