from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(["GET"])
def get_books_from_api(request):
    query = request.GET.get("q", "python")  # default search
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"

    response = requests.get(url)
    data = response.json()

    books = []

    if "items" in data:
        for item in data["items"]:
            info = item.get("volumeInfo", {})
            books.append({
                "title": info.get("title", "No Title"),
                "authors": info.get("authors", ["Unknown"]),
                "published_date": info.get("publishedDate", "NA"),
                "description": info.get("description", "No Description"),
            })

    return Response({"results": books})

def dashboard(request):
    return render(request, 'index.html')