from django.contrib import admin
from django.urls import path
from .views import create_brief, briefs_list

app_name = 'BriefMe'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('briefs/', briefs_list, name='briefs_list'),
    path('', create_brief, name='create_brief'),
]
