from rest_framework import routers
from django.urls import path, include
from .views import (
    TodosViewSet,
    Signin,
    Signup,
    Logout
)


router = routers.DefaultRouter()
router.register(r'todos', TodosViewSet, basename='todos')

urlpatterns = [
    path('signin/', Signin.as_view()),
    path('signup/', Signup.as_view()),
    path('logout/', Logout.as_view()),
    path('', include(router.urls))
]
