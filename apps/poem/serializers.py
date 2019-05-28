from rest_framework import serializers


from .models import (
    Poem, Poet
)


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = '__all__'