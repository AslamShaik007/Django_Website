from django.contrib import admin
from .models import (
    KickStart,
    ContactUs,
    Subscribe,
    Webinars_table,
    LiveDemo,
    Partner_Program,
    Feedback_table,
    Careers_table,
    Ebook_Download,
    Whitepaper_Download,
    Ebook_pdf,
    Whitepaper_pdf,
    VoIPServices,
    Podcast,
    QRcode,
    DynamicQrCode,
    Get_Quote,
    Request_Demo_Now,
    setup_plans
)


class DynamicQrCodeAdmin(admin.ModelAdmin):
    list_display = ['Base_url','Redirect_to']

admin.site.register(DynamicQrCode,DynamicQrCodeAdmin)



class QRcodeAdmin(admin.ModelAdmin):
    list_display = ["link",]
admin.site.register(QRcode, QRcodeAdmin)


class KickStartAdmin(admin.ModelAdmin):
    list_display = [
        "First_Name",
        "Last_Name",
        "Email_Id",
        "Phone_No",
        "Company",
        "Size_Of_Company",
        "How_You_Know_Us",
        "Submitted_on",
    ]


admin.site.register(KickStart, KickStartAdmin)


# ContactUs model registration
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        "Name",
        "Organization_Name",
        "Mobile",
        "Email",
        "Message",
        "HowYouKnow",
        "Whom_to_send",
        "Submitted_on",
    ]


admin.site.register(ContactUs, ContactUsAdmin)


# Subscribe model registration
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ["NewsLetterEmail", "Submitted_on"]


admin.site.register(Subscribe, SubscribeAdmin)


# Webinars model registration
class WWebinars_tableAdmin(admin.ModelAdmin):
    list_display = ["Name", "Email", "CompanyName", "Submitted_on"]


admin.site.register(Webinars_table, WWebinars_tableAdmin)


# LiveDemo model registration
class LiveDemoAdmin(admin.ModelAdmin):
    list_display = [
        "Date",
        "Time",
        "CompanyName",
        "No_of_users",
        "FullName",
        "Designation",
        "Email",
        "Phone",
        "WhereDidYouHear",
        "Submitted_on",
    ]


admin.site.register(LiveDemo, LiveDemoAdmin)


# Partner_Program model registration
class Partner_ProgramAdmin(admin.ModelAdmin):
    list_display = [
        "FirstName",
        "LastName",
        "Company",
        "State",
        "Email",
        "Phone",
        "Submitted_on",
    ]


admin.site.register(Partner_Program, Partner_ProgramAdmin)


# Feedback_table model registration
class Feedback_tableAdmin(admin.ModelAdmin):
    list_display = [
        "QualityService",
        "CustomerService",
        "CompanyName",
        "Email",
        "Suggestion",
        "Submitted_on",
    ]


admin.site.register(Feedback_table, Feedback_tableAdmin)


# Careers_table model registration
class Careers_tableAdmin(admin.ModelAdmin):
    list_display = [
        "Name",
        "Email",
        "Phone",
        "Experience",
        "Message",
        "Resume",
        "Submitted_on",
    ]


admin.site.register(Careers_table, Careers_tableAdmin)


# E-Book  model registration
class Ebook_DownloadAdmin(admin.ModelAdmin):
    list_display = ["Name", "Mobile", "CompanyName", "Email", "submitted_on"]


admin.site.register(Ebook_Download, Ebook_DownloadAdmin)


# WhitePaper model registration
class Whitepaper_DownloadAdmin(admin.ModelAdmin):
    list_display = ["Name", "Mobile", "CompanyName", "Email", "submitted_on"]


admin.site.register(Whitepaper_Download, Whitepaper_DownloadAdmin)


class Ebook_pdfAdmin(admin.ModelAdmin):
    list_display = [
        "enumber",
        "ebook_pdf",
        "ebook_image",
        "title",
        "description",
        "perma_link",
        "alt",
    ]


admin.site.register(Ebook_pdf, Ebook_pdfAdmin)


class Whitepaper_pdfAdmin(admin.ModelAdmin):
    list_display = [
        "wnumber",
        "whitepaper_pdf",
        "whitepaper_image",
        "title",
        "description",
        "perma_link",
        "alt",
    ]


admin.site.register(Whitepaper_pdf, Whitepaper_pdfAdmin)


# VoIp Services Model Registration
class VoIPServicesAdmin(admin.ModelAdmin):
    list_display = [
        "First_Name",
        "Last_Name",
        "Email_Id",
        "Phone_No",
        "Company",
        "Size_Of_Company",
        "How_You_Know_Us",
        "Submitted_on",
    ]


admin.site.register(VoIPServices, VoIPServicesAdmin)


class PodcastAdmin(admin.ModelAdmin):
    list_display = ["podcast_link"]


admin.site.register(Podcast, PodcastAdmin)


class Get_QuoteAdmin(admin.ModelAdmin):
    list_display = [
        "Name",
        "phonenumber",
        "Email_Id",
        "CompanyName",
        "Created_On",
        "Modified_On",
    ]


admin.site.register(Get_Quote, Get_QuoteAdmin)


class Request_Demo_NowAdmin(admin.ModelAdmin):
    list_display = [
        "Selected_date",
        "Time",
        "Email_Id",
        "Created_On",
        "Modified_On",
    ]


admin.site.register(Request_Demo_Now, Request_Demo_NowAdmin)




admin.site.register(setup_plans)