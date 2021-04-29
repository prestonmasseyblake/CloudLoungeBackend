from django.urls import include, path, re_path
from allauth.account.views import confirm_email
urlpatterns = [
path('auth/', include('rest_auth.urls')),    
path('auth/register/', include('rest_auth.registration.urls')),    
re_path(r'^api/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]