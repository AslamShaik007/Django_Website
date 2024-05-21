from http.client import HTTPResponse
from xmlrpc.client import ProtocolError
from django.shortcuts import render, redirect
from .models import *
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from requests.packages.urllib3.util.retry import Retry
from PSSProject import settings
from datetime import datetime
import pytz
import random
import os
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from filehandler import SaveResume, doctodocx, FileValidation
import json
from django.core.mail import get_connection, send_mail
from django.http import HttpResponse

Timezone = pytz.timezone("Asia/Kolkata")

# ENDPOINT = 'https://resume.vitelglobal.com/api/test'


# Create your views here.
def Index(request):
    return render(request, "index.html")
def About_Us(request):
    return render(request, "about-us.html")
# ===========FUNCTIONS FOR SERVICES==================
def education(request):
    return render(request, "education.html")

def ar_vr_app_developemnt(request):
    return render(request, "ar-vr-app-developemnt.html")


def business_modernization(request):
    return render(request, "business-modernization.html")

def career_counsellings(request):
    return render(request, "career-counsellings.html")
def customized_training_programs(request):
    return render(request, "customized-training-programs.html")
# ===========FUNCTIONS FOR SUCCESSSTORIES=======
def podcasts(request):
    return render(request, "podcasts.html")
# def podcasts(request):
#     pod = Podcast.objects.all()
#     return render(request,"podcasts.html",{'podcasts':pod})


def promotional_videos(request):
    return render(request, "promotional-videos.html")


def blog(request):
    return render(request, "blog.html")
def csr(request):
    return render(request, "csr.html")






# =======FUNCTIONS for careers=====

def graduates(request):
    return render(request, "graduates.html")
def experienced_professionals(request):
    return render(request, "experienced-professionals.html")
def students_internships(request):
    return render(request, "students-internships.html") 
def explore_opportunities(request):
    return render(request, "explore-opportunities.html")
# =======FUNCTIONS for new room=====
def news_room(request):
    return render(request, "news-room.html")
def press_releases(request):
    return render(request, "press-releases.html")
def features(request):
    return render(request, "features.html")





# new urls start


def growth_optimization(request):
    return render(request, "growth-optimization.html")

def talent_acceleration(request):
    return render(request, "talent-acceleration.html")

# def talent_acceleration(request):
#     return render(request, "talent-acceleration.html"),

def generative_ai_advisory(request):
    return render(request, "generative-ai-advisory.html")

# def next_gen_marketing(request):
#     return render(request, "next-gen-marketing.html")



def cx_strategy_and_design(request):
    return render(request, "cx-strategy-and-design.html")

# def cx_strategy_and_design(request):
#     return render(request, "cx-strategy-and-design.html"),

def next_gen_marketing(request):
    return render(request, "next-gen-marketing.html"),

def workforce_experience(request):
    return render(request, "workforce-experience.html")



def react_js_practice (request):
    return render(request, "react-js-practice.html")


def managed_detection_response (request):
    return render(request, "managed-detection-response.html")

def digital_risk_management (request):
    return render(request, "digital-risk-management.html")



def ransomware_protection (request):
    return render(request, "ransomware-protection.html")

def zero_trust_implementation (request):
    return render(request, "zero-trust-implementation.html")

def next_gen_marketing (request):
    return render(request, "next-gen-marketing.html")

def embedded_system_development (request):
    return render(request, "embedded-system-development.html")

def services (request):
    return render(request, "services.html")


# ====Functions for new Industries====
def industries(request):
    return render(request, "industries.html")

def consumer_packaged_goods(request):
    return render(request, "consumer-packaged-goods.html")
def travel_and_hospitality(request):
    return render(request, "travel-and-hospitality.html")
def retail(request):
    return render(request, "retail.html")
def wealth_management(request):
    return render(request, "wealth-management.html")
def commercial_banking(request):
    return render(request, "commercial-banking.html")
def telecommunications(request):
    return render(request, "telecommunications.html")
def media_and_entertainment(request):
    return render(request, "media-and-entertainment.html")
def gaming(request):
    return render(request, "gaming.html")
def business_information_and_publishing(request):
    return render(request, "business-information-and-publishing.html")
def sports(request):
    return render(request, "sports.html")
def regulations(request):
    return render(request, "regulations.html")
def metahuman_assistant(request):
    return render(request, "metahuman-assistant.html")
def medtech(request):
    return render(request, "medtech.html")
def software_and_tech(request):
    return render(request, "software-and-tech.html")
def education(request):
    return render(request, "education.html")
def energy_and_resources(request):
    return render(request, "energy-and-resources.html")




def corporate_responsibility (request):
    return render(request, "corporate-responsibility.html")

def ethics_and_compliance (request):
    return render(request, "ethics-and-compliance.html")

def events (request):
    return render(request, "events.html")

# def contactus (request):
#     return render(request, "contactus.html")

def faqs (request):
    return render(request, "faqs.html")



def get_on_board (request):
    return render(request, "get-on-board.html")

def relocate_with_spg (request):
    return render(request, "relocate-with-spg.html")

def referral_program (request):
    return render(request, "referral-program.html")



def spg_insights (request):
    return render(request, "spg-insights.html")


# def ebooks_innerpage (request, ebook):
#     obj = Ebook_pdf.objects.filter(perma_link = ebook).first()
#     if obj:
#         return render(request, "ebooks-innerpage.html", {"Ebookdata": obj})
#     return render(request, "/")

# def whitepapers_innerpage(request,wbook):
#     obj = Whitepaper_pdf.objects.filter(perma_link = wbook).first()
#     if obj:
#         return render(request, "whitepapers-innerpage.html", {"Whitepaperdata": obj})
#     return render(request, "/")



    

   









# new urls start



   
    
   

# =========== Function for Robots.txt =======
def robots(request):
    return HttpResponse(open("robots.txt").read(), content_type="text/plain")


# ============= Function for Sitemaps.xml ===============
def sitemap(request):
    return HttpResponse(open("sitemap.xml").read(), content_type="text/xml")

def captcha_authenticator(client_key):
    secret_key = "6LfmsQokAAAAAD4JdPNgD_PeX5dJyWwetbySgwqa"
    captcha_data = {"secret": secret_key, "response": client_key}
    r = requests.post(
        "https://www.google.com/recaptcha/api/siteverify", data=captcha_data
    )
    response = json.loads(r.text)
    verify = response["success"]
    if verify:
        return True
    else:
        return False

# =========================CONTACT-US=====================================

def New_Contact(rwquest):
    return redirect("contact")       


def Contact_Us(request):
    if request.method == "GET":
        return render(request, "contact.html")
    else:
        Name = request.POST.get("yourname")
        Organization_Name = request.POST.get("yourorganization")
        Mobile = request.POST.get("yourphone")
        Email = request.POST.get("youremail")
        Message = request.POST.get("yourmessage")
        client_key = request.POST["g-recaptcha-response"]
        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        Date = DateTime.split(" ")[0]
        authenticated = captcha_authenticator(client_key)
        if authenticated:
            ContactUs(
                Name=Name,
                Organization_Name=Organization_Name,
                Mobile=Mobile,
                Email=Email,
                Message=Message,
                Submitted_on=DateTime,
                # userinfo=Crsf_token + "|" + str(verify),
            ).save()
            html_content = render_to_string(
                "contact-email-template.html", {"First_Name": Name}
            )
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                "Thank you for Contacting-Us",
                text_content,
                settings.EMAIL_HOST_USER,
                [Email],
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
            # ===================Sending mail to the admin ============
            text = f"""
            <p>
                <strong>
                From:
                </strong>
                {Name} - {Email}<br>
                <strong>
                Sent:
                </strong>{DateTime}<br>
                <strong>
                To:
                </strong>noreply@spgamerica.com<br>
                <strong>
                Subject: 
                </strong>SPG America - Contact Us<br><br>
            </p>
            <table cellpadding="5" cellpadding="0">
            <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
            <tr><td width="100">Name</td><td>:</td><td>{Name}</td></tr>
            <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
            <tr><td>Phone</td><td>:</td><td>{Mobile}</td></tr>
            <tr><td>Organization Name</td><td>:</td><td>{Organization_Name}</td></tr>
            <tr><td colspan="3"><strong>Customer Message Details are as follows:</strong></td></tr>
            <tr><td>Message</td><td>:</td><td>{Message}</td></tr>
            <tr><td>Date</td><td>:</td><td>{Date}</td></tr></table><br>
            <p>
                Sincerely, <br><br>
                SPG America, <br>
                noreply@spgamerica.com
            </p>
            """
            Admintext_content = text
            Adminemail = EmailMultiAlternatives(
                "SPG America - Contact Us",
                Admintext_content,
                settings.EMAIL_HOST_USER,
                # ["aman@vitelglobal.com", "ashok.n@vitelglobal.com"],
                ["careers@spgamerica.com"],
                cc=['ashaik@spgamerica.com', 'vlaxmi@spgamerica.com', 'rohit@spgamerica.com']
                # ["enquiry@vitelglobal.in"],
            )
            Adminemail.content_subtype = "html"
            Adminemail.send()
            return render(request, "thankyou.html")
        else:
            return redirect('/')


def ebooks_innerpage (request, ebook):
    obj = Ebook_pdf.objects.filter(perma_link = ebook).first()
    if obj: 
        return render(request, "ebooks-innerpage.html", {'Ebookdata': obj})
    return render(request, "ebooks-innerpage.html")

def e_books(request):
    EBookdata=Ebook_pdf.objects.all().order_by('-enumber')
    if request.method=="GET":
        return render(request,'e-books.html',{'EBookdata':EBookdata})
    else:
        Client_Key = request.POST["g-recaptcha-response"]
        authenticated = captcha_authenticator(Client_Key)
        if authenticated:
            Name = request.POST.get("name")
            Mobile = request.POST.get("phone")
            Email = request.POST.get("email")
            CompanyName= request.POST.get('organization')
            Ebookid = request.POST.get("ebookid")
            Ebook =Ebook_pdf.objects.get(enumber=Ebookid)
            Ebook_link= Ebook.ebook_pdf
            Title=Ebook.title
            DateTime= datetime.now(Timezone)
            DateTime= (str(DateTime)).split('.')[0]
            Date= DateTime.split(' ')[0]
            Ebook_Download(
                Name=Name,
                Mobile=Mobile,
                Email=Email,
                CompanyName=CompanyName,
                submitted_on=DateTime,
            ).save()
            html_content = render_to_string('ebooks-email-template.html',{"First_Name":Name,"Ebook_link":Ebook_link})
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                "Thank you for Downloading Our E-Book",
                text_content,
                settings.FROM_EMAIL,
                [Email]
            )
            email.attach_alternative(html_content,'text/html')
            email.send()
            #===================Sending mail to the admin ============
            text= f'''
            <p>
                <strong>
                From:
                </strong>
                {Name} - {Email}<br>
                <strong>
                Sent:
                </strong>{DateTime}<br>
                <strong>
                To:
                </strong> noreply@spgamerica.com<br>
                <strong>
                Subject: 
                </strong>Downladed-E_Book entitled: {Title} <br><br>
            </p>
            <table cellpadding="5" cellpadding="0">
            <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
            <tr><td width="150">Name</td><td>:</td><td>{Name}</td></tr>
            <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
            <tr><td>Phone</td><td>:</td><td>{Mobile}</td></tr>
            <tr><td>Company Name:</td><td>:</td><td>{CompanyName}</td></tr>
            <tr><td>Downloaded E-Book on</td><td>:</td><td>{Date}</td></tr></table><br>
            <p>
                Sincerely, <br>
                SPG America, <br>
                enquiry@vitelglobal.com
            </p>
            '''
            Admintext_content = text
            Adminemail = EmailMultiAlternatives(
                "SPG America - E_Book",
                Admintext_content,
                settings.EMAIL_HOST_USER,
                # ["aman@vitelglobal.com", "ashok.n@vitelglobal.com"],
                ["careers@spgamerica.com"],
                cc=['ashaik@spgamerica.com', 'vlaxmi@spgamerica.com', 'rohit@spgamerica.com']
            )
            Adminemail.content_subtype='html'
            Adminemail.send()
            # data= {'message': f'Thanks for your interest to download our E-book entitled <b>“{Title}”</b>.<br>You are just one step closer to explore our innovative resources section. You will be offered with informative, trendy, and knowledgeable content.<br>Get your E-book download link to your registered email address: <b>{Email}</b>'}
            return render(request, "thankyou.html")
        else:
            return redirect('/')
        
def whitepapers_pages(request, ebook):
    whitepaper = Whitepaper_pdf.objects.filter(perma_link = ebook).first()
    if whitepaper:
        return render(request, 'whitepapers-innerpage.html', {'Whitepapers': whitepaper})
    else:
        return render('/')
    

def white_papers(request):
    Whitepaperdata=Whitepaper_pdf.objects.all().order_by('-wnumber')
    if request.method=="GET":
        return render(request,'white-papers.html',{'Whitepaperdata':Whitepaperdata}) 
    else:
        Client_Key = request.POST["g-recaptcha-response"]
        authenticated = captcha_authenticator(Client_Key)
        if authenticated:
            Name = request.POST.get("name")
            Mobile = request.POST.get("phone")
            Email = request.POST.get("email")
            CompanyName= request.POST.get('organization')
            Wpaperid = request.POST.get("wpaperid")
            wpaper =Whitepaper_pdf.objects.get(wnumber=Wpaperid) 
            wpaper_link= wpaper.whitepaper_pdf
            Title=wpaper.title
            DateTime= datetime.now(Timezone)
            DateTime= (str(DateTime)).split('.')[0]
            Date= DateTime.split(' ')[0]
            Whitepaper_Download(
                Name=Name,
                Mobile=Mobile,
                Email=Email,
                CompanyName=CompanyName,
                submitted_on=DateTime,
            ).save()
            html_content = render_to_string('whitepapers-email-template.html',{"First_Name":Name,"wpaper_link":wpaper_link})
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                "Thank you for Downloading Our Whitepaper",
                text_content,
                settings.EMAIL_HOST_USER,
                [Email]
            )
            email.attach_alternative(html_content,'text/html')
            email.send()
            #===================Sending mail to the admin ============
            text= f'''
            <p>
                <strong>
                From:
                </strong>
                {Name} - {Email}<br>
                <strong>
                Sent:
                </strong>{DateTime}<br>
                <strong>
                To:
                </strong> noreply@spgamerica.com<br>
                <strong>
                Subject: 
                </strong>Downladed-Whitepaper entitled: {Title} <br><br>
            </p>
            <table cellpadding="5" cellpadding="0">
            <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
            <tr><td width="150">Name</td><td>:</td><td>{Name}</td></tr>
            <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
            <tr><td>Phone</td><td>:</td><td>{Mobile}</td></tr>
            <tr><td>CompanyName</td><td>:</td><td>{CompanyName}</td></tr>
            <tr><td>Downloaded Whitepaper on</td><td>:</td><td>{Date}</td></tr></table><br>
            <p>
                Sincerely, <br>
                SPG America, <br>
                noreply@spgamerica.com
            </p>
            '''
            Admintext_content = text
            Adminemail = EmailMultiAlternatives(
                "SPG America - Whitepaper",
                Admintext_content,
                settings.FROM_EMAIL,
                # ["aman@vitelglobal.com", "ashok.n@vitelglobal.com"],
                ["careers@spgamerica.com"],
                cc=['ashaik@spgamerica.com', 'vlaxmi@spgamerica.com', 'rohit@spgamerica.com']
                #["enquiry@vitelglobal.in"],
                #cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
            )
            Adminemail.content_subtype='html'
            Adminemail.send()
            # data= {'message': f'It is most exciting to see you here! <br>You made the right choice to download our Whitepaper entitled <b>“{Title}”</b>.<br>You are going to step in into an extensive hub for product insights, awareness about the latest technologies in the telecom industry, and many more interesting topics through our Whitepapers.<br>Get your Whitepaper download link to your registered email address: <b>{Email}</b> '}
            return render(request, "thankyou.html")
        else:
            return redirect('/')

# Function for Newsletter Subscription
def Newsletter(request):
    if request.method=="GET":
        return redirect('/')
    else:
        NewsLetterEmail = request.POST.get("newsletteremail")
        DateTime= datetime.now(Timezone)
        DateTime= (str(DateTime)).split('.')[0]
        RequestedDate= DateTime.split(' ')[0]
        Subscribe(
            NewsLetterEmail=NewsLetterEmail,
            Submitted_on=DateTime,
        ).save()
        html_content = render_to_string('newsletter-email-template.html')
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Thank you for subscribing to our Newsletter",
            text_content,
            settings.EMAIL_HOST_USER,
            [NewsLetterEmail]
        )
        email.attach_alternative(html_content,'text/html')
        email.send()
        #==========sending mail to the admin =============
        text= f'''
        <p>
            <strong>
            From:
            </strong>
            {NewsLetterEmail}<br>
            <strong>
            Sent:
            </strong>{DateTime}<br>
            <strong>
            To:
            </strong> noreply@spgamerica.com<br>
            <strong>
            Subject: 
            </strong>Newsletter Subscription<br><br>
        </p>
        <table cellpadding="5" cellpadding="0">
        <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
        <tr><td width="240">Customer Email</td><td>:</td><td>{NewsLetterEmail}</td></tr>
        <tr><td>Subscribed our Newsletter on</td><td>:</td><td>{RequestedDate}</td></tr></table><br>
        <p>
            Sincerely, <br><br>
            SPG America, <br>
            noreply@spgamerica.com
        </p>
        '''
        Admintext_content = text
        Adminemail = EmailMultiAlternatives(
            "Newsletter Subscription",
            Admintext_content,
            settings.EMAIL_HOST_USER,
            # ["aman@vitelglobal.com", "ashok.n@vitelglobal.com"],
            ["careers@spgamerica.com"],
            cc=['ashaik@spgamerica.com', 'vlaxmi@spgamerica.com', 'rohit@spgamerica.com']
            #['enquiry@vitelglobal.in'],
            #cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
        )
        Adminemail.content_subtype='html'
        Adminemail.send()
        
        # data= {'message': 'Kudos! You have just took a powerful decision to transform your mailbox into an innovative space. We will make your day more beautiful with our updates and special offers.'}
        return render(request, 'thankyou.html')


def careers(request):
    if request.method == 'POST':
        Client_Key = request.POST["g-recaptcha-response"]
        authenticated = captcha_authenticator(Client_Key)
        if authenticated:
            resume = request.FILES["formFile"]
            size_validation = FileValidation(resume)
            if not size_validation:
                return redirect('/')
            name = request.POST.get("yourname")
            phone = request.POST.get("yourphone")
            Email = request.POST.get("youremail")
            experience = request.POST.get("cyear")
            message = request.POST.get("cmessage")
            Resume = SaveResume(resume, "media/", "/media", Email)
            DateTime= datetime.now(Timezone)
            DateTime= (str(DateTime)).split('.')[0]
            Careers_table(
                Name = name,
                Email = Email,
                Phone= phone,
                Experience= experience,
                Message = message,
                Resume = Resume
            ).save()
            html_content = render_to_string(
                "career-email-template.html", {"First_Name": name}
            )
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                "Thank you for Applying at SPG America",
                text_content,
                settings.EMAIL_HOST_USER,
                [Email],
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
            # ===================Sending mail to the admin ============
            text = f"""
            <p>
                <strong>
                From:
                </strong>
                {name} - {Email}<br>
                <strong>
                Sent:
                </strong>{DateTime}<br>
                <strong>
                To:
                </strong>noreply@spgamerica.com<br>
                <strong>
                Subject: 
                </strong>Job Application - Career Portal <br><br>
            </p>
            <table cellpadding="5" cellpadding="0">
            <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
            <tr><td width="100">Name</td><td>:</td><td>{name}</td></tr>
            <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
            <tr><td>Phone</td><td>:</td><td>{phone}</td></tr>
            <tr><td>Experience</td><td>:</td><td>{experience}</td></tr>
            <tr><td colspan="3"><strong>Applicant Message Details are as follows:</strong></td></tr>
            <tr><td>Message</td><td>:</td><td>{message}</td></tr>
            <tr><td>Resume</td><td>:</td><td><a href="https://www.spgamerica.com/media/{Resume}">{Resume}</a></td></tr></table><br>
            <p>
                Sincerely, <br><br>
                SPG America, <br>
                noreply@spgamerica.com
            </p>
            """
            Admintext_content = text
            Adminemail = EmailMultiAlternatives(
                "Job Application - Career Portal",
                Admintext_content,
                settings.EMAIL_HOST_USER,
                # ["aman@vitelglobal.com", "ashok.n@vitelglobal.com"],
                ["careers@spgamerica.com"],
                cc=['ashaik@spgamerica.com', 'vlaxmi@spgamerica.com', 'rohit@spgamerica.com']
            )
            Adminemail.content_subtype = "html"
            Adminemail.send()
            return render(request, 'thankyou.html')
    return render(request, "careers.html")


############################## NEW URL Redirections #############################
def ai_ml_automation(request):
    return redirect('ai-ml-research-and-development', permanent=True)

def ai_ml_research_and_development (request):
    return render(request, "ai-ml-research-and-development.html")
#----------------------------------------------------------------

def digital_marketing_agency(request):
    return redirect('services/digital-transformation', permanent=True)

def digital_transformation(request):
    return render(request, "digital-transformation.html")

#----------------------------------------------------------------

def spg_metaverse(request):
    return redirect("services/metaverse", permanent=True)

def metaverse (request):
    return render(request, "metaverse.html")
#-----------------------------------------------------------------

def cloud_tech(request):
    return redirect("cloud-data-security", permanent=True)

def cloud_data_security (request):
    return render(request, "cloud-data-security.html")

#-----------------------------------------------------------------
def web_development(request):
    return redirect("services/digital-transformation", permanent=True)

def web_digital_transformation(request):
    return render(request, "digital-transformation.html")

#------------------------------------------------------------------
def programming(request):
    return redirect("services/python-practice", permanent=True)

def python_practice (request):
    return render(request, "python-practice.html")

#--------------------------------------------------------------

def networking(request):
    return redirect("services/cybersecurity-advisory", permanent=True)

def cybersecurity_advisory (request):
    return render(request, "cybersecurity-advisory.html")
#---------------------------------------------------------------

def technical_training_programs(request):
    return redirect('index', permanent=True)

def tech_Index(request):
    return render(request, "index.html")

#----------------------------------------------------------------
def itconsulting_services(request):
    return redirect('index', permanent=True)

def it_Index(request):
    return render(request, "index.html")

#----------------------------------------------------------------

def spg_mission_statement(request):
    return redirect('index', permanent=True)


def mission_Index(request):
    return render(request, "index.html")
#----------------------------------------------------------------
def inclusion_and_diversity(request):
     return redirect('index', permanent=True)

def inclusion_Index(request):
    return render(request, "index.html")

#------------------------------------------------------------------
def all_in_one_services(request):
	return redirect('new-services', permanent=True)

def new_all_in_one(request):
    return render(request, "all-in-one-services.html")

#-----------------------------------------------
def fraud_warning(request):
    return redirect("privacy-policy", permanent=True)

def privacy_policy(request):
    return render(request, "privacy-policy.html")

#--------------------------------------------------------------
































#########################################################################################################

























# def get_data(job_order, error):
#     data = requests.get("http://38.143.106.213/ATS/get_joborder.php")
#     DataText = data.json()
#     for item in DataText:
#         if item["joborder_id"] == job_order:
#             output = {
#                 "job_title": item["title"],
#                 "city": item["city"],
#                 "state": item["state"],
#                 "date_created": item["date_created"],
#                 "required_experience": item["required_experience"],
#                 "shift_timing": item["shift_timing"],
#                 "required_education": item["required_education"],
#                 "mode_of_operation": item["mode_of_operation"],
#                 "openings": item["openings"],
#                 # gender has to be added
#                 "perks_and_benefits": item["perks_and_benefits"],
#                 "salary": item["salary"],
#                 "job_description": item["description"],
#                 "roles_responsibility": item["roles_responsibility"],
#                 # "profile": item["profile"],
#                 "company_email": item["company_email"],
#                 "job_id": job_order,
#                 "required_key_skills": item["required_key_skills"],
#                 "error": error,
#             }
#             return output


# def Sucess(request):
#     if request.method == "POST":
#         try:
#             name = request.POST.get("name")
#             email = request.POST.get("email")
#             phone = request.POST.get("phone")
#             technology = request.POST.get("technology")
#             skills = request.POST.get("skills")
#             designation = request.POST.get("designation")
#             experience = request.POST.get("experience")
#             companies = request.POST.get("companies")
#             education = request.POST.get("education")
#             college = request.POST.get("college")
#             resume = request.POST.get("filepath")
#             TimeDate = datetime.now(Timezone)
#             TimeDate = (str(TimeDate)).split(".")[0]
#             context = {
#                 "name": name,
#                 "email": email,
#                 "phone": phone,
#                 "technology": technology,
#                 "skills": skills,
#                 "designation": designation,
#                 "experience": experience,
#                 "datetime": TimeDate,
#                 "companies": companies,
#                 "education": education,
#                 "college": college,
#                 "filepath": resume,
#             }
#             Resumefile = {"Resumefile": open(f"media/{resume}", "rb")}
#             r = requests.post(
#                 "https://resume.vitelglobal.com/api/pss_save",
#                 data=context,
#                 files=Resumefile,
#             )
#             # r = requests.post("http://resume.vitelglobal.com:5000/api/pss_save", data=context, files=Resumefile, timeout=60, allow_redirects=True)
#             response = r.text
#             return render(request, "careerthankyou.html")
#         except:
#             return render(request, "error.html")
#     else:
#         return redirect("/")


# def Careers_listing(request, joborderid):
#     my_host = "smtp-mail.outlook.com"
#     my_port = 587
#     my_username = "career@pranathiss.com"
#     my_password = "dC$V@C4EK1z8w"
#     my_use_tls = True
#     connection = get_connection(
#         host=my_host,
#         port=my_port,
#         username=my_username,
#         password=my_password,
#         use_tls=my_use_tls,
#     )
#     if request.method == "GET":
#         output = get_data(joborderid, "")
#         return render(request, "careers-listing.html", output)
#     else:
#         try:
#             Name = request.POST.get("cfname")
#             Email = (request.POST.get("cemail")).strip()
#             Phone = request.POST.get("cphoneno")
#             Experience = request.POST.get("cyear")
#             Message = request.POST.get("cmessage")
#             Resume = request.FILES["formFile"]
#             # Resumename = Email+ '.' +(Resume.name).split('.')[-1]
#             DateTime = datetime.now(Timezone)
#             DateTime = (str(DateTime)).split(".")[0]
#             if FileValidation(Resume):
#                 Obj = Careers_table.objects.filter(Email=Email, JobOrderID=joborderid)
#                 if len(Obj) == 0:
#                     NewResume = SaveResume(Resume, "media/", "/media", Email)
#                     if NewResume.split(".")[-1] == "doc":
#                         NewResume = doctodocx(f"media/", NewResume, "/media")
#                     Careers_table(
#                         Name=Name,
#                         Email=Email,
#                         Phone=Phone,
#                         Experience=Experience,
#                         Message=Message,
#                         Resume=NewResume,
#                         JobOrderID=joborderid,
#                         Submitted_on=DateTime,
#                     ).save()
#                     Resumefile = {"Resume": open(f"media/{NewResume}", "rb")}
#                     data = {
#                         "Name": Name,
#                         "Email": Email,
#                         "Phone": Phone,
#                         "Experience": Experience,
#                         "Message": Message,
#                         "Resume": NewResume,
#                         "Joborderid": joborderid,
#                         "Submitted_on": DateTime,
#                     }
#                     r = requests.post(
#                         "https://resume.vitelglobal.com/api/pss",
#                         data=data,
#                         files=Resumefile,
#                     )
#                     # r = requests.post("http://resume.vitelglobal.com:5000/api/pss", data=data, files=Resumefile, timeout=60, allow_redirects=True)
#                     response = r.text
#                     response = r.json()
#                     r1 = requests.post(
#                         "http://38.143.106.213/ATS/pss_career_candidate.php", data=data
#                     )
#                     html_content = render_to_string(
#                         "careers-email.html", {"First_Name": Name}
#                     )
#                     text_content = strip_tags(html_content)
#                     email = EmailMultiAlternatives(
#                         "Thank you for Applying at Pranathiss",
#                         text_content,
#                         "career@pranathiss.com",
#                         [Email],
#                         connection=connection,
#                     )
#                     email.attach_alternative(html_content, "text/html")
#                     email.send()
#                     # ===================Sending mail to the admin ============
#                     text = f"""
#                     <p>
#                         <strong>
#                         From:
#                         </strong>
#                         {Name} - {Email}<br>
#                         <strong>
#                         Sent:
#                         </strong>{DateTime}<br>
#                         <strong>
#                         To:
#                         </strong>career@pranathiss.com<br>
#                         <strong>
#                         Subject: 
#                         </strong>Job Application - Career Portal <br><br>
#                     </p>
#                     <table cellpadding="5" cellpadding="0">
#                     <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
#                     <tr><td width="100">Name</td><td>:</td><td>{Name}</td></tr>
#                     <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
#                     <tr><td>Phone</td><td>:</td><td>{Phone}</td></tr>
#                     <tr><td>Experience</td><td>:</td><td>{Experience}</td></tr>
#                     <tr><td colspan="3"><strong>Applicant Message Details are as follows:</strong></td></tr>
#                     <tr><td>Message</td><td>:</td><td>{Message}</td></tr>
#                     <tr><td>Resume</td><td>:</td><td><a href="https://pss.pranathiss.com/media/{NewResume}">{NewResume}</a></td></tr></table><br>
#                     <tr><td>For Job Order ID</td><td>:</td><td>{joborderid}</td></tr></table><br>
#                     <p>
#                         Sincerely, <br><br>
#                         Pranathi Software Services Pvt.Ltd., <br>
#                         career@pranathiss.com
#                     </p>
#                     """
#                     Admintext_content = text
#                     Adminemail = EmailMultiAlternatives(
#                         "Job Application - Career Portal",
#                         Admintext_content,
#                         "career@pranathiss.com",
#                         ["career@pranathiss.com"],
#                         cc=[
#                             "sridhar@pranathiss.com",
#                             "aarti@pranathiss.com",
#                             "mukesh@pranathiss.com",
#                         ],
#                         # ["enquiry@vitelglobal.in"],
#                         connection=connection,
#                     )
#                     Adminemail.content_subtype = "html"
#                     Adminemail.send()
#                     return render(request, "careers-listing-edit.html", response)
#                 else:
#                     output = get_data(
#                         joborderid, "*You have already applied for this job."
#                     )
#                     return render(request, "careers-listing.html", output)
#             else:
#                 output = get_data(
#                     joborderid, "*File size or file format not supported."
#                 )
#                 return render(request, "careers-listing.html", output)
#         except:
#             return render(request, "error.html")

