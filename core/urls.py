from django.urls import path

from core import views

urlpatterns = [
    path("search_docs/", views.search_docs, name="search-docs"),
]
