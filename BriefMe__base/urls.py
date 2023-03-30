from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('briefme/', include('BriefMe.urls', namespace='BriefMe')),

]
