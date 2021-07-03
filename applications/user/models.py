from django.db import models
from django.contrib.auth.models import  AbstractUser,Group
# Create your models here.



class User(AbstractUser):
    """Model definition for User."""

    # TODO: Define fields here
    groups=models.ForeignKey(Group,on_delete=models.CASCADE)
    email=models.EmailField( max_length=50,unique=True)
    
    REQUIRED_FIELDS = ['groups_id', 'email']

    class Meta:
        """Meta definition for User."""

        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
            return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username