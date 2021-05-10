from create import views
from django.urls import path
from .views import LoungeView, LoungeLookupView, LoungePageView, LoungePageUpdateView, SearchPage, LoungePageDetailUpdateView
urlpatterns = [
    path('lounges',LoungeView.as_view({'get': 'list', 'post': 'create'})),
    path('edit/<slug>',LoungePageView.as_view()),
    path('update/<slug>',LoungePageUpdateView.as_view()),
    path('<slug>',LoungeLookupView.as_view({'get':'list'})),
    path('search/<str:q>', SearchPage.as_view()),
    path('pageDetailUpdate/<slug>',LoungePageDetailUpdateView.as_view())
]
