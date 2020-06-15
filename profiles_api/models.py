from django.db import models
from django.contrib.auth.models import AbstractBaseUser # overide/custon standard django user
from django.contrib.auth.models import PermissionsMixin # overide/custom standard django user
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""
    
    def create_user(self, email, name, password=None):
        """Create and save new user"""
        
        # sets the domain portion of the email address in lowercase
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)

        # set email and name as user 
        user = self.model(email=email, name=name)

        # set user password with hash 
        user.set_password(password) 
        
        # save to database 
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True 
        user.save(using=self._db)

        return user 


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Custom user model """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #
    objects = UserProfileManager()

    # replace default username field with email (required by default)
    USERNAME_FIELD = 'email'

    # set required fields for user login
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    
    def __str__(self):
        """Return string representation of our user"""
        return self.email 










