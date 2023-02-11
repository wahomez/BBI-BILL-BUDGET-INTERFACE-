from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.db.models.signals import post_save

#choices
BUDGET_CHOICE = [
    ("rent" , "rent"), 
     ("fees" , "fees"), 
     ("transport" , "transport"),
     ("personal_use" , "personal_use"),
     ("savings" , "savings"),
]

PAYMENT_CHOICES = [
    ("mpesa" , "mpesa"), 
     ("account" , "account"),
     
]
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    mobile_no = models.CharField(max_length=13, blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True, default=r"C:\Users\Jeff\bbi-env\BBI\static\images\default.png")
    creditcard_no = models.IntegerField(blank=True, null=True)
    income_amount = models.IntegerField(blank=True, null=True)
    income_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    #Create Profile when new User Signs Up
def createProfile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(createProfile, sender=User)
    
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, choices=BUDGET_CHOICE)
    amount = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return str(self.user.username) + " - " + str(self.name)
    
class Bill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="bill")
    payment_method = models.CharField(max_length=200, choices=PAYMENT_CHOICES)
    payment_details = models.TextField()

    def __str__(self):
        return self.budget
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, choices=BUDGET_CHOICE)
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + " - " + str(self.category)