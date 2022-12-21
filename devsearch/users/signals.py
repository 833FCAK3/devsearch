from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from users.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender: User, instance: User, created: bool, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user, username=user.username, email=user.email, name=user.first_name
        )


@receiver(post_delete, sender=Profile)
def delete_user(sender: Profile, instance: Profile, **kwargs):
    user = instance.user
    user.delete()


# post_save.connect(profile_updated, sender=Profile)
# post_delete.connect(delete_user, sender=Profile)
