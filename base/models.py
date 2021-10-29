
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
# this is tobe comment kane added this
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.dispatch.dispatcher import receiver
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.db.models.signals import post_save


# class CustomUserManager(UserManager):
#     def create_user(self, username, email, password, **extra_fields):
#         if not email:
#             raise ValueError('email already in use')
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username,
#                           password=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, username, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError("staff must be set True")

#         extra_fields.setdefault('is_superuser', True)
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError("superuser must be set True")
#         return self.create_user(username, email, password, **extra_fields)


# class customUser(AbstractBaseUser, PermissionsMixin):

#     email = models.EmailField(_('email address'), unique=True)
#     username = models.CharField(_('username'), unique=True, max_length=30)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
#     is_active = models.BooleanField(_('active'), default=True)
#     is_staff = models.BooleanField(_('staff'), default=False)
#     is_superuser = models.BooleanField(_('superuser'), default=False)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

#     objects = CustomUserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

#     class Meta:

#         verbose_name = _('custom user')
#         verbose_name_plural = _('custom users')

#     def get_full_name(self):
#         '''
#         Returns the first_name plus the last_name, with a space in between.
#         '''
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         '''
#         Returns the short name for the user.
#         '''
#         return self.first_name

#     def email_user(self, subject, message, from_email=None, **kwargs):
#         '''
#         Sends an email to this User.
#         '''
#         send_mail(subject, message, from_email, [self.email], **kwargs)


class InterestMsg(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=500)
    read = models.BooleanField(_('Read'), default=False)
    replied = models.BooleanField(_('Replied'), default=False)

    class Meta:
        managed = True
        verbose_name = 'InterestMsg'
        verbose_name_plural = 'InterestMsg'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


@receiver(post_save, sender=InterestMsg)
def send_rcv_mail(created, sender, instance, *args, **kwargs):
    if created:
        send_mail(
            'Oakciti', 'Thank you for Showing interest ! Your message is being read and we will get back to you pretty soon',
            'oakcitigroup@gmail.com', [str(instance.email)], fail_silently=False)
        print(instance.email)
