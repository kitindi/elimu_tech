from django.db import models

# Create your models here.


class School(models.Model):
    CAT_CHOICES = (
        ("TZ", "NECTA School"),
        ("UK", "Cambridge International School"),
        ("IB", "International Baccalaureate® (IB)"),
    )

    school_name = models.CharField(max_length=125)
    address_city = models.CharField(max_length=125)
    email_address = models.EmailField(max_length=225)
    post_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=125)
    category = models.CharField(max_length=255, choices=CAT_CHOICES)
    company_sizes = models.IntegerField()
    description = models.TextField()
    # thumbnail = models.ImageField(upload_to='images/')
    website_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return self.school_name
