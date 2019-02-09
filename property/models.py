from django.db import models
from django.db.models import Max
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, ValidationError
from datetime import date
from calendar import monthrange
from collections import namedtuple, deque
import itertools
from operator import attrgetter
from django.forms import Textarea
from decimal import Decimal


class property_location(models.Model):
	name = models.CharField(_("name"), max_length=255)

	class Meta:
	    verbose_name = _("Property Location")
	    verbose_name_plural = _("Property Locations")
	    ordering = ['name']

	def __str__(self):
	    return self.name


class PropertyType(models.Model):
    name = models.CharField(_("name"), max_length=255)
    notes = models.TextField(_("notes"), blank=True)

    class Meta:
        verbose_name = _("Property Type")
        verbose_name_plural = _("Property Types")
        ordering = ['name']

    def __str__(self):
        return self.name

    def property_count(self):
        return self.property_set.count()

    property_count.short_description = _("number of properties")



class Property(models.Model):
    name = models.CharField(_("name"), max_length=255)
    prop_type=models.ForeignKey(PropertyType,on_delete=models.PROTECT)
    location = models.ForeignKey(
        property_location,
        verbose_name=property_location._meta.verbose_name,
        blank=True, null=True, on_delete=models.PROTECT)

    address = models.TextField(_("address"))
    notes = models.TextField(_("notes"), blank=True)
    area = models.DecimalField(
        _("surface area"), max_digits=7, decimal_places=2,
        validators=[MinValueValidator(0)])
    rooms = models.DecimalField(
        _("number of rooms"), max_digits=2, decimal_places=0,
        validators=[MinValueValidator(1)])

    price=models.DecimalField(max_digits=7, decimal_places=2,
        validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = _("property")
        verbose_name_plural = _("properties")
        ordering = ['name']

    def __str__(self):
        return u'{}\n{}'.format(self.name, self.address)


class PropertyFile(models.Model):
    property = models.ForeignKey(
        Property, verbose_name=Property._meta.verbose_name,on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=255)
    file = models.FileField(_('file'), upload_to='property/docs')

    class Meta:
        verbose_name = _("Property file")
        verbose_name_plural = _("Property files")

    def __str__(self):
        return self.name