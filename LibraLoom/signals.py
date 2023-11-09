# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from .models import Member

@receiver(user_signed_up)
def create_member_profile(sender, user, request, **kwargs):
    member = Member(user=user)
    member.save()
