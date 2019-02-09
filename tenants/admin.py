from django.contrib import admin

from tenants.models import Tenant,Reminder,Payment,RentRevision



for model in [Tenant,Reminder,Payment,RentRevision]:
    admin.site.register(model)