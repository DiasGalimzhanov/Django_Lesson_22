from django.urls import path
from .views import *

urlpatterns = [
    path('', ListCar.as_view(),name='home'),
    path('<int:pk>/', DetailCar.as_view(), name='detail'),
    path('create/', CreateCar.as_view(), name='create'),
    path('update/<int:pk>/', UpdateCar.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteCar.as_view(), name='delete'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

]