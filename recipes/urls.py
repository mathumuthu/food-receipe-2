# urls.py
from django.urls import path
from .views import FoodRecipePatchAPIView, FoodRecipeListAPIView

urlpatterns = [
    path('recipes/', FoodRecipeListAPIView.as_view(), name='foodrecipe-list'),
    path('recipes/<int:pk>/', FoodRecipePatchAPIView.as_view(), name='foodrecipe-patch'),
]
