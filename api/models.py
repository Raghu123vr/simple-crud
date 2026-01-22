from django.db import models

# Create your models here.
class Restapi(models.Model):
    id=models.BigAutoField(primary_key=True)
    company_name=models.CharField(max_length=50,blank=False, 
        null=False)
    email_id=models.CharField(max_length=50,unique=True)
    company_code=models.CharField(max_length=50,unique=True,blank=True,null=True, help_text="Format: 2 alphabets, 2 numbers, ends with E or N (e.g., AB12E)",
)
    strength=models.PositiveBigIntegerField(null=True,blank=True)
    website=models.CharField(max_length=50)
    created_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

