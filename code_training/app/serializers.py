from rest_framework import serializers

from .models import Decision
from .tasks import check_cache_result


class DecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decision
        fields = ['id', 'text', 'status', 'created_at']
        extra_kwargs = {'status': {'read_only': True}}

    def create(self, validated_data):
        decision = Decision(text=validated_data['text'])
        # проверяем в кеше решение и если есть, то задаем статус решения
        status = check_cache_result(decision.text)
        if status:
            decision.status = getattr(Decision, status)
        decision.save()
        return decision
