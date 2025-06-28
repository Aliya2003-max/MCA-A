from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Faculty
from .forms import FacultyForm
# Create your views here.
class FacultyListView(ListView):
    model = Faculty
    template_name = 'faculty_list.html'

class FacultyDetailView(DetailView):
    model = Faculty
    template_name = 'faculty_detail.html'

class FacultyCreateView(CreateView):
    model = Faculty
    form_class = FacultyForm
    template_name = 'faculty_form.html'
    success_url = reverse_lazy('faculty_list')

class FacultyUpdateView(UpdateView):
    model = Faculty
    form_class = FacultyForm
    template_name = 'faculty_form.html'
    success_url = reverse_lazy('faculty_list')

class FacultyDeleteView(DeleteView):
    model = Faculty
    template_name = 'faculty_confirm_delete.html'
    success_url = reverse_lazy('faculty_list')

