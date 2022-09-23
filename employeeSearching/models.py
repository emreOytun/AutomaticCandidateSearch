from django.db import models

# Create your models here.

class Candidate(models.Model) : 
    name = models.CharField(max_length = 300, verbose_name = "Name", null = True)
    location = models.CharField(max_length = 300, verbose_name = "Location", null = True)
    email = models.CharField(max_length = 300, verbose_name = "Email", null = True)
    company = models.CharField(max_length = 300, verbose_name = "Company", null = True)
    bio = models.CharField(max_length = 500, verbose_name = "Bio", null = True)
    blog = models.CharField(max_length = 500, verbose_name = "Blog", null = True)
    userHtmlUrl = models.CharField(max_length = 2048, verbose_name = "URL", null = True, unique = True)

    def __str__(self) : 
        return self.name
