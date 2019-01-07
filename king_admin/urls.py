
from django.urls import path
from king_admin import views
urlpatterns = [
    path('', views.index, name="table_index"),

]