from django.shortcuts import render
from registration.models import Profile
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

# Create your views here.

class ProfileListView(ListView):
    model = Profile
    paginate_by = 3  # if pagination is desired
    template_name = 'profiles/profile_list.html'

class ProfileDeatilView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
         return get_object_or_404(Profile, user__username=self.kwargs['username'])
