from django.db import models

# Model for Creers-model
class Careers_table(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=50)
    Experience = models.CharField(max_length=50)
    Message = models.CharField(max_length=300)
    Resume = models.FileField(upload_to="")
    # JobOrderID = models.CharField(max_length=50)
    Submitted_on = models.DateTimeField(auto_now=True)


# Model for ContactUs model
class ContactUs(models.Model):
    Name = models.CharField(max_length=60)
    Organization_Name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Message = models.CharField(max_length=500)
    Submitted_on = models.DateTimeField(null=True)
    # userinfo=models.CharField(max_length=500)

#model for E_Book form
class Ebook_Download(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=20,null=True)
    CompanyName=models.CharField(max_length=50,null=True)
    Email = models.EmailField(max_length=50)
    submitted_on = models.DateTimeField(null=True)   

#model form WhitePapers form
class Whitepaper_Download(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=20,null=True)
    CompanyName=models.CharField(max_length=50,null=True)
    Email = models.EmailField(max_length=50)
    submitted_on = models.DateTimeField(null=True) 

class Ebook_pdf(models.Model):
    enumber=models.IntegerField(null=True,unique=True)
    ebook_pdf=models.FileField(upload_to='static/assets/E-Books/')
    ebook_image=models.FileField(upload_to='static/assets/E-Books/images/')
    title=models.CharField(max_length=100)
    perma_link = models.CharField(max_length=100,null=True,blank=True)
    alt = models.CharField(max_length = 100,default="Ebook",null=True,blank=True)
    keyword = models.CharField(max_length = 256,default="spgamerica",null=True,blank=True)
    paragraph = models.CharField(max_length = 256,null=True,blank=True)

class Whitepaper_pdf(models.Model):
    wnumber=models.IntegerField(null=True,unique=True)
    whitepaper_pdf=models.FileField(upload_to='static/assets/Whitepapers/')
    whitepaper_image=models.FileField(upload_to='static/assets/Whitepapers/images/')
    title=models.CharField(max_length=100)
    perma_link = models.CharField(max_length=100,null=True,blank=True)
    alt = models.CharField(max_length = 100,default="Ebook",null=True,blank=True)
    keyword = models.CharField(max_length = 256,default="spgamerica",null=True,blank=True)
    paragraph = models.CharField(max_length = 256,null=True,blank=True)


#model for Subscribe
class Subscribe(models.Model):
    NewsLetterEmail = models.EmailField(max_length=60)
    Submitted_on=models.DateTimeField(null=True)


class Podcast(models.Model):
    purl=models.CharField(max_length=1000)
    pnumber=models.IntegerField(null=False, blank=False)