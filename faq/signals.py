from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FAQ
from googletrans import Translator

@receiver(post_save, sender=FAQ)
def translate_faq(sender, instance, **kwargs):
    translator = Translator()
    if not instance.question_hi:
        instance.question_hi = translator.translate(instance.question, dest='hi').text
    if not instance.question_bn:
        instance.question_bn = translator.translate(instance.question, dest='bn').text
    if not instance.answer_hi:
        instance.answer_hi = translator.translate(instance.answer, dest='hi').text
    if not instance.answer_bn:
        instance.answer_bn = translator.translate(instance.answer, dest='bn').text
    instance.save()