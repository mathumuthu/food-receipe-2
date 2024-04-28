# serializers.py
from rest_framework import serializers
from .models import FoodRecipe

class FoodRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRecipe
        fields = '__all__'

    def validate_name(self, value):
        if self.instance and FoodRecipe.objects.exclude(id=self.instance.id).filter(name=value).exists():
            raise serializers.ValidationError("A recipe with this name already exists.")
        return value
