from django.shortcuts import render
from .models import Person

def home(request):
  people = Person.objects.all()
  return render(request, "index.html", {"people": people})
