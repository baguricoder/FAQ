from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        lang = self.context['request'].query_params.get('lang', 'en')
        data['question'] = instance.get_question(lang)
        data['answer'] = instance.get_answer(lang)
        return data