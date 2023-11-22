
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name = "index"),
    path("home", home, name = "home"),
    path("data", data, name = "data"),
    path("prediction", prediction, name = "prediction"),
    path("accuracy", accuracy, name = "accuracy"),
]


# urlpatterns += static(settings.)

