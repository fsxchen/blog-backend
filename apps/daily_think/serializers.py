from rest_framework import serializers

from .models import DailyThink

class DailyThinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyThink
        fields = ('content', 'author', 'add_time', 'update_time')