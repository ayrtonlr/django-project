from django.views.generic import ListView

from .models import Program

class ProgramListView(ListView):
    model = Program