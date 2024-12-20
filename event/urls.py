from django.urls import path
from . import views

app_name = "event"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("edit/<int:event_id>", views.edit, name="edit"),
    path("edit/<int:event_id>/update", views.update, name="update"),
    path("delete/<int:event_id>", views.delete, name="delete"),
    path("date/<int:event_id>/date", views.date, name="date"),
    path("date/<int:event_id>/create", views.create_date, name="create_date"),
    path("choice/<int:choice_id>/delete", views.choice_delete, name="choice_delete"),
]
