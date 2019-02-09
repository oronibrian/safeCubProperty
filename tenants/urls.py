from django.urls import path
from . import views

urlpatterns = [

    path('', views.tenants, name="tenants"),
    path('tenant-cashflows/<int:tenant_id>/',
        views.tenant_cashflows, name="tenant_cashflows"),
]