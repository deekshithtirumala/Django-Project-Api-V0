from rest_framework import routers
from .viewsets import ResponseViewSet
from django.urls import path
from . import views
router = routers.SimpleRouter()
router.register(r'api', ResponseViewSet)

#no url pattern for now
#to add urlpatterns = []
#urlpatterns += router.urls

#or include('router.url') <- also works

urlpatterns = [
    path("", views.home, name="home"),
]
urlpatterns+=router.urls