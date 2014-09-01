from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from userena.forms import AuthenticationForm, SignupForm
from account.models import Profile

form_singin = AuthenticationForm
form_sginup = SignupForm


class LoginView(TemplateView):
    template_name = 'vtregister/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['form'] = form_singin()
        return context


class RegisterView(TemplateView):
    template_name = 'vtregister/register.html'

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['form'] = form_sginup()
        return context


def profile_view(request, username):
    template = 'vtregister/profile.html'
    user = get_object_or_404(Profile, user__username=username)
    
    return TemplateResponse(request, template, {'user': user})