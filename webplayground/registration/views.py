from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm, EmailForm


# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    
    def get_form(self, form_class = None):
        form = super(SignUpView, self).get_form(form_class)
        form.fields['username'].widget = forms.TextInput(attrs = {'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs = {'class': 'form-control mb-2', 'placeholder': 'Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs = {'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs = {'class': 'form-control mb-2', 'placeholder': 'Repite la contraeña'})
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    template_name = 'registration/profile_form.html'
    success_url = reverse_lazy('profile')
    def get_object(self):
        profile, created =  Profile.objects.get_or_create(user=self.request.user)
        return profile
    
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    template_name = 'registration/profile_email_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
    
    def get_form(self, form_class = None):
        form = super(EmailUpdate, self).get_form(form_class)
        form.fields['email'].widget = forms.EmailInput(attrs = {'class': 'form-control mb-2', 'placeholder': 'Email'})
        return form