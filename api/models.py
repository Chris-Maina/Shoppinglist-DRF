from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    """ Base user manager class """
    def create_user(self, email, username, password=None, is_staff=False,
                    is_active=True, is_superuser=False):
        """
        Creates and saves a User with the given email,username and password.
        """
        if not email:
            raise ValueError("Please provide an email")
        if not password:
            raise ValueError("Please provide a password")
        if not username:
            raise ValueError("Please provide a username")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.staff = is_staff
        user.active = is_active
        user.superuser = is_superuser
        user.save(using=self._db)
        return user

    def create_staff_user(self, email, username, password):
        """ Create a staff user with is_staff set to True, is_superuser False """
        user = self.create_user(email, username, password=password,
                                is_staff=True)
        return  user

    def create_superuser(self, email, username, password):
        """ Create a super user with is_staff set to True, is_superuser=True  """
        user = self.create_user(email, username, password=password,
                                is_staff=True, is_superuser=True)
        return  user

class User(AbstractBaseUser):
    """ Custom user model """
    username = models.CharField(_('username'), max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    staff = models.BooleanField(_('staff'), default=False)
    active = models.BooleanField(_('active'), default=True)
    superuser = models.BooleanField(_('superuser'), default=False)
    date_joined = models.DateTimeField(_('date_joined'), auto_now_add=True)

    objects = UserManager()

    # name of the field on the User model that is used as the unique identifier
    USERNAME_FIELD = 'email'
    # field names that will be prompted for when creating a user via the createsuperuser command
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        """ Display in a human readable manner """
        return "{}".format(self.username)

    def has_perm(self, perm, obj=None):
        """ Define permissions  """
        return True

    def has_module_perms(self, app_label):
        """ Define module permissions  """
        return True

    @property
    def is_staff(self):
        """ Define model property is_staff to use staff """
        return self.staff

    @property
    def is_active(self):
        """ Define model property is_active to use active """
        return self.active
    @property
    def is_superuser(self):
        """ Define model property is_superuser to use superuser """
        return self.superuser
    
    class Meta:
        """ Define verbose names """
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Shoppinglist(models.Model):
    """ Shoppinglist model """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Display in a human readable manner """
        return "{}".format(self.name)

    class Meta:
        """ Define ordering and verbose names """
        verbose_name = _('shoppinglist')
        verbose_name_plural = _('shoppinglists')
        ordering = ['-date_created']
