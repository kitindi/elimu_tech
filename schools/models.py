from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class School(models.Model):
    CAT_CHOICES = (
        ("NECTA School", "NECTA School"),
        ("Cambridge International School", "Cambridge International School"),
        ("International Baccalaureate® (IB)", "International Baccalaureate® (IB)"),
    )

    school_name = models.CharField(max_length=125)
    address_city = models.CharField(max_length=125)
    email_address = models.EmailField(max_length=225)
    post_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=125)
    category = models.CharField(max_length=255, choices=CAT_CHOICES)
    company_sizes = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField(default="default.png")
    school_logo = models.ImageField(default="default.png")
    website_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return self.school_name


class Newsletter(models.Model):
    email_address = models.EmailField(max_length=225)

    def __str__(self):
        return self.email_address


class Job(models.Model):
    JOB_TYPE = (
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
        ("Intenship", "Intenship"),
    )
    JOB_INDUSTRY = (
        ("Advertising and Marketing", "Advertising and Marketing"),
        (" Aerospace", " Aerospace"),
        ("Agriculture", "Agriculture"),
        ("Computer and Technology", "Computer and Technology"),
        ("Construction", "Construction"),
        ("Education", "Education"),
        ("Energy", "Energy"),
        ("Entertainment", "Entertainment"),
        (" Fashion", " Fashion"),
        ("Finance and Economic", "Finance and Economic"),
        ("Food and Beverage", "Food and Beverage"),
        ("Health care", "Health care"),
        ("Hospitality", "Hospitality"),
        ("Manufacturing", "Manufacturing"),
        ("Media and news", "Media and news"),
        ("Mining", "Mining"),
        ("Pharmaceutical", "Pharmaceutical"),
        ("Telecommunication", "Telecommunication"),
        ("Transportation", "Transportation"),
    )
    title = models.CharField(max_length=225)
    job_type = models.CharField(max_length=225, choices=JOB_TYPE)
    posted_on = models.DateTimeField(auto_now_add=True, blank=True)
    company_summary = models.TextField()
    industry = models.CharField(max_length=225, choices=JOB_INDUSTRY)
    company_name = models.CharField(max_length=255)
    submit_before = models.CharField(max_length=255)
    image = models.ImageField()
    description = CKEditor5Field("Text", config_name="extends")
    location = models.CharField(max_length=225)
    componay_url = models.URLField(blank=True)

    class Meta:
        ordering = ["-posted_on"]
