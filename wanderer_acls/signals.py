# Standard Library
import logging

# Django
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed, post_save, pre_delete
from django.dispatch import receiver

# Alliance Auth
from allianceauth import hooks
from allianceauth.authentication.models import CharacterOwnership, UserProfile

# signals go here
logger = logging.getLogger(__name__)


@receiver(m2m_changed, sender=User.groups.through)
def group_trigger(sender, instance, **kwargs):
    try:
        if isinstance(instance, User):
            _update_user_acls(instance)
    except Exception:
        logger.exception(
            f"Could not process update, expected User got {type(instance)}"
        )


@receiver(post_save, sender=CharacterOwnership)
def char_trigger(sender, instance, **kwargs):
    _update_user_acls(instance.user)


@receiver(post_save, sender=UserProfile)
def state_trigger(sender, instance, **kwargs):
    _update_user_acls(instance.user)


def _update_user_acls(user: User):
    #todo queue celery tasks for updating each affected ACL
    pass