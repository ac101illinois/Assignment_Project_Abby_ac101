from django.contrib.admindocs.views import ViewDetailView
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView
from django.db.models import Count

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import io
from io import BytesIO

from .models import Student, CoffeeShop, Visit, Review
from .forms import ReviewForm
from django.urls import reverse
import json
import urllib.request
import requests


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

#List View
class VisitListView(ListView):
    model = Visit
    template_name = "visit_list.html"
    context_object_name = "visit_list"

    def get_queryset(self):
        q = self.request.GET.get("q", "")
        if q:
            return Visit.objects.filter(student__first_name__icontains=q)
        return Visit.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["q"] = self.request.GET.get("q", "")


        ctx["visits_per_student"] = (
            Visit.objects.values("student__first_name", "student__last_name")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

        # Grouping 2: Visits per shop
        ctx["visits_per_shop"] = (
            Visit.objects.values("shop__name")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

        ctx["total_visits"] = Visit.objects.count()
        return ctx

#Base View
class StudentBaseView(View):
    def get(self, request):
        students = Student.objects.all()
        # Render template with context
        return render(request, "student_list.html", {
            "students": students
        })

#Generic View
class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'review_list_html'


#Third View - Detail View
class StudentDetailView(DetailView):
    def get(self, request, primary_key):
        student = get_object_or_404(Student, pk=primary_key)
        visits = student.visit_set.all()  # default related name

        return render(
            request,
            'student_detail.html',
            {
                'student_var_for_looping': student,
                'visits_var_for_looping': visits,
            }
        )


import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

#Chart for visits per each student
def student_visits_chart(request):

    data = (
        Student.objects
        .annotate(visit_count=Count("visit"))
        .order_by("first_name")
    )

    labels = [f"{s.first_name} {s.last_name}" for s in data]
    counts = [s.visit_count for s in data]

    fig, ax = plt.subplots(figsize=(6, 3), dpi=150)

    ax.bar(labels, counts, color="#00b6bd")

    ax.set_title("Coffee Shop Visits per Student", fontsize=10, color="#00b6bd")
    ax.set_xlabel("Student", fontsize=8)
    ax.set_ylabel("Visits", fontsize=8)
    ax.tick_params(axis="x", rotation=45, labelsize=8)
    ax.tick_params(axis="y", labelsize=8)

    fig.tight_layout()

    buf = BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)

    return HttpResponse(buf.getvalue(), content_type="image/png")

def analytics(request):
    visits_per_student = (
        Visit.objects
        .values("student__first_name", "student__last_name")
        .annotate(count=Count("id"))
        .order_by("-count")
    )

    context = {
        "visits_per_student": visits_per_student
    }

    return render(request, "analytics.html", context)

#Assignment 8, Function-based view that handles post and get

def review_view(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("Name:", data["name"], "Review:", data["comment"])
            return redirect("students:review-list")
    else:
        form = ReviewForm()
    return render(request, "add_review.html", {"form": form})


#Assignment 8: Generic class based view
from django.urls import reverse_lazy

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "add_review.html"
    success_url = reverse_lazy('students:review-list')

#Assignment 9: APIs and JSON
from django.http import JsonResponse
from django.db.models import Count, Q


# Function based api view
def api_visits(request):
    visits = Visit.objects.select_related("student", "shop").all()
    data = {
        "count": visits.count(),
        "results": [
            {
                "student": f"{v.student.first_name} {v.student.last_name}",
                "shop": v.shop.name,
                "location": v.shop.location,
                "visit_date": v.visit_date.strftime("%Y-%m-%d"),
                "study_duration": v.study_duration,
            }
            for v in visits
        ],
    }
    return JsonResponse(data)


#class based view
class CoffeeVisitAPI(View):
    def get(self, request):
        data = (
            CoffeeShop.objects.annotate(total_visits=Count("visit", distinct=True))
            .values("shop_id", "name", "location", "total_visits")
            .order_by("-total_visits")
            .distinct()
        )
        return JsonResponse(list(data), safe=False)


# chart view
def visits_chart_png(request):
    api_url = request.build_absolute_uri(reverse("students:coffee_shop_visit_api"))

    with urllib.request.urlopen(api_url) as resp:
        payload = json.load(resp)

    rows = payload

    labels = [r["name"] for r in rows]
    all_counts = [r["total_visits"] for r in rows]

    active_counts = []
    for r in rows:
        shop_id = r["shop_id"]
        long_visits = Visit.objects.filter(shop_id=shop_id, study_duration__gte=60).count()
        active_counts.append(long_visits)

    x = range(len(labels))
    width = 0.4

    fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=150)
    ax.bar([i - width / 2 for i in x], all_counts, width=width, label="All Visits", color="#00b6bd")
    ax.bar([i + width / 2 for i in x], active_counts, width=width, label="Long Visits", color="#d2b48c")

    ax.set_title("Visits per Coffee Shop")
    ax.set_ylabel("Number of Visits")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.legend()
    fig.tight_layout()


    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/png")

def visits_chart_view(request):
    return render(request, "visits_chart.html")

def api_ping_jsonresponse(request):
    return JsonResponse({"ok": True})


def api_ping_httpresponse(request):
    payload = json.dumps({"ok": True})
    payload2 = json.loads(payload)
    return HttpResponse(payload2, content_type="application/json")

class MapNow(View):
    def get(self, request):
        query = request.GET.get("q", "Champaign, IL")
        params = {
            "q": query,
            "format": "json",
            "limit": 1
        }

        try:
            output_raw_all = requests.get(
                "https://nominatim.openstreetmap.org/search",
                params=params,
                timeout=5,
                headers={"User-Agent": "Django-Student-App"}
            )
            output_raw_all.raise_for_status()
            output_polished_all = output_raw_all.json()

            if output_polished_all:
                top_result = output_polished_all[0]
                output_polished_trimmed = {
                    "display_name": top_result.get("display_name"),
                    "lat": top_result.get("lat"),
                    "lon": top_result.get("lon"),
                    "type": top_result.get("type"),
                    "importance": top_result.get("importance"),
                }
            else:
                output_polished_trimmed = {"error": "No location found"}

            return render(
                request,
                "map.html",  # ✅ template path
                {"ok": True, "location": output_polished_trimmed, "query": query}
            )

        except requests.exceptions.RequestException as e:
            return render(
                request,
                "map.html",
                {"ok": False, "error": str(e), "query": query}
            )
