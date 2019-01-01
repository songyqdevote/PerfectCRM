
from django.urls import path
from crm import views
urlpatterns = [
    path('', views.index, name="sales_index"),
    path('customers/', views.customer_list, name="customer_list"),
]