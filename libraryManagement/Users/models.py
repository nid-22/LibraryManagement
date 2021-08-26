from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active=True
        user.is_staff=True
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

        # return self.create_user(email, password, **other_fields)


class Users(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
    )
    Name = models.CharField(max_length=50,null=True, blank=True)
    Address= models.CharField(max_length=100,null=True, blank=True)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    BirthDate = models.DateField(null=True)
    # RoleID = models.ForeignKey(Role, on_delete=models.SET_NULL,  null=True, blank=True)
    Phone = models.CharField(max_length=10,null=True, blank=True )
    CreatedBy = models.ForeignKey('self',on_delete=models.SET_NULL, related_name='UserCreatedBy',null=True, blank=True)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedBy = models.ForeignKey('self',on_delete=models.SET_NULL, related_name='UserUpdatedBy',null=True, blank=True)
    UpdatedOn =  models.DateTimeField(auto_now=True, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.Name)
