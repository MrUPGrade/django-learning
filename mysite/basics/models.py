from django.db import models
from django.contrib.auth.models import User


class IntrospectionMixin:
    @classmethod
    def field_list(cls, include_hidden=False, exclude=()):
        fields = cls._meta.get_fields(include_hidden=include_hidden)
        return [f.name for f in fields if f.name not in exclude]


class Tag(models.Model, IntrospectionMixin):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Contact(models.Model, IntrospectionMixin):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    profile_pic = models.ImageField(upload_to='profile', blank=True, null=True)

    tags = models.ManyToManyField(Tag, related_name='contacts', blank=True)
    user = models.ForeignKey(User, related_name='contacts')
