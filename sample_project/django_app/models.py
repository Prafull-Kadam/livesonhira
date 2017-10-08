from django.db import models
# Create your models here.
class profile(models.Model):
    id         = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    city       = models.CharField(max_length=30)
    taluka     = models.CharField(max_length=30)
    district   = models.CharField(max_length=30)
    message    = models.TextField(null=True, blank=True)
    picture    = models.TextField(null=True,blank=True)
    mobile_no  = models.CharField('mobile phone', max_length=10)
    email      = models.EmailField('email address')
    created_on = models.DateTimeField('Created On', auto_now_add=True)

    def profile_details(self):
        return {'id'        : self.id,
                'first_name': self.first_name,
                'last_name' : self.last_name,
                'city'      : self.city,
                'taluka'    : self.taluka,
                'district'  : self.district,
                'message'   : self.message,
                'picture'   : self.picture,
                'mobile_no' : self.mobile_no,
                'email'     : self.email}

    class Meta:
        verbose_name        = 'profile'
        verbose_name_plural = 'profiles'

    def get_short_name(self):
        return self.first_name
