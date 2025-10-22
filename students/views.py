from django.contrib.admindocs.views import ViewDetailView
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.db.models import Count

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from io import BytesIO

from .models import Student, CoffeeShop, Visit, Review
from .forms import ReviewForm


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

def review_view(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("Name:", data["name"], "Review:", data["review"])
    else:
        form = ReviewForm()

    return render(request, "students/review.html", {"form": form})
