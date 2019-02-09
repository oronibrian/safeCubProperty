from django.contrib import admin
from property.models import property_location,PropertyType,Property,PropertyFile




for model in [property_location, PropertyType, Property,PropertyFile]:
    admin.site.register(model)

