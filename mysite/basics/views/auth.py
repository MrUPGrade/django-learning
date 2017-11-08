from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse


class MyLoginView(LoginView):
    template_name = 'basics/auth/login.html'


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('basics:index'))
