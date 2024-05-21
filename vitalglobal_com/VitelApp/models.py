from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
# Model for Kick-Start

# model for Subscribe

class DynamicQrCode(models.Model):
    Base_url = models.CharField(max_length=255)
    Redirect_to = models.CharField(max_length=255)


class QRcode(models.Model):
    link = models.CharField(max_length=255)


class KickStart(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email_Id = models.EmailField(max_length=100)
    Phone_No = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    Size_Of_Company = models.CharField(max_length=10)
    How_You_Know_Us = models.CharField(max_length=100)
    Submitted_on = models.DateTimeField(null=True)
    terms_and_conditions = models.BooleanField(default = False, null=True,blank=True)


# model for VoIP Services
class VoIPServices(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email_Id = models.EmailField(max_length=100)
    Phone_No = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    Size_Of_Company = models.CharField(max_length=10)
    How_You_Know_Us = models.CharField(max_length=100)
    Submitted_on = models.DateTimeField(null=True)


# model for Contact-Us
class ContactUs(models.Model):
    Name = models.CharField(max_length=60)
    Organization_Name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Message = models.CharField(max_length=500)
    HowYouKnow = models.CharField(max_length=500)
    Whom_to_send = models.CharField(max_length=50)
    Submitted_on = models.CharField(max_length=100)
    terms_and_conditions = models.BooleanField(default = False, null=True,blank=True)
    # Submitted_on=models.DateTimeField(null=True)


# model for Subscribe
class Subscribe(models.Model):
    NewsLetterEmail = models.EmailField(max_length=60)
    Submitted_on = models.DateTimeField(null=True)


# model for Webinars
class Webinars_table(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=60)
    CompanyName = models.CharField(max_length=100)
    Submitted_on = models.DateTimeField(null=True)


# model for Live-demo-form
class LiveDemo(models.Model):
    Date = models.DateField()
    Time = models.TimeField()
    CompanyName = models.CharField(max_length=50)
    No_of_users = models.CharField(max_length=50)
    FullName = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=50)
    WhereDidYouHear = models.CharField(max_length=50)
    Submitted_on = models.DateTimeField(null=True)
    terms_and_conditions = models.BooleanField(default = False, null=True,blank=True)


# model for Creers-form
class Careers_table(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=50)
    Experience = models.CharField(max_length=50)
    Message = models.CharField(max_length=300)
    Resume = models.FileField(upload_to="")
    JobOrderID = models.CharField(max_length=50, null = True, blank = True)
    Submitted_on = models.DateTimeField(null=True)


# model for partners-form
class Partner_Program(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=50)
    Submitted_on = models.DateTimeField(null=True)
    terms_and_conditions = models.BooleanField(default = False, null=True,blank=True)


# model for Feedback-form
class Feedback_table(models.Model):
    QualityService = models.CharField(max_length=50)
    CustomerService = models.CharField(max_length=50)
    CompanyName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Suggestion = models.CharField(max_length=300)
    Submitted_on = models.DateTimeField(null=True)


# model for E_Book form
class Ebook_Download(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=20, null=True)
    CompanyName = models.CharField(max_length=50, null=True)
    Email = models.EmailField(max_length=50)
    submitted_on = models.DateTimeField(null=True)


# model form WhitePapers form
class Whitepaper_Download(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=20, null=True)
    CompanyName = models.CharField(max_length=50, null=True)
    Email = models.EmailField(max_length=50)
    submitted_on = models.DateTimeField(null=True)


class Ebook_pdf(models.Model):
    enumber = models.IntegerField(null=True, unique=True)
    ebook_pdf = models.FileField(upload_to="static/assets/E-Books/")
    ebook_image = models.FileField(upload_to="static/assets/E-Books/images/")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    perma_link = models.CharField(max_length=100)
    alt = models.CharField(max_length = 100,default="ebook",null=True,blank=True)
    keyword = models.CharField(max_length = 256,default="Vitelglobal",null=True,blank=True)
    paragraph = models.CharField(max_length = 256,null=True,blank=True)


class Whitepaper_pdf(models.Model):
    wnumber = models.IntegerField(null=True, unique=True)
    whitepaper_pdf = models.FileField(upload_to="static/assets/Whitepapers/")
    whitepaper_image = models.FileField(upload_to="static/assets/Whitepapers/images/")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    perma_link = models.CharField(max_length=100)
    alt = models.CharField(max_length = 100,default="ebook",null=True,blank=True)
    keyword = models.CharField(max_length = 256,default="Vitelglobal",null=True,blank=True)
    paragraph = models.CharField(max_length = 256,null=True,blank=True)


class Podcast(models.Model):
    podcast_link = models.CharField(max_length=500)


class Get_Quote(models.Model):
    Name = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=50)
    Email_Id = models.EmailField(max_length=100)
    CompanyName = models.CharField(max_length=256)
    Created_On = models.DateTimeField(auto_now=False,auto_now_add=True,)
    Modified_On = models.DateTimeField(auto_now=True,auto_now_add=False,)


class Request_Demo_Now(models.Model):
    Selected_date = models.DateField()
    Time = models.TimeField()
    Email_Id = models.EmailField(max_length=100)
    Name = models.CharField(max_length = 100,null=True,blank = True)
    PhoneNumber = models.CharField(max_length = 50,null=True,blank = True)
    Created_On = models.DateTimeField(auto_now=False,auto_now_add=True,)
    Modified_On = models.DateTimeField(auto_now=True,auto_now_add=False,)
    
    
# ------ Viteldevelopment Code ---------
# model for Setup-Plan
class setup_plans(models.Model):
    firstname           = models.CharField(max_length=50)
    lastname            = models.CharField(max_length=50)
    password            = models.CharField(max_length=255)
    email               = models.EmailField(max_length=100)
    mobile              = models.CharField(max_length=100)
    quantity            = models.IntegerField()
    businessname        = models.CharField(max_length=100)
    businessaddress     = models.CharField(max_length=500)  
    Suite               = models.CharField(max_length=100)
    city                = models.CharField(max_length=50)
    zipcode             = models.CharField(max_length=50)
    state               = models.CharField(max_length=50)
    country             = models.CharField(max_length=50)
    dids                = models.CharField(max_length=100)
    submitted_on        = models.DateTimeField(auto_now_add=True)

### Un - Subscribe
class UnsubscribeRequest(models.Model):
    yourname = models.CharField(max_length=100)
    email = models.EmailField()
    phoneno = models.CharField(max_length=56)
    unsubscribe_promotional = models.BooleanField(default=False)
    unsubscribe_notifications = models.BooleanField(default=False)
    unsubscribe_all = models.BooleanField(default=False)
    Created_On = models.DateTimeField(auto_now=False,auto_now_add=True,)
    Modified_On = models.DateTimeField(auto_now=True,auto_now_add=False,)