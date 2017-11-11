from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from ..serializers import UserSerializer, GroupSerializer, ContactSerializer, TagSerializer
from ..models import Contact, Tag



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().select_related('user')
    serializer_class = ContactSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'tags', TagViewSet)
router.register(r'contacts', ContactViewSet)

