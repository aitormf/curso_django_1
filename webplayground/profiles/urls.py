from django.urls import path
from .views import ProfileListView, ProfileDeatilView


profiles_patterns = ([
    path('', ProfileListView.as_view(), name='list'),
    path('<username>/', ProfileDeatilView.as_view(), name='detail'),
], 'profiles')