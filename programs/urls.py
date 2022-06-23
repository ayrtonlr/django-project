from django.urls import path

from .views import ProgramListView

urlpatterns = [
    path('', ProgramListView.as_view(), name="programs_list"),
]