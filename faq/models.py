from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.question

    def get_translated_text(self, field, lang):
        # Check if translation exists in cache
        cache_key = f"{self.id}_{field}_{lang}"
        cached_value = cache.get(cache_key)
        if cached_value:
            return cached_value

        # If not, translate and cache the result
        translator = Translator()
        original_text = getattr(self, field)
        try:
            translated_text = translator.translate(original_text, dest=lang).text
            cache.set(cache_key, translated_text, timeout=60 * 60)  # Cache for 1 hour
            return translated_text
        except Exception as e:
            # Fallback to English if translation fails
            return original_text

    def get_question(self, lang='en'):
        if lang == 'en':
            return self.question
        return self.get_translated_text(f'question_{lang}', lang)

    def get_answer(self, lang='en'):
        if lang == 'en':
            return self.answer
        return self.get_translated_text(f'answer_{lang}', lang)