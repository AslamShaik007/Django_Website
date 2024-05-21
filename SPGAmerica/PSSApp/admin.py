from django.contrib import admin
from .models import *

# Register your models here.
class Careers_tableAdmin(admin.ModelAdmin):
    list_display = [
        "Name",
        "Email",
        "Phone",
        "Experience",
        "Message",
        "Resume",
        # "JobOrderID",
        "Submitted_on",
    ]


admin.site.register(Careers_table, Careers_tableAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    # list_display = ["Name", "Organization_Name", "Mobile",'Email','Message','Submitted_on', 'userinfo']
    list_display = [
        "Name",
        "Organization_Name",
        "Mobile",
        "Email",
        "Message",
        "Submitted_on",
    ]


admin.site.register(ContactUs, ContactUsAdmin)

#E-Book  model registration
class Ebook_DownloadAdmin(admin.ModelAdmin):
    list_display = ['Name','Mobile','CompanyName','Email','submitted_on']

admin.site.register(Ebook_Download,Ebook_DownloadAdmin)

#WhitePaper model registration
class Whitepaper_DownloadAdmin(admin.ModelAdmin):
    list_display = ['Name','Mobile','CompanyName','Email','submitted_on']

admin.site.register(Whitepaper_Download,Whitepaper_DownloadAdmin)

class Ebook_pdfAdmin(admin.ModelAdmin):
    list_display=['enumber','ebook_pdf','ebook_image','title','perma_link','alt']
admin.site.register(Ebook_pdf,Ebook_pdfAdmin)

class Whitepaper_pdfAdmin(admin.ModelAdmin):
    list_display=['wnumber','whitepaper_pdf','whitepaper_image','title','perma_link','alt']
admin.site.register(Whitepaper_pdf,Whitepaper_pdfAdmin)

#Subscribe model registration
class SubscribeAdmin(admin.ModelAdmin):
    list_display=['NewsLetterEmail','Submitted_on']

admin.site.register(Subscribe,SubscribeAdmin)

class PodcastAdmin(admin.ModelAdmin):
    list_display=['purl','pnumber']

admin.site.register(Podcast,PodcastAdmin)