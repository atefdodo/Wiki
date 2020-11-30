from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("search/",views.get_search_query, name="search_results"),
    path("new/",views.new_page, name="create"),
    path("random/",views.random_page, name ="random"),
    path("edit/",views.edit_page, name="edit"),
    path("save/",views.save_page, name="save"),
    path("<str:title>",views.get_page, name="title"),
]
