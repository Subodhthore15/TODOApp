
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from todoapp.urls import *
urlpatterns = [
    path('admin/', admin.site.urls),

    path('todo/',include('todoapp.urls'))
]
