from django.urls import path

from portfolio.views import all_blogs


urlpatterns = [
    path('', all_blogs, name='all_blogs'),
]
