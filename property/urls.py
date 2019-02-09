from django.urls import path
from . import views

urlpatterns = [

    path('', views.property_view, name="property"),
    # path('property/<int:tenant_id>/',
    #     views.tenant_cashflows, name="property_single"),
]
