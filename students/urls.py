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
    CoffeeVisitAPI,
    visits_chart_png,
    api_ping_jsonresponse,
    api_ping_httpresponse,
    visits_chart_view,
    MapNow,
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
    path("charts/visits.png", visits_chart_png, name="visits_chart_png"),
    path("charts/visits/", visits_chart_view, name="visits_chart_view"),
    path("api/ping/json/", api_ping_jsonresponse, name="visits_ping_jsonresponse"),
    path("api/ping/http/", api_ping_httpresponse, name="visits_ping_httpresponse"),
    path("api/map/", MapNow.as_view(), name="map"),

]