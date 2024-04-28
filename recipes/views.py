# views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import FoodRecipe
from .serializers import FoodRecipeSerializer

class FoodRecipePatchAPIView(generics.UpdateAPIView):
    queryset = FoodRecipe.objects.all()
    serializer_class = FoodRecipeSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class FoodRecipeListAPIView(generics.ListAPIView):
    queryset = FoodRecipe.objects.all()
    serializer_class = FoodRecipeSerializer
