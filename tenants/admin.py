from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# from django.core import urlresolvers
from django.urls import reverse


from django.utils.html import format_html
from django.utils.safestring import mark_safe


from tenants.models import (Tenant,
	Reminder,
	Payment,
	RentRevision,
	TenantFile,
	Refund,
	Fee,
	Invoice,
	Discount)



class RentRevisionInline(admin.TabularInline):
    model = RentRevision
    extra = 1


class TenantFileInline(admin.TabularInline):
    model = TenantFile
    extra = 1


class PaymentInline(admin.TabularInline):
    model = Payment


class RefundInline(admin.TabularInline):
    model = Refund

class FeeInline(admin.TabularInline):
    model = Fee
    extra = 1


class DiscountInline(admin.TabularInline):
    model = Discount
    extra = 1


class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance')
    inlines = [
        RentRevisionInline,
        FeeInline,
        DiscountInline,
        TenantFileInline,
        PaymentInline,
        RefundInline,
    ]
    readonly_fields = ('property_link', 'balance',)

    def property_link(self, obj):
        url = reverse(
            'admin:property_property_change', args=(obj.property.id,))
        return format_html(u'<a href={}>{}</a>', mark_safe(url), obj.property)
    property_link.short_description = _('link to the property')



# This is a hack to have 2 displays for the tenants
class TenantReminders(Tenant):
    class Meta:
        proxy = True
        verbose_name = _("tenant reminder list")
        verbose_name_plural = _("tenants reminder lists")


class ReminderInline(admin.TabularInline):
    fields = ['date', 'read', 'text']
    model = Reminder
    extra = 1


class TenantRemindersAdmin(admin.ModelAdmin):
    fields = ('name', 'property')
    readonly_fields = ('name', 'property')
    inlines = [
        ReminderInline,
    ]

admin.site.register(Tenant,TenantAdmin)
admin.site.register(TenantReminders, TenantRemindersAdmin)
admin.site.register(Reminder)
admin.site.register(Invoice)














