# -- coding: utf-8 --
from django.db import models

from django.core.urlresolvers import reverse

class Company(models.Model):
    """ A company """
    name = models.CharField(max_length=300)
    website = models.URLField(max_length=200, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company',args=[self.id])

class Customer(models.Model):
    """ A client"""
    name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    company = models.ForeignKey(Company, blank=True,null=True, related_name='employees')
    age = models.IntegerField(blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True)

    def __unicode__(self):
        return self.name

KIND_CHOICES = (
    (1,u'Teléfono'),
    (2,u'Correo Electrónico'),
)

class Interaction(models.Model):
    """An interaction is something that happens between a
    customer and you :)
    """
    when = models.DateTimeField(auto_now_add=True)
    kind = models.IntegerField(choices=KIND_CHOICES)
    customer = models.ForeignKey(Customer)
    what = models.TextField(blank=True)

# Create your models here.
