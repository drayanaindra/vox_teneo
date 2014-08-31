from django.views.generic import TemplateView
from userena.forms import AuthenticationForm, SignupForm

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