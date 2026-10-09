from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("ore/", views.ore, name="ore"), 
    path("cell/", views.cell, name="cell"), 
    path("genetic/", views.genetic, name="genetic"),
    path("gross/", views.gross, name="gross"),
    path("test-py-html/", views.test_py_html, name="test_py_html"),
]
