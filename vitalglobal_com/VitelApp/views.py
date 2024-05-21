from email.message import Message
from time import time
from urllib import request
from django.shortcuts import render, redirect
from .models import (
    Subscribe,
    KickStart,
    ContactUs,
    Webinars_table,
    LiveDemo,
    Careers_table,
    Partner_Program,
    Feedback_table,
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
    setup_plans,
    UnsubscribeRequest,
)
from django.core.mail.message import EmailMessage
from django.core.mail import get_connection, send_mail
import os
import json
import random
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from http import HTTPStatus
from django.test import TestCase
from VitelProject import settings

# Email Html required imports
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from ics import Calendar, Event
from datetime import datetime
import pytz
import requests
from requests.adapters import HTTPAdapter, Retry
from bs4 import BeautifulSoup
from filehandler import SaveResume, doctodocx, FileValidation
from .utils import Util, timezone_now

from .forms import CaptchaForm

Timezone = pytz.timezone("Asia/Kolkata")


def redirect_itserve(request):
    return redirect('itserve-offer')

def qrcode(request, qrcode):
    data = DynamicQrCode.objects.filter(Base_url=qrcode)
    if data:
        link = data[0].Redirect_to
        return redirect(link)


def qrcode(request):
    data = QRcode.objects.all().first()
    link = data.link
    return redirect(link)


def index_test2(request):
    return render(request, "index_test.html")


def get_ip(request):
    try:
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = " "
    return ip


def captcha_authenticator(client_key):
    secret_key = "6LfK-0IiAAAAAAR-tXzmE6ZjEW9tP9pxOmiFjlvY"
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


# This function saves the  uploaded  file
def handle_uploaded_file(f, email):
    basepath = str(os.getcwd()) + "/media"
    path = os.listdir(basepath)
    # CHANGES THE FILE NAME TO THE EMAIL OF THE CANDIDATE
    if ".pdf" in f.name:
        filename = email + ".pdf"
    elif ".docx" in f.name:
        filename = email + ".docx"
    elif ".doc" in f.name:
        filename = email + ".doc"
    else:
        return None  # HANDLED temporarily

    # CHECKS IF FILENAME ALREADY EXISTS OR NOT
    if filename not in path:
        with open("media/" + filename, "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    # IF SAME FILE EXISTS IT RENAMES IT
    else:
        if ".pdf" in filename:
            filename = email + str(random.randint(1000, 9999)) + ".pdf"
            with open("media/" + filename, "wb+") as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        elif ".docx" in filename:
            filename = email + str(random.randint(1000, 9999)) + ".docx"
            with open("media/" + filename, "wb+") as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        elif ".doc" in filename:
            filename = email + str(random.randint(1000, 9999)) + ".doc"
            with open("media/" + filename, "wb+") as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        else:
            pass
    return filename


# Create your views here.
def index(request):
    form = CaptchaForm(use_required_attribute=False)
    newsform = CaptchaForm(use_required_attribute=False, prefix="news")
    feedform = CaptchaForm(use_required_attribute=False, prefix="feed")
    return render(
        request,
        "index.html",
        {"form": form, "newsform": newsform, "feedform": feedform},
    )


def index_test(request):
    form = CaptchaForm(use_required_attribute=False)
    newsform = CaptchaForm(use_required_attribute=False, prefix="news")
    feedform = CaptchaForm(use_required_attribute=False, prefix="feed")
    return render(
        request,
        "index.html",
        {"form": form, "newsform": newsform, "feedform": feedform},
    )


def test(request):
    return render(request, "test.html")


# =======Functions for Products====
def ucaas(request):
    return render(request, "ucaas.html")


def cloud_based_business_phone(request):
    return render(request, "cloud-based-business-phone.html")


def ip_phones(request):
    return render(request, "ip-phones.html")


def voip_video_conference(request):
    return render(request, "voip-video-conference.html")


def redirect_voip_video_conference(request):
    return redirect("voip-video-conference")


def team_messaging(request):
    return render(request, "team-messaging.html")


def communication_apis(request):
    return render(request, "communication-apis.html")


def email_server_services(request):
    return render(request, "email-server-services.html")


def mobile_voip_app(request):
    return render(request, "mobile-voip-app.html")


def desktop_voip_app(request):
    return render(request, "desktop-voip-app.html")


# =======Functions for Solutions=================================
# By Organization
def corporate_business_phone_solutions(request):
    return render(request, "corporate-business-phone-solutions.html")


def enterprise_business_phone_service(request):
    return render(request, "enterprise-business-phone-service.html")


def business_phone_solutions_non_profit(request):
    return render(request, "business-phone-solutions-non-profit.html")


def small_business_phone_service(request):
    return render(request, "small-business-phone-service.html")


# Functions for Sector====
def it_staffing_cloud_phone_system(request):
    return render(request, "it-staffing-cloud-phone-system.html")


def education_cloud_phone_system(request):
    return render(request, "education-cloud-phone-system.html")


def healthcare_cloud_phone_services(request):
    return render(request, "healthcare-cloud-phone-services.html")


def business_communications_for_financial_services(request):
    return render(request, "business-communications-for-financial-services.html")


def manufacturing_business_phone_service(request):
    return render(request, "manufacturing-business-phone-service.html")


def business_phone_service_retail_stores(request):
    return render(request, "business-phone-service-retail-stores.html")


def real_estate_business_phone_service(request):
    return render(request, "real-estate-business-phone-service.html")


def business_phone_technical_services(request):
    return render(request, "business-phone-technical-services.html")


def transportation_warehousing_phone_service(request):
    return render(request, "transportation-warehousing-phone-service.html")


# Functions for By Need====
def cloud_voip_solutions(request):
    return render(request, "cloud-voip-solutions.html")


def SIP_trunking(request):
    return render(request, "SIP-trunking.html")


def global_scope(request):
    return render(request, "global-scope.html")


def redirect_global_scope(request):
    return redirect("global-scope")


def crm_integration(request):
    return render(request, "crm-integration.html")


def ats_integration(request):
    return render(request, "ats-integration.html")


def voip_api_integration(request):
    return render(request, "voip-api-integration.html")


# Functions for Pricing
def unlimited_calling_plans(request):
    return render(request, "unlimited-calling-plans.html")


def pay_as_you_go(request):
    return render(request, "pay-as-you-go.html")


# =======urls for Resources====
def promo_videos(request):
    return render(request, "promo-videos.html")


def e_books(request):
    return render(request, "e-books.html")


def podcasts(request):
    PodcastsObj = Podcast.objects.all()
    return render(request, "podcasts.html", {"Podcasts": PodcastsObj})


def factsheet(request):
    return render(request, "factsheet.html")


# def partners_program(request):
#     form = CaptchaForm(use_required_attribute=False)
#     return render(request, "partners-program.html", {"form": form})

def press_release(request):
    return render(request, "press-release.html")


def white_papers(request):
    return render(request, "white-papers.html")


def newsroom(request):
    return render(request, "newsroom.html")


def rewards_by_cio_coverage_magazine(request):
    return render(request, "rewards-by-cio-coverage-magazine.html")


def inc5000_press_release(request):
    return render(request, "inc5000-press-release.html")


def platinum_sponsor_of_itserve(request):
    return render(request, "platinum-sponsor-of-itserve.html")


def inclusion(request):
    return render(request, "inclusion.html")


def csr(request):
    return render(request, "csr.html")


def hybrid_workforce(request):
    return render(request, "hybrid-workforce.html")


# =======urls for company====
def overview(request):
    return render(request, "overview.html")


def why_vitelglobal(request):
    return render(request, "why-vitelglobal.html")


def why_voip(request):
    return render(request, "why-voip.html")


def contact_center_solutions(request):
    return render(request, "contact-center-solutions.html")


# =======urls for features====
def local_dialling(request):
    return render(request, "local-dialling.html")


def extensions(request):
    return render(request, "extensions.html")


def call_delegation(request):
    return render(request, "call-delegation.html")


def call_forwarding(request):
    return render(request, "call-forwarding.html")


def call_flip(request):
    return render(request, "call-flip.html")


def call_screening(request):
    return render(request, "call-screening.html")


def omnipresence(request):
    return render(request, "omnipresence.html")


def local_numbers(request):
    return render(request, "local-numbers.html")


def one_touch_calling(request):
    return render(request, "one-touch-calling.html")


def call_park(request):
    return render(request, "call-park.html")


def answering_methods(request):
    return render(request, "answering-methods.html")


def visual_voicemail(request):
    return render(request, "visual-voicemail.html")


def phones_accessories(request):
    return render(request, "phones-accessories.html")


def paging(request):
    return render(request, "paging.html")


def internet_fax(request):
    return render(request, "internet-fax.html")


def shared_lines(request):
    return render(request, "shared-lines.html")


def voicemail_to_email(request):
    return render(request, "voicemail-to-email.html")


def cloud_pbx(request):
    return render(request, "cloud-pbx.html")


def greetings(request):
    return render(request, "greetings.html")


def multi_level_ivr(request):
    return render(request, "multi-level-ivr.html")


def music_on_hold(request):
    return render(request, "music-on-hold.html")


def dial_by_name_directory(request):
    return render(request, "dial-by-name-directory.html")


def number_porting(request):
    return render(request, "number-porting.html")


def multi_site_management(request):
    return render(request, "multi-site-management.html")


def call_monitoring(request):
    return render(request, "call-monitoring.html")


def call_logs(request):
    return render(request, "call-logs.html")


def automatic_call_recording(request):
    return render(request, "automatic-call-recording.html")


def audit_trail(request):
    return render(request, "audit-trail.html")


def brilliant_desking(request):
    return render(request, "brilliant-desking.html")


def caller_id(request):
    return render(request, "caller-id.html")


def list_of_directory(request):
    return render(request, "list-of-directory.html")


def user_templates(request):
    return render(request, "user-templates.html")


def international_numbers(request):
    return render(request, "international-numbers.html")


def international_calling(request):
    return render(request, "international-calling.html")


def video_conferencing(request):
    return render(request, "video-conferencing.html")


def audio_conferencing(request):
    return render(request, "audio-conferencing.html")


def cloud(request):
    return render(request, "cloud.html")


def collaboration_with_teams(request):
    return render(request, "collaboration-with-teams.html")


def business_sms_and_mms(request):
    return render(request, "business-sms-and-mms.html")


def message_alerts(request):
    return render(request, "message-alerts.html")


def secure_voip_service(request):
    return render(request, "secure-voip-service.html")


def single_registration(request):
    return render(request, "single-registration.html")


def data_center_overview(request):
    return render(request, "data-center-overview.html")


def roles_and_permissions(request):
    return render(request, "roles-and-permissions.html")


def analytics_portal(request):
    return render(request, "analytics-portal.html")


def performance_reports(request):
    return render(request, "performance-reports.html")


def qos_reports(request):
    return render(request, "qos-reports.html")


def live_reports(request):
    return render(request, "live-reports.html")


# =======urls for states====
def alabama(request):
    return render(request, "alabama.html")

def kentucky(request):
    return render(request, "kentucky.html")


def missouri(request):
    return render(request, "missouri.html")


def alaska(request):
    return render(request, "alaska.html")


def colorado(request):
    return render(request, "colorado.html")


def georgia(request):
    return render(request, "georgia.html")


def michigan(request):
    return render(request, "michigan.html")


def montana(request):
    return render(request, "montana.html")


def new_jersey(request):
    return render(request, "new-jersey.html")


def north_dakota(request):
    return render(request, "north-dakota.html")


def massachusetts(request):
    return render(request, "massachusetts.html")


def illinois(request):
    return render(request, "illinois.html")


def pennsylvania(request):
    return render(request, "pennsylvania.html")


def tennessee(request):
    return render(request, "tennessee.html")


def virginia(request):
    return render(request, "virginia.html")


def wisconsin(request):
    return render(request, "wisconsin.html")


def new_hampshire(request):
    return render(request, "new-hampshire.html")


def north_carolina(request):
    return render(request, "north-carolina.html")


def oregon(request):
    return render(request, "oregon.html")


def south_dakota(request):
    return render(request, "south-dakota.html")


def vermont(request):
    return render(request, "vermont.html")


def west_virginia(request):
    return render(request, "west-virginia.html")


def arizona(request):
    return render(request, "arizona.html")


def connecticut(request):
    return render(request, "connecticut.html")


def iowa(request):
    return render(request, "iowa.html")


def maine(request):
    return render(request, "maine.html")


def minnesota(request):
    return render(request, "minnesota.html")


def nebraska(request):
    return render(request, "nebraska.html")


def new_mexico(request):
    return render(request, "new-mexico.html")


def ohio(request):
    return render(request, "ohio.html")


def rhode_island(request):
    return render(request, "rhode-island.html")


def washington(request):
    return render(request, "washington.html")


def wyoming(request):
    return render(request, "wyoming.html")


def arkansas(request):
    return render(request, "arkansas.html")


def delaware(request):
    return render(request, "delaware.html")


def idaho(request):
    return render(request, "idaho.html")


def kansas(request):
    return render(request, "kansas.html")


def maryland(request):
    return render(request, "maryland.html")


def mississippi(request):
    return render(request, "mississippi.html")


def nevada(request):
    return render(request, "nevada.html")


def new_york(request):
    return render(request, "new-york.html")


def oklahoma(request):
    return render(request, "oklahoma.html")


def south_carolina(request):
    return render(request, "south-carolina.html")


def utah(request):
    return render(request, "utah.html")


def washington_dc(request):
    return render(request, "washington-dc.html")


def louisiana(request):
    return render(request, "louisiana.html")


# =======urls for states====
def alabama(request):
    return render(request, "alabama.html")

def kentucky(request):
    return render(request, "kentucky.html")


def missouri(request):
    return render(request, "missouri.html")


def alaska(request):
    return render(request, "alaska.html")


def colorado(request):
    return render(request, "colorado.html")


def georgia(request):
    return render(request, "georgia.html")


def michigan(request):
    return render(request, "michigan.html")


def montana(request):
    return render(request, "montana.html")


def new_jersey(request):
    return render(request, "new-jersey.html")


def north_dakota(request):
    return render(request, "north-dakota.html")


def massachusetts(request):
    return render(request, "massachusetts.html")


def illinois(request):
    return render(request, "illinois.html")


def pennsylvania(request):
    return render(request, "pennsylvania.html")


def tennessee(request):
    return render(request, "tennessee.html")


def virginia(request):
    return render(request, "virginia.html")


def wisconsin(request):
    return render(request, "wisconsin.html")


def new_hampshire(request):
    return render(request, "new-hampshire.html")


def north_carolina(request):
    return render(request, "north-carolina.html")


def oregon(request):
    return render(request, "oregon.html")


def south_dakota(request):
    return render(request, "south-dakota.html")


def vermont(request):
    return render(request, "vermont.html")


def west_virginia(request):
    return render(request, "west-virginia.html")


def arizona(request):
    return render(request, "arizona.html")


def connecticut(request):
    return render(request, "connecticut.html")


def iowa(request):
    return render(request, "iowa.html")


def maine(request):
    return render(request, "maine.html")


def minnesota(request):
    return render(request, "minnesota.html")


def nebraska(request):
    return render(request, "nebraska.html")


def new_mexico(request):
    return render(request, "new-mexico.html")


def ohio(request):
    return render(request, "ohio.html")


def rhode_island(request):
    return render(request, "rhode-island.html")


def texas(request):
    return render(request, "texas.html")


def washington(request):
    return render(request, "washington.html")


def wyoming(request):
    return render(request, "wyoming.html")


def arkansas(request):
    return render(request, "arkansas.html")


def delaware(request):
    return render(request, "delaware.html")


def idaho(request):
    return render(request, "idaho.html")


def kansas(request):
    return render(request, "kansas.html")


def maryland(request):
    return render(request, "maryland.html")


def mississippi(request):
    return render(request, "mississippi.html")


def nevada(request):
    return render(request, "nevada.html")


def new_york(request):
    return render(request, "new-york.html")


def oklahoma(request):
    return render(request, "oklahoma.html")


def south_carolina(request):
    return render(request, "south-carolina.html")


def utah(request):
    return render(request, "utah.html")


def washington_dc(request):
    return render(request, "washington-dc.html")


def louisiana(request):
    return render(request, "louisiana.html")



# =======urls for area code ====
def area_codes(request):
    return render(request, "area-codes.html")   

def area_codes_1(request):
    return render(request, "area-codes-1.html") 
 
def local_numbers_ac(request):
    return render(request, "local-numbers-ac.html")   

def washington_ac(request):
    return render(request, "washington-ac.html")  

def alabama_ac(request):
    return render(request, "alabama-ac.html")   
 
def arizona_ac(request):
    return render(request, "arizona-ac.html")

def arkansas_ac(request):
    return render(request, "arkansas-ac.html")

def california_ac(request):
    return render(request, "california-ac.html") 

def colorado_ac(request):
    return render(request, "colorado-ac.html") 

def connecticut_ac(request):
    return render(request, "connecticut-ac.html") 

def delaware_ac(request):
    return render(request, "delaware-ac.html") 

def florida_ac(request):
    return render(request, "florida-ac.html")

def district_of_columbia(request):
    return render(request, "district-of-columbia.html") 

def georgia_ac(request):
    return render(request, "georgia-ac.html") 

def hawaii_ac(request):
    return render(request, "hawaii-ac.html") 

def idaho_ac(request):
    return render(request, "idaho-ac.html")

def illinois_ac(request):
    return render(request, "illinois-ac.html")

def iowa_ac(request):
    return render(request, "iowa-ac.html")

def kansas_ac(request):
    return render(request, "kansas-ac.html")

def kentucky_ac(request):
    return render(request, "kentucky-ac.html")

def louisiana_ac(request):
    return render(request, "louisiana-ac.html")

def maine_ac(request):
    return render(request, "maine-ac.html")

def maryland_ac(request):
    return render(request, "maryland-ac.html")

def massachusetts_ac(request):
    return render(request, "massachusetts-ac.html")

def michigan_ac(request):
    return render(request, "michigan-ac.html")

def minnesota_ac(request):
    return render(request, "minnesota-ac.html")

def mississippi_ac(request):
    return render(request, "mississippi-ac.html")

def montana_ac(request):
    return render(request, "montana-ac.html")

def nebraska_ac(request):
    return render(request, "nebraska-ac.html")

def nevada_ac(request):
    return render(request, "nevada-ac.html")

def new_jersey_ac(request):
    return render(request, "new-jersey-ac.html")

def new_mexico_ac(request):
    return render(request, "new-mexico-ac.html")

def new_york_ac(request):
    return render(request, "new-york-ac.html")

def north_carolina_ac(request):
    return render(request, "north-carolina-ac.html")

def north_dakota_ac(request):
    return render(request, "north-dakota-ac.html")

def ohio_ac(request):
    return render(request, "ohio-ac.html")

def oklahoma_ac(request):
    return render(request, "oklahoma-ac.html")

def oregon_ac(request):
    return render(request, "oregon-ac.html")

def pennsylvania_ac(request):
    return render(request, "pennsylvania-ac.html")

def rhode_island_ac(request):
    return render(request, "rhode-island-ac.html")

def south_carolina_ac(request):
    return render(request, "south-carolina-ac.html")


def south_dakota_ac(request):
    return render(request, "south-dakota-ac.html")


def tennessee_ac(request):
    return render(request, "tennessee-ac.html")

def texas_ac(request):
    return render(request, "texas-ac.html")

def utah_ac(request):
    return render(request, "utah-ac.html")

def vermont_ac(request):
    return render(request, "vermont-ac.html")

def virginia_ac(request):
    return render(request, "virginia-ac.html")

def west_virginia_ac(request):
    return render(request, "west-virginia-ac.html")

def wisconsin_ac(request):
    return render(request, "wisconsin-ac.html")

def wyoming_ac(request):
    return render(request, "wyoming-ac.html")

# =======urls for vitel-center====
def center(request):
    return render(request, "vitel-center.html")

def faq(request):
    return render(request, "faq.html")    






def channel_partners(request):
    if request.method == 'GET':
        return render(request, 'channel-partners.html')
    else:
        Client_Key = request.POST["g-recaptcha-response"]
        authenticated = captcha_authenticator(Client_Key)
        
        if not authenticated:
            return redirect("/itserve-offer")
        
        ip_address = get_ip(request)
        Name = request.POST.get("yourname")
        Organization_Name = request.POST.get("yourorganization")
        Mobile = request.POST.get("yourphone")
        Email = request.POST.get("youremail")
        Message = request.POST.get("yourmessage")
        Howyouknow = request.POST.get("howyouknow")
        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        Date = DateTime.split(" ")[0]
        html_content = render_to_string("itserve-email.html", {"First_Name": Name})
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
            </strong> websales@vitelglobal.com<br>
            <strong>
            Subject: 
            </strong>Requested Quote - Channel Partners<br><br>
        </p>
        <table cellpadding="5" cellpadding="0">
        <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
        <tr><td width="100">Name</td><td>:</td><td>{Name}</td></tr>
        <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
        <tr><td>Organization Name</td><td>:</td><td>{Organization_Name}</td></tr>
        <tr><td>How you know</td><td>:</td><td>{Howyouknow}</td></tr>
        <tr><td>Phone</td><td>:</td><td>{Mobile}</td></tr>
        <tr><td>Message</td><td>:</td><td>{Message}</td></tr>
        <tr><td>Requested Quote on</td><td>:</td><td>{Date}</td></tr></table><br>
        <tr><td>IP Address</td><td>:</td><td>{ip_address}</td></tr></table><br>
        <p>
            Sincerely, <br><br>
            Vitel Global Communications, <br>
            contact@vitelglobal.com
        </p>
        """
        Admintext_content = text
        Adminemail = EmailMultiAlternatives(
            "Requested Quote - Channel Partners",
            Admintext_content,
            "contact@vitelglobal.com",
            # ["aman@vitelglobal.com"],
            [
                "websales@vitelglobal.com",
                
            ],
            # ["enquiry@vitelglobal.in"],
            # cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
        )
        Adminemail.content_subtype = "html"
        Adminemail.send()
        # data= {'message': 'Thank you for getting in touch!\nWe appreciate your patience in contacting us to explore more. You will be contacted by one of our executives for further assistance regarding the concerned subject. '}
        return redirect("contactus-thankyou")


# =======urls for footer====
def itserve_offer(request):
    if request.method == "GET":
        return render(request, "itserve-offer.html")
    else:
        Client_Key = request.POST["g-recaptcha-response"]
        authenticated = captcha_authenticator(Client_Key)
        if authenticated:
            ip_address = get_ip(request)
            Name = request.POST.get("yourname")
            Organization_Name = request.POST.get("yourorganization")
            Mobile = request.POST.get("yourphone")
            Email = request.POST.get("youremail")
            Message = request.POST.get("yourmessage")
            Howyouknow = request.POST.get("howyouknow")
            DateTime = datetime.now(Timezone)
            DateTime = (str(DateTime)).split(".")[0]
            Date = DateTime.split(" ")[0]
            # ContactUs(
            #     Name=Name,
            #     Organization_Name=Organization_Name,
            #     Mobile=Mobile,
            #     Email=Email,
            #     Message=Message,
            #     HowYouKnow=HowYouKnow,
            #     Whom_to_send=whom_email,
            #     Submitted_on=DateTime,
            # ).save()
            html_content = render_to_string("itserve-email.html", {"First_Name": Name})
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
                </strong> websales@vitelglobal.com<br>
                <strong>
                Subject: 
                </strong>Requested Quote - IT Serve Offer <br><br>
            </p>
            <table cellpadding="5" cellpadding="0">
            <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
            <tr><td width="100">Name</td><td>:</td><td>{Name}</td></tr>
            <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
            <tr><td>Organization Name</td><td>:</td><td>{Organization_Name}</td></tr>
            <tr><td>How you know</td><td>:</td><td>{Howyouknow}</td></tr>
            <tr><td>Phone</td><td>:</td><td>{Mobile}</td></tr>
            <tr><td colspan="3"><strong>Customer Message Details are as follows:</strong></td></tr>
            <tr><td>Number of Lines</td><td>:</td><td>{Message}</td></tr>
            <tr><td>Requested Quote on</td><td>:</td><td>{Date}</td></tr></table><br>
            <tr><td>IP Address</td><td>:</td><td>{ip_address}</td></tr></table><br>
            <p>
                Sincerely, <br><br>
                Vitel Global Communications, <br>
                contact@vitelglobal.com
            </p>
            """
            Admintext_content = text
            Adminemail = EmailMultiAlternatives(
                "Requested Quote - IT Serve Offer",
                Admintext_content,
                "contact@vitelglobal.com",
                # ["aman@vitelglobal.com"],
                [
                    "websales@vitelglobal.com",
                ],
                # ["enquiry@vitelglobal.in"],
                # cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
            )
            Adminemail.content_subtype = "html"
            Adminemail.send()

            # data= {'message': 'Thank you for getting in touch!\nWe appreciate your patience in contacting us to explore more. You will be contacted by one of our executives for further assistance regarding the concerned subject. '}
            return redirect("contactus-thankyou")
        else:
            return redirect("/itserve-offer")


def terms_and_conditions(request):
    return render(request, "terms-and-conditions.html")


def privacy_policy(request):
    return render(request, "privacy-policy.html")


def campaign_registry(request):
    return render(request, "campaign-registry.html")


def sms_registration(request):
    return render(request, "sms-registration.html")


def mms_sms_registry(request):
    return render(request, "mms-sms-registry.html")


# robots.txt
def robots(request):
    return HttpResponse(open("robots.txt").read(), content_type="text/plain")


# =======urls for Top====


# def voip_live_demo(request):
#     return render(request, "voip-live-demo.html")

# =======urls for footer====


# ============= Function for Sitemaps.xml ===============
def sitemap(request):
    return HttpResponse(open("sitemap.xml").read(), content_type="text/xml")


# ====================================Functions for All Forms ===================================================

def Careers(request):
    data = requests.get("https://hrms.indianhr.in/ATS/get_joborder_vitelglobal_com.php")
    # data = requests.get("https://hrms.indianhr.in/ATS/get_joborder.php")
    # data = requests.get("http://38.143.106.213/ATS/get_joborder.php")
    DataText = data.json()
    return render(request, "careers.html", {"output": DataText})



def get_data(job_order, error):
    data = requests.get("https://hrms.indianhr.in/ATS/get_joborder_vitelglobal_com.php")
    # data = requests.get("https://hrms.indianhr.in/ATS/get_joborder.php")
    # data = requests.get("http://38.143.106.213/ATS/get_joborder.php")
    DataText = data.json()
    for item in DataText:
        if item["joborder_id"] == job_order:
            output = {
                "job_title": item["title"],
                "city": item["city"],
                "state": item["state"],
                "date_created": item["date_created"],
                "required_experience": item["required_experience"],
                "shift_timing": item["shift_timing"],
                "required_education": item["required_education"],
                "mode_of_operation": item["mode_of_operation"],  # ddddd
                "openings": item["openings"],
                "gender": item["gender"],
                "perks_and_benefits": item["perks_and_benefits"],  # dddd
                "salary": item["salary"],
                "job_description": item["description"],
                "roles_responsibility": item["roles_responsibility"],
                # "profile": item["profile"],
                "company_email": item["company_email"],  # dddd
                "job_id": job_order,
                "required_key_skills": item["required_key_skills"],
                "error": error,
            }
            return output
        

def Careers_listing(request, joborderid):
    if request.method == "GET":
        output = get_data(joborderid, "")
        return render(request, "careers-listing.html", output)
    
    if request.method == "POST":
        form = CaptchaForm(request.POST, use_required_attribute=False)
        if not form.is_valid():
            return render(
                request, "careers-listing.html", {"form": form, "error": "*Invalid Captcha!"}
            )

        Name = request.POST.get("cfname")
        Email = request.POST.get("cemail")
        Phone = request.POST.get("cphoneno")
        Experience = request.POST.get("cyear")
        Message = request.POST.get("cmessage")
        Resume = request.FILES["formFile"]
        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        RequestedDate = DateTime.split(" ")[0]
        # Resumefile = handle_uploaded_file(Resume, Email)
        # ip_address = get_ip(request)
        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        if FileValidation(Resume):
            Obj = Careers_table.objects.filter(Email=Email, JobOrderID=joborderid)
            if not Obj:
                NewResume = SaveResume(Resume, "media/", "/media", Email)
                if NewResume.split(".")[-1] == "doc":
                    NewResume = doctodocx(f"media/", NewResume, "/media")
                Careers_table(
                    Name=Name,
                    Email=Email,
                    Phone=Phone,
                    Experience=Experience,
                    Message=Message,
                    Resume=NewResume,
                    JobOrderID=joborderid,
                    Submitted_on=DateTime,
                ).save()
                Resumefile = {"Resume": open(f"media/{NewResume}", "rb")}
                data = {
                    "CompanyName": "www.vitelglobal.com",
                    "Name": Name,
                    "Email": Email,
                    "Phone": Phone,
                    "Experience": Experience,
                    "Message": Message,
                    "Resume": NewResume,
                    "Joborderid": joborderid,
                    "Submitted_on": DateTime,
                }

                r1 = requests.post(
                    "https://hrms.indianhr.in/ATS/pss_career_candidate.php",
                    data=data,
                )
                my_host = "mail.vitelglobal.com"
                my_port = 465
                my_username = "contact"
                my_fromEmail = "contact@vitelglobal.com"
                my_password = "cq3o2$Iw%WFZ"
                my_use_tls = True
                connection = get_connection(
                    host=my_host,
                    port=my_port,
                    username=my_username,
                    password=my_password,
                    use_tls=my_use_tls,
                    from_email=my_fromEmail,
                )
                html_content = render_to_string("careers-email.html", {"First_Name": Name})
                text_content = strip_tags(html_content)
                email = EmailMultiAlternatives(
                    "Thank you for Applying at Vitelglobal.com",
                    text_content,
                    my_fromEmail,
                    [Email],
                    connection=connection,
                )
                email.attach_alternative(html_content, "text/html")
                email.send()
                # ================sending mail to the admin ===============
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
                        </strong><br>
                        <strong>
                        Subject: 
                        </strong>Application recieved from Candidate<br><br>
                    </p>
                    <table cellpadding="5" cellpadding="0">
                    <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
                    <tr><td width="100">Name</td><td>:</td><td>{Name}</td></tr>
                    <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
                    <tr><td>Phone</td><td>:</td><td>{Phone}</td></tr>
                    <tr><td>Experience</td><td>:</td><td>{Experience}</td></tr>
                    <tr><td colspan="3"><strong>Applicant Message Details are as follows:</strong></td></tr>
                    <tr><td>Message</td><td>:</td><td>{Message}</td></tr>
                    <tr><td>Resume</td><td>:</td><td><a href="https://www.vitelglobal.com/media/{NewResume}">{NewResume}</a></td></tr></table><br>
                    <tr><td>For Job Order ID</td><td>:</td><td>{joborderid}</td></tr></table><br>
                    <p>
                        Sincerely, <br><br>
                        Vitel Global Communications, <br>
                        careers@vitelglobal.com
                    </p>
                    """
                Admintext_content = text
                Adminemail = EmailMultiAlternatives(
                    "Job Application - Career Portal",
                    Admintext_content,
                    my_fromEmail,
                    [
                        "mukesh.a@vitelglobal.com", 
                        "hr@pranathiss.com",
                        "shalini@pranathiss.com",
                    ],
                    # cc=["mukesh@vitelglobal.in"],
                    connection=connection,
                )
                Adminemail.content_subtype = "html"
                Adminemail.send()
                return redirect("careers-thankyou")
            else:
                return HttpResponse("Resume already submitted in our portal")
        else:
            return HttpResponse("Invalid File or File not provided")
            # else:
            #     form = CaptchaForm(use_required_attribute=False)
            #     print("Form: ", form)
            #     return render(request, "careers.html", {"form": form})

# Function for Careers Form
# def Careers_list(request):
#     if request.method == "POST":
#         # Client_Key = request.POST["g-recaptcha-response"]
#         # authenticated = captcha_authenticator(Client_Key)
#         # # if authenticated:
#         form = CaptchaForm(request.POST, use_required_attribute=False)
#         if not form.is_valid():
#             return render(
#                 request, "careers.html", {"form": form, "error": "*Invalid Captcha!"}
#             )
#         my_host = "mail.vitelglobal.in"
#         my_port = 587
#         my_username = "careers@vitelglobal.in"
#         my_password = "cHp6u@9gV#fL"
#         my_use_tls = True
#         connection = get_connection(
#             host=my_host,
#             port=my_port,
#             username=my_username,
#             password=my_password,
#             use_tls=my_use_tls,
#         )
#         Name = request.POST.get("cfname")
#         Email = request.POST.get("cemail")
#         Phone = request.POST.get("cphoneno")
#         Experience = request.POST.get("cyear")
#         Message = request.POST.get("cmessage")
#         Resume = request.FILES["formFile"]
#         DateTime = datetime.now(Timezone)
#         DateTime = (str(DateTime)).split(".")[0]
#         RequestedDate = DateTime.split(" ")[0]
#         Resumefile = handle_uploaded_file(Resume, Email)
#         ip_address = get_ip(request)
#         Careers_table(
#             Name=Name,
#             Email=Email,
#             Phone=Phone,
#             Experience=Experience,
#             Message=Message,
#             Resume=Resumefile,
#             Submitted_on=DateTime,
#         ).save()
#         html_content = render_to_string("careers-email.html", {"First_Name": Name})
#         text_content = strip_tags(html_content)
#         email = EmailMultiAlternatives(
#             "We appreciate your interest in Vitelglobal Communications",
#             text_content,
#             "careers@vitelglobal.in",
#             [Email],
#             connection=connection,
#         )
#         email.attach_alternative(html_content, "text/html")
#         email.send()
#         # ================sending mail to the admin ===============
#         text = f"""
#         <p>
#             <strong>
#             From:
#             </strong>
#             {Name} - {Email}<br>
#             <strong>
#             Sent:
#             </strong>{DateTime}<br>
#             <strong>
#             To:
#             </strong> careers@vitelglobal.com<br>
#             <strong>
#             Subject: 
#             </strong>Application recieved from Candidate<br><br>
#         </p>
#         <table cellpadding="5" cellpadding="0">
#         <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
#         <tr><td width="200">Name</td><td>:</td><td>{Name}</td></tr>
#         <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
#         <tr><td>Phone</td><td>:</td><td>{Phone}</td></tr>
#         <tr><td>Years of Experience</td><td>:</td><td>{Experience}</td></tr>
#         <tr><td>Message from Candidate</td><td>:</td><td>{Message}</td></tr>
#         <tr><td>Candidate applied on</td><td>:</td><td>{RequestedDate}</td></tr>
#         <tr><td>IP Address</td><td>:</td><td>{ip_address}</td></tr></table><br>
#         <p>
#             Sincerely, <br><br>
#             Vitel Global Communications, <br>
#             careers@vitelglobal.com
#         </p>
#         """
#         Admintext_content = text
#         Adminemail = EmailMultiAlternatives(
#             "Application recieved from Candidate",
#             Admintext_content,
#             "careers@vitelglobal.in",
#             [
#                 "mukesh.a@vitelglobal.com", 
#                 "hr@pranathiss.com",
#                 "shalini@pranathiss.com",
#             ],
#             # cc=["mukesh@vitelglobal.in"],
#             connection=connection,
#         )
#         Adminemail.content_subtype = "html"
#         Adminemail.attach_file(f"media/{Resumefile}")
#         Adminemail.send()
#         # EmailMessage('Vitelglobal Carrers', 'Hello Aspirant! \nThank you for applying for the vacant post at Vitel Global Communications.\n\nThanks & Regards,\nVitelglobal.in', 'careers@vitelglobal.in', [Email], connection=connection).send(fail_silently=False)
#         data = {
#             "message": f"Hello {Name}! Thank you for applying for the vacant post at Vitel Global Communications.\nOur HR Executive will get in touch with you after going through the details provided by you.\nWe hope to see you on board. Stay safe! Stay Healthy!"
#         }
#         return redirect("careers-thankyou")
#     else:
#         form = CaptchaForm(use_required_attribute=False)
#         print("Form: ", form)
#         return render(request, "careers.html", {"form": form})


def Careers_Thankyou(request):
    return render(request, "careers-thankyou.html")


# Function for Newsletter Subscription
def Newsletter(request):
    if request.method == "POST":
        # Client_Key = request.POST["g-recaptcha-response"]
        # authenticated = captcha_authenticator(Client_Key)
        # if not authenticated:
        #     return redirect("/")
        form = CaptchaForm(request.POST, use_required_attribute=False)
        newsform = CaptchaForm(
            request.POST, use_required_attribute=False, prefix="news"
        )
        print(newsform.data)
        if not newsform.is_valid():
            return render(
                request,
                "index.html",
                {"form": form, "newsform": newsform, "news_error": "*Invalid Captcha!"},
            )

        ip_address = get_ip(request)
        NewsLetterEmail = request.POST.get("newsletteremail")
        if "@" not in NewsLetterEmail:
            return redirect("/")

        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        RequestedDate = DateTime.split(" ")[0]
        Subscribe(
            NewsLetterEmail=NewsLetterEmail,
            Submitted_on=DateTime,
        ).save()
        html_content = render_to_string("subscribe-email.html")
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Thank you for subscribing to our Newsletter",
            text_content,
            settings.EMAIL_HOST_USER,
            [NewsLetterEmail],
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        # ==========sending mail to the admin =============
        text = f"""
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
            </strong> websales@vitelglobal.com<br>
            <strong>
            Subject: 
            </strong>Newsletter Subscription<br><br>
        </p>
        <table cellpadding="5" cellpadding="0">
        <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
        <tr><td width="240">Customer Email</td><td>:</td><td>{NewsLetterEmail}</td></tr>
        <tr><td>Subscribed our Newsletter on</td><td>:</td><td>{RequestedDate}</td></tr></table><br>
        <tr><td>IP Address</td><td>:</td><td>{ip_address}</td></tr></table><br>
        <p>
            Sincerely, <br><br>
            Vitel Global Communications, <br>
            contact@vitelglobal.com
        </p>
        """
        Admintext_content = text
        Adminemail = EmailMultiAlternatives(
            "Newsletter Subscription",
            Admintext_content,
            "contact@vitelglobal.com",
            # ['aman@vitelglobal.com'],
            ["websales@vitelglobal.com"],
            # ['enquiry@vitelglobal.in'],
            # cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
        )
        Adminemail.content_subtype = "html"
        Adminemail.send()
        return redirect("newsletter-thankyou")
    else:
        form = CaptchaForm(use_required_attribute=False)
        newsform = CaptchaForm(use_required_attribute=False, prefix="news")
        return render(request, "index.html", {"form": form, "newsform": newsform})


def Newsletter_Thankyou(request):
    return render(request, "newsletter-thankyou.html")


# 1) Function Contact Form
def contact(request):
    if request.method == "POST":
        # Client_Key = request.POST["g-recaptcha-response"]
        # authenticated = captcha_authenticator(Client_Key)
        # if authenticated:
        form = CaptchaForm(request.POST, use_required_attribute=False)
        if not form.is_valid():
            return render(
                request, "contact.html", {"form": form, "error": "*Invalid Captcha!"}
            )
        ip_address = get_ip(request)
        Name = request.POST.get("yourname")
        Organization_Name = request.POST.get("yourorganization")
        Mobile = request.POST.get("yourphone")
        Email = request.POST.get("youremail")
        Message = request.POST.get("yourmessage")
        whom_email = request.POST.get("whom_vitel")
        HowYouKnow = request.POST.get("howyouknow")
        terms = request.POST.get("terms")
        terms_and_conditions = True
        t_and_c = "Agreed"
        if terms is None:
            terms_and_conditions = False
            t_and_c = "Disagree"
        # if HowYouKnow == 'Others':
        #     HowYouKnow = request.POST.get("otherstext")
        if whom_email == "support@vitelglobal.com":
            send_email_list = ["support@vitelglobal.com", 'websales@vitelglobal.com']
        else:
            send_email_list = ["websales@vitelglobal.com"]
        # print(whom_email)
        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        Date = DateTime.split(" ")[0]
        ContactUs(
            Name=Name,
            Organization_Name=Organization_Name,
            Mobile=Mobile,
            Email=Email,
            Message=Message,
            HowYouKnow=HowYouKnow,
            Whom_to_send=whom_email,
            Submitted_on=DateTime,
            terms_and_conditions=terms_and_conditions,
        ).save()
        html_content = render_to_string("contactus-email.html", {"First_Name": Name})
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
            </strong> {whom_email}<br>
            <strong>
            Subject: 
            </strong>Requested Quote - Contact Us <br><br>
        </p>
        <table cellpadding="5" cellpadding="0">
        <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
        <tr><td width="100">Name</td><td>:</td><td>{Name}</td></tr>
        <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
        <tr><td>Phone</td><td>:</td><td>{Mobile}</td></tr>
        <tr><td colspan="3"><strong>Customer Message Details are as follows:</strong></td></tr>
        <tr><td>Message</td><td>:</td><td>{Message}</td></tr>
        <tr><td>Where did you hear about us</td><td>:</td><td>{HowYouKnow}</td></tr>
        <tr><td>Requested Quote on</td><td>:</td><td>{Date}</td></tr>
        <tr><td>Terms and Conditions</td><td>:</td><td>{t_and_c}</td></tr></table><br>
        <tr><td>IP Address</td><td>:</td><td>{ip_address}</td></tr></table><br>
        <p>
            Sincerely, <br><br>
            Vitel Global Communications, <br>
            contact@vitelglobal.com
        </p>
        """
        Admintext_content = text
        Adminemail = EmailMultiAlternatives(
            "Requested Quote - Contact Us",
            Admintext_content,
            "contact@vitelglobal.com",
            send_email_list
            # ["enquiry@vitelglobal.in"],
            # cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
        )
        Adminemail.content_subtype = "html"
        Adminemail.send()
        return redirect("contactus-thankyou")
    else:
        form = CaptchaForm(use_required_attribute=False)
        return render(request, "contact.html", {"form": form})


# Thankyou Functionfor contactus
def Contactus_Thankyou(request):
    return render(request, "contactus-thankyou.html")


# 2) Function for Get-Rolling form
def get_rolling(request):
    if request.method == "POST":
        ip_address = get_ip(request)
        First_Name = request.POST.get("fname")
        Last_Name = request.POST.get("lastname")
        Email_Id = request.POST.get("email")
        Phone_No = request.POST.get("phoneno")
        Company = request.POST.get("comp")
        Size_Of_Employees = request.POST.get("select")
        How_You_Know_Us = request.POST.get("howyouknow")
        terms = request.POST.get("terms")
        terms_and_conditions = True
        t_and_c = "Agreed"
        if terms is None:
            terms_and_conditions = False
            t_and_c = "Disagree"

        form = CaptchaForm(request.POST, use_required_attribute=False)
        if not form.is_valid():
            return render(
                request,
                "get-rolling.html",
                {"form": form, "error": "*Invalid Captcha!"},
            )
        # else:
        # Client_Key = request.POST["g-recaptcha-response"]
        # authenticated = captcha_authenticator(Client_Key)
        # if authenticated:
        ip_address = get_ip(request)
        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        RequestedDate = DateTime.split(" ")[0]
        KickStart(
            First_Name=First_Name,
            Last_Name=Last_Name,
            Email_Id=Email_Id,
            Phone_No=Phone_No,
            Company=Company,
            Size_Of_Company=Size_Of_Employees,  # this has to be changed to Size of Employees
            How_You_Know_Us=How_You_Know_Us,
            Submitted_on=DateTime,
            terms_and_conditions=terms_and_conditions,
        ).save()
        html_content = render_to_string(
            "getrolling-email.html", {"First_Name": First_Name}
        )
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Thank you for Get Rolling",
            text_content,
            settings.EMAIL_HOST_USER,
            [Email_Id],
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        # ==============sending mail to the admin==================
        text = f"""
        <p>
            <strong>
            From:
            </strong>
            {First_Name} {Last_Name} - {Email_Id}<br>
            <strong>
            Sent:
            </strong>{DateTime}<br>
            <strong>
            To:
            </strong> websales@vitelglobal.com<br>
            <strong>
            Subject: 
            </strong>Requested Quote - Get Rolling<br><br>
        </p>
        <table cellpadding="5" cellpadding="0">
        <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
        <tr><td width="200">Name</td><td>:</td><td>{First_Name} {Last_Name}</td></tr>
        <tr><td>Email</td><td>:</td><td>{Email_Id}</td></tr>
        <tr><td>Phone</td><td>:</td><td>{Phone_No}</td></tr>
        <tr><td colspan="3"><strong>Requested Quote Details are as follows:</strong></td></tr>
        <tr><td>Company Name</td><td>:</td><td>{Company}</td></tr>
        <tr><td>Total No Of Employees</td><td>:</td><td>{Size_Of_Employees}</td></tr>
        <tr><td>How did you hear about us</td><td>:</td><td>{How_You_Know_Us}</td></tr>
        <tr><td>Requested Quote on</td><td>:</td><td>{RequestedDate}</td></tr>
        <tr><td>Terms and Conditions</td><td>:</td><td>{t_and_c}</td></tr></table><br>
        <tr><td>IP Address</td><td>:</td><td>{ip_address}</td></tr></table><br>
        <p>
            Sincerely, <br><br>
            Vitel Global Communications, <br>
            contact@vitelglobal.com
        </p>
        """
        Admintext_content = text
        Adminemail = EmailMultiAlternatives(
            "Requested Quote - Get Rolling",
            Admintext_content,
            "contact@vitelglobal.com",
            ["websales@vitelglobal.com"],
            # ["aman@vitelglobal.com"],
            # cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
        )
        Adminemail.content_subtype = "html"
        Adminemail.send()
        return redirect("getrolling-thankyou")
    else:
        form = CaptchaForm(use_required_attribute=False)
        return render(request, "get-rolling.html", {"form": form})


# Thankyou Function for KickStart
def getrolling_Thankyou(request):
    return render(request, "getrolling-thankyou.html")


def Redirect_to_live_demo(request):
    return redirect("voip-live-demo")

# 3) Function for Live-Demo Form
def voip_live_demo(request):
    if request.method == "POST":
        # Client_Key = request.POST["g-recaptcha-response"]
        # authenticated = captcha_authenticator(Client_Key)
        # if authenticated:
        form = CaptchaForm(request.POST, use_required_attribute=False)
        if not form.is_valid():
            return render(
                request,
                "voip-live-demo.html",
                {"form": form, "error": "*Invalid Captcha!"},
            )
        ip_address = get_ip(request)
        Date = request.POST.get("datepicker")
        # Date = Date.split("/")
        # Date = Date[2] + "-" + Date[0] + "-" + Date[1]
        Time = request.POST.get("time")
        CompanyName = request.POST.get("vcname")
        No_of_users = request.POST.get("vusers")
        FullName = request.POST.get("vfname")
        Designation = request.POST.get("vdesignation")
        Email = request.POST.get("vemail")
        Phone = request.POST.get("vbphone")
        WhereDidYouHear = request.POST.get("vabout_vitel")
        terms = request.POST.get("terms")
        terms_and_conditions = True
        t_and_c = "Agreed"
        if terms is None:
            terms_and_conditions = False
            t_and_c = "Disagree"
        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        RequestedDate = DateTime.split(" ")[0]
        c = Calendar()
        e = Event()
        e.name = (
            f"Vitel Global Live Demo @ Time: {Time} {Date} Eastern Time (US and Canada)"
        )
        e.begin = Date
        e.organizer = "enquiry@vitelglobal.com"
        e.location = (
            "https://us02web.zoom.us/j/9063039626?pwd=elI3Mm1PZ203RjhoZk40Mm1uWCtzdz09"
        )
        e.url = (
            "https://us02web.zoom.us/j/9063039626?pwd=elI3Mm1PZ203RjhoZk40Mm1uWCtzdz09"
        )
        e.description = f"Vitel Global is inviting you to a scheduled Zoom meeting. Topic: Live Demo Date @ Time: {Date} {Time} Eastern Time (US and Canada)"
        c.events
        e.begin = datetime.fromisoformat(f"{Date}T{Time}:00-04:00")
        EndTime = Time.split(":")
        e.end = datetime.fromisoformat(f"{Date}T{str(int(EndTime[0])+1)}:00:00-04:00")
        c.events.add(e)
        with open("invite.ics", "w") as my_file:
            my_file.writelines(c.serialize_iter())
        LiveDemo(
            Date=Date,
            Time=Time + ":00",
            CompanyName=CompanyName,
            No_of_users=No_of_users,
            FullName=FullName,
            Designation=Designation,
            Email=Email,
            Phone=Phone,
            WhereDidYouHear=WhereDidYouHear,
            Submitted_on=DateTime,
            terms_and_conditions=terms_and_conditions,
        ).save()
        # html_content = render_to_string('livedemo-email.html',{'date':Date,'time':Time,'First_Name':FullName})
        # text_content = strip_tags(html_content)
        text_content = f"Hello {FullName}!\nThank you for registering for the live demo. \n\nMeeting Details\n-----------------------------\n\nVitel Global is inviting you to a scheduled Zoom meeting.\n\nTopic: Live Demo @ Time: {Date} {Time} Eastern Time (US and Canada)\n\nJoin Zoom Meeting : https://us02web.zoom.us/j/9063039626?pwd=elI3Mm1PZ203RjhoZk40Mm1uWCtzdz09\n\nMeeting ID: 906 303 9626\n\nPasscode: 8wbDYK\n\nOne tap mobile\n\n+13462487799,,9063039626#,,,,*411053# US (Houston)\n\n+14086380968,,9063039626#,,,,*411053# US (San Jose)\n\nDial by your location\n+1 346 248 7799 US (Houston)\+1 408 638 0968 US (San Jose)\n+1 646 876 9923 US (New York)\n+1 646 876 9923 US (New York)\n+1 669 900 6833 US (San Jose)\n+1 253 215 8782 US (Tacoma)\n+1 301 715 8592 US (Washington DC)\n+1 312 626 6799 US (Chicago)\n+1 301 715 8592 US (Washington DC)\n+1 312 626 6799 US (Chicago)\n\nMeeting ID: 906 303 9626\n\nPasscode: 411053\n\nFind your local number: https://us02web.zoom.us/u/kbXqgMtPOy\n\nSincerely,\n\nVitel Global Communications,\nsupport@vitelglobal.com"
        email = EmailMultiAlternatives(
            f" Vitel Global Live Demo @ Time: {Time} {Date} Eastern Time (US and Canada)",
            text_content,
            settings.EMAIL_HOST_USER,
            [Email],
        )
        email.attach_file("invite.ics")
        email.send()
        # =================== sendimg the mail to the admin =================
        text = f"""
        <p>
            <strong>
            From:
            </strong>
            {CompanyName} - {Email}<br>
            <strong>
            Sent:
            </strong>{DateTime}<br>
            <strong>
            To:
            </strong> websales@vitelglobal.com<br>
            <strong>
            Subject: 
            </strong>Requested Quote - VOIP Live Demo<br><br>
        </p>
        <table cellpadding="5" cellpadding="0">
        <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
        <tr><td width="200">Name</td><td>:</td><td>{FullName}</td></tr>
        <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
        <tr><td>Phone</td><td>:</td><td>{Phone}</td></tr>
        <tr><td colspan="3"><strong>Requested Quote - VoIP Live Demo:</strong></td></tr>
        <tr><td>Company Name</td><td>:</td><td>{CompanyName}</td></tr>
        <tr><td>No. of Users</td><td>:</td><td>{No_of_users}</td></tr>
        <tr><td>Designation</td><td>:</td><td>{Designation}</td></tr>
        <tr><td>Where did you hear about us?</td><td>:</td><td>{WhereDidYouHear}</td></tr>
        <tr><td>Date for Live Demo</td><td>:</td><td>{Date}</td></tr>
        <tr><td>Time for Live Demo</td><td>:</td><td>{Time}</td></tr>
        <tr><td>Url for Live Demo</td><td>:</td><td> https://us02web.zoom.us/j/9063039626?pwd=elI3Mm1PZ203RjhoZk40Mm1uWCtzdz09</td></tr>
        <tr><td>Requested Quote on</td><td>:</td><td>{RequestedDate}</td></tr>
        <tr><td>Terms and Conditions</td><td>:</td><td>{t_and_c}</td></tr></table><br>
        <tr><td>IP Adress</td><td>:</td><td>{ip_address}</td></tr></table><br>
        <p>
            Sincerely, <br><br>
            Vitel Global Communications, <br>
            contact@vitelglobal.com
        </p>
        """
        Admintext_content = text
        Adminemail = EmailMultiAlternatives(
            "Requested Quote - VOIP Live Demo",
            Admintext_content,
            "contact@vitelglobal.com",
            ["websales@vitelglobal.com"],
            # ["enquiry@vitelglobal.in"],
            # cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
        )
        Adminemail.content_subtype = "html"
        Adminemail.send()
        return redirect("live-demo-thankyou")
    else:
        form = CaptchaForm(use_required_attribute=False)
        return render(request, "voip-live-demo.html", {"form": form})


# Thankyou Function for Live-demo
def Live_Demo_Thankyou(request):
    return render(request, "live-demo-thankyou.html")


# 4) Function for feedback form
def Feedback(request):
    if request.method == "POST":
        # Client_Key = request.POST["g-recaptcha-response"]
        # authenticated = captcha_authenticator(Client_Key)
        # if authenticated:

        form = CaptchaForm(request.POST, use_required_attribute=False)
        feedform = CaptchaForm(
            request.POST, use_required_attribute=False, prefix="feed"
        )
        if not feedform.is_valid():
            return render(
                request,
                "index.html",
                {
                    "form": form,
                    "feedform": feedform,
                    "feedback_error": "*Invalid Captcha!",
                },
            )

        ip_address = get_ip(request)
        QualityService = request.POST.get("ktiming")
        CustomerService = request.POST.get("kmatch")
        Email = request.POST.get("kcomp")
        Suggestion = request.POST.get("comments")
        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        Feedback_table(
            QualityService=QualityService,
            CustomerService=CustomerService,
            Email=Email,
            Suggestion=Suggestion,
            Submitted_on=DateTime,
        ).save()
        html_content = render_to_string("feedback-email.html")
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Thank you for your feedback",
            text_content,
            settings.EMAIL_HOST_USER,
            [Email],
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        # ===========sending mail to the admin=========
        text = f"""
        <p>
            <strong>
            From:
            </strong>
            {Email}<br>
            <strong>
            Sent:
            </strong>{DateTime}<br>
            <strong>
            To:
            </strong> websales@vitelglobal.com<br>
            <strong>
            Subject: 
            </strong>Customer - Feedback <br><br>
        </p>
        <table cellpadding="5" cellpadding="0">
        <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
        <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
        <tr><td colspan="3"><strong>Feedback From the Customer:</strong></td></tr>
        <tr><td>Quality of Service</td><td>:</td><td>{QualityService}/5</td></tr>
        <tr><td>Customer Service:</td><td>:</td><td>{CustomerService}/5</td></tr>
        <tr><td>Suggestion</td><td>:</td><td>{Suggestion}</td></tr></table><br>
        <tr><td>IP Address</td><td>:</td><td>{ip_address}</td></tr></table><br>
        <p>
            Sincerely, <br><br>
            Vitel Global Communications, <br>
            contact@vitelglobal.com
        </p>
        """
        Admintext_content = text
        Adminemail = EmailMultiAlternatives(
            "Customer - Feedback ",
            Admintext_content,
            "contact@vitelglobal.com",
            ["websales@vitelglobal.com"],
            # ["aman@vitelglobal.com"],
            # cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
        )
        Adminemail.content_subtype = "html"
        Adminemail.send()
        return redirect("feedback-thankyou")
    else:
        form = CaptchaForm(use_required_attribute=False)
        feedform = CaptchaForm(use_required_attribute=False, prefix="feed")
        return render(request, "index.html", {"form": form, "feedform": feedform})


def Feedback_Thankyou(request):
    return render(request, "feedback-thankyou.html")


# 5) Function for Partners Programm
def partners(request):
    if request.method == "POST":
        # Client_Key = request.POST["g-recaptcha-response"]
        # authenticated = captcha_authenticator(Client_Key)
        # if authenticated:
        form = CaptchaForm(request.POST, use_required_attribute=False)
        if not form.is_valid():
            return render(
                request, "partners-program.html", {"form": form, "error": "*Invalid Captcha!"}
            )
        ip_address = get_ip(request)
        FirstName = request.POST.get("partner_fname")
        LastName = request.POST.get("partner_lname")
        Company = request.POST.get("partner_company")
        State = request.POST.get("partner_state")
        Email = request.POST.get("partner_email")
        Phone = request.POST.get("partner_phone")
        terms = request.POST.get("terms")
        terms_and_conditions = True
        t_and_c = "Agreed"
        if terms is None:
            terms_and_conditions = False
            t_and_c = "Disagree"
        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        Date = DateTime.split(" ")[0]
        Partner_Program(
            FirstName=FirstName,
            LastName=LastName,
            Company=Company,
            State=State,
            Email=Email,
            Phone=Phone,
            Submitted_on=DateTime,
            terms_and_conditions=terms_and_conditions,
        ).save()
        html_content = render_to_string(
            "partners-email.html", {"First_Name": FirstName}
        )
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Partner Program - Vitel Global",
            text_content,
            settings.EMAIL_HOST_USER,
            [Email],
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        # ================sending mail to the admin ==========
        text = f"""
        <p>
            <strong>
            From:
            </strong>
            {FirstName} {LastName} - {Email}<br>
            <strong>
            Sent:
            </strong>{DateTime}<br>
            <strong>
            To:
            </strong> websales@vitelglobal.com <br>
            <strong>
            Subject: 
            </strong>Requested Quote - Partners Program <br><br>
        </p>
        <table cellpadding="5" cellpadding="0">
        <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
        <tr><td width="100">Name</td><td>:</td><td>{FirstName} {LastName}</td></tr>
        <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
        <tr><td>Phone</td><td>:</td><td>{Phone}</td></tr>
        <tr><td>Company</td><td>:</td><td>{Company}</td></tr>
        <tr><td>State</td><td>:</td><td>{State}</td></tr>
        <tr><td>Requested Quote on</td><td>:</td><td>{Date}</td></tr>
        <tr><td>Terms and Conditions</td><td>:</td><td>{t_and_c}</td></tr></table><br>
        <tr><td>IP Address</td><td>:</td><td>{ip_address}</td></tr></table><br>
        <p>
            Sincerely, <br><br>
            Vitel Global Communications, <br>
            contact@vitelglobal.com
        </p>
        """
        Admintext_content = text
        Adminemail = EmailMultiAlternatives(
            "Requested Quote - Partner Program",
            Admintext_content,
            "contact@vitelglobal.com",
            ["websales@vitelglobal.com"],
            # ["aman@vitelglobal.com"],
            # cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
        )
        Adminemail.content_subtype = "html"
        Adminemail.send()
        data = {
            "message": "Thank you for showing your interest in our Partner Program. Partnering with VitelGlobal is an opportunity where you or your organization can partner with us for various events. "
        }
        return redirect("partners-thankyou")
    else:
        form = CaptchaForm(use_required_attribute=False)
        return render(request, "partners-program.html", {"form": form})


def partners_Thankyou(request):
    return render(request, "partners-thankyou.html")


# ==========Functions for E-Books and Whitepapers====================

# def ebook_page(request, ebook):
#     dep_obj= Ebook_pdf.objects.filter(perma_link=ebook)
#     if dep_obj:
#         return render(request, "e-book-page.html", {'EBookdata':dep_obj})
#     else:
#         return redirect('/')


def ebook_page(request, ebook):
    obj = Ebook_pdf.objects.filter(perma_link=ebook).first()
    if obj:
        form = CaptchaForm(use_required_attribute=False)
        return render(request, "e-books-page.html", {"EBookdata": obj, "form": form})
    else:
        return redirect("/")


def e_books(request):
    if request.method == "POST":
        # Client_Key = request.POST["g-recaptcha-response"]
        # authenticated = captcha_authenticator(Client_Key)
        # if authenticated:
        form = CaptchaForm(request.POST, use_required_attribute=False)
        if not form.is_valid():
            EBookdata = Ebook_pdf.objects.all().order_by("-enumber")
            return render(
                request,
                "e-books.html",
                {"form": form, "error": "*Invalid Captcha!", "EBookdata": EBookdata},
            )
        ip_address = get_ip(request)
        Name = request.POST.get("yourname")
        Mobile = request.POST.get("yourphone")
        Email = request.POST.get("youremail")
        CompanyName = request.POST.get("yourorganization")
        Ebookid = request.POST.get("ebookid")
        Ebook = Ebook_pdf.objects.get(enumber=Ebookid)
        Ebook_link = Ebook.ebook_pdf
        Title = Ebook.title
        # print(Title)
        # print(Ebook_link)
        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        Date = DateTime.split(" ")[0]
        Ebook_Download(
            Name=Name,
            Mobile=Mobile,
            Email=Email,
            CompanyName=CompanyName,
            submitted_on=DateTime,
        ).save()
        html_content = render_to_string(
            "ebooks-mail.html", {"First_Name": Name, "Ebook_link": Ebook_link}
        )
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Thank you for Downloading Our E-Book",
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
            </strong> websales@vitelglobal.com<br>
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
        <tr><td>IP Address</td><td>:</td><td>{ip_address}</td></tr></table><br>
        <p>
            Sincerely, <br>
            Vitel Global Communications, <br>
            contact@vitelglobal.com
        </p>
        """
        Admintext_content = text
        Adminemail = EmailMultiAlternatives(
            "Vitelglobal - E_Book",
            Admintext_content,
            "contact@vitelglobal.com",
            ["websales@vitelglobal.com"],
            # ["enquiry@vitelglobal.in"],
            # cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
        )
        Adminemail.content_subtype = "html"
        Adminemail.send()
        return redirect("e-books-thankyou")
    else:
        EBookdata = Ebook_pdf.objects.all().order_by("-enumber")
        form = CaptchaForm(use_required_attribute=False)
        return render(request, "e-books.html", {"EBookdata": EBookdata, "form": form})


def e_books_Thankyou(request):
    return render(request, "ebooks-thankyou.html")


def whitepapers_page(request, whitepaper):
    Whitepaperdata = Whitepaper_pdf.objects.filter(perma_link=whitepaper).first()
    if Whitepaperdata:
        form = CaptchaForm(use_required_attribute=False)
        return render(
            request,
            "white-papers-page.html",
            {"Whitepaperdata": Whitepaperdata, "form": form},
        )
    else:
        return redirect("/")


def white_papers(request):
    if request.method == "POST":
        # Client_Key = request.POST["g-recaptcha-response"]
        # authenticated = captcha_authenticator(Client_Key)
        # if authenticated:
        form = CaptchaForm(request.POST, use_required_attribute=False)
        if not form.is_valid():
            Whitepaperdata = Whitepaper_pdf.objects.all().order_by("-wnumber")
            return render(
                request,
                "white-papers.html",
                {
                    "form": form,
                    "error": "*Invalid Captcha!",
                    "Whitepaperdata": Whitepaperdata,
                },
            )
        ip_address = get_ip(request)
        Name = request.POST.get("yourname")
        Mobile = request.POST.get("yourphone")
        Email = request.POST.get("youremail")
        CompanyName = request.POST.get("yourorganization")
        Wpaperid = request.POST.get("wpaperid")
        wpaper = Whitepaper_pdf.objects.get(wnumber=Wpaperid)
        wpaper_link = wpaper.whitepaper_pdf
        Title = wpaper.title
        # print(wpaper_link)
        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        Date = DateTime.split(" ")[0]
        Whitepaper_Download(
            Name=Name,
            Mobile=Mobile,
            Email=Email,
            CompanyName=CompanyName,
            submitted_on=DateTime,
        ).save()
        html_content = render_to_string(
            "whitepaper-email.html",
            {"First_Name": Name, "wpaper_link": wpaper_link},
        )
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Thank you for Downloading Our Whitepaper",
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
            </strong> websales@vitelglobal.com<br>
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
        <tr><td>IP Address</td><td>:</td><td>{ip_address}</td></tr></table><br>
        <p>
            Sincerely, <br>
            Vitel Global Communications, <br>
            contact@vitelglobal.com
        </p>
        """
        Admintext_content = text
        Adminemail = EmailMultiAlternatives(
            "Vitelglobal - Whitepaper",
            Admintext_content,
            "contact@vitelglobal.com",
            # ["suresh.k@vitelglobal.com","ashok.n@vitelglobal.com"],
            ["websales@vitelglobal.com"],
            # ["enquiry@vitelglobal.in"],
            # cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
        )
        Adminemail.content_subtype = "html"
        Adminemail.send()
        return redirect("white-papers-thankyou")
    else:
        Whitepaperdata = Whitepaper_pdf.objects.all().order_by("-wnumber")
        form = CaptchaForm(use_required_attribute=False)
        return render(
            request,
            "white-papers.html",
            {"Whitepaperdata": Whitepaperdata, "form": form},
        )


def white_papers_Thankyou(request):
    return render(request, "whitepapers-thankyou.html")


# Landing Page
def landing_page_business_phone(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST, use_required_attribute=False)
        ip_address = get_ip(request)
        name = request.POST.get("fname")
        phone = request.POST.get("phoneno")
        company_name = request.POST.get("comp")
        UserEmail = request.POST.get("email")
        DateTime = datetime.now(Timezone)
        DateTime = (str(DateTime)).split(".")[0]
        RequestedDate = DateTime.split(" ")[0]

        # if not form.is_valid():
        #     return render(
        #         request, "businessphone.html", {"form": form, "error": "*Invalid Captcha!"}
        #     )
        Get_Quote(
            Name = name,
            phonenumber = phone,
            Email_Id = UserEmail,
            CompanyName = company_name,
        ).save()
        html_content = render_to_string(
            "business-landign-email.html", {"First_Name": name}
        )
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "Thank you for Get Quote",
            text_content,
            settings.EMAIL_HOST_USER,
            [UserEmail],
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        # ==============sending mail to the admin==================
        text = f"""
        <p>
            <strong>
            From:
            </strong>
            {name} - {UserEmail}<br>
            <strong>
            Sent:
            </strong>{DateTime}<br>
            <strong>
            To:
            </strong> websales@vitelglobal.com<br>
            <strong>
            Subject: 
            </strong>Requested Get Quote<br><br>
        </p>
        <table cellpadding="5" cellpadding="0">
        <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
        <tr><td width="200">Name</td><td>:</td><td>{name}</td></tr>
        <tr><td>Email</td><td>:</td><td>{UserEmail}</td></tr>
        <tr><td>Phone</td><td>:</td><td>{phone}</td></tr>
        <tr><td colspan="3"><strong>Requested Get Quote Details are as follows:</strong></td></tr>
        <tr><td>Company Name</td><td>:</td><td>{company_name}</td></tr>
        <tr><td>Requested Quote on</td><td>:</td><td>{RequestedDate}</td></tr></table><br>
        <tr><td>IP Address</td><td>:</td><td>{ip_address}</td></tr></table><br>
        <p>
            Sincerely, <br><br>
            Vitel Global Communications, <br>
            contact@vitelglobal.com
        </p>
        """
        Admintext_content = text
        Adminemail = EmailMultiAlternatives(
            "Requested - Get Quote",
            Admintext_content,
            "contact@vitelglobal.com",
            ["websales@vitelglobal.com"],
            # ["suresh.k@pranathiss.com"],
            # cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
        )
        Adminemail.content_subtype = "html"
        Adminemail.send()
        return redirect("businessphone-thankyou")
    else:
        form = CaptchaForm(use_required_attribute=False)
        return render(request, "businessphone.html", {"form": form})

def business_phone_thankyou(request):
    return render(request, "thankyou-quote.html")


from datetime import timedelta

def request_demo_land_page(request):
    if request.method == 'POST':
        ip_address = get_ip(request)
        Date = request.POST.get("date")
        Time = request.POST.get("time")
        UserEmail = request.POST.get("demail")
        UserName = request.POST.get("uname")
        PhoneNumber = request.POST.get("phonenumber")
        form = CaptchaForm(request.POST, use_required_attribute=False)
        # if not form.is_valid():
        #     return render(
        #         request, "businessphone.html", {"form": form, "error": "*Invalid Captcha!"}
        #     )
        c = Calendar()
        e = Event()
        e.name = (
            f"Vitel Global Live Demo @ Time: {Time} {Date} Eastern Time (US and Canada)"
        )
        e.begin = Date
        e.organizer = "enquiry@vitelglobal.com"
        e.location = (
            "https://us02web.zoom.us/j/9063039626?pwd=elI3Mm1PZ203RjhoZk40Mm1uWCtzdz09"
        )
        e.url = (
            "https://us02web.zoom.us/j/9063039626?pwd=elI3Mm1PZ203RjhoZk40Mm1uWCtzdz09"
        )
        e.description = f"Vitel Global is inviting you to a scheduled Zoom meeting. Topic: Live Demo Date @ Time: {Date} {Time} Eastern Time (US and Canada)"
        c.events
        e.begin = datetime.fromisoformat(f"{Date}T{Time}:00-04:00")
        EndTime = Time.split(":")
        e.end = datetime.fromisoformat(f"{Date}T{str(int(EndTime[0])+1)}:00:00-04:00")
        c.events.add(e)
        with open("invite.ics", "w") as my_file:
            my_file.writelines(c.serialize_iter())
        Request_Demo_Now(
            Selected_date = Date,
            Time = Time,
            Email_Id = UserEmail,
            Name = UserName,
            PhoneNumber = PhoneNumber,
        ).save()
        text_content = f"Hello {UserName}!\nThank you for registering for the live demo. \n\nMeeting Details\n-----------------------------\n\nVitel Global is inviting you to a scheduled Zoom meeting.\n\nTopic: Live Demo @ Time: {Date} {Time} Eastern Time (US and Canada)\n\nJoin Zoom Meeting : https://us02web.zoom.us/j/9063039626?pwd=elI3Mm1PZ203RjhoZk40Mm1uWCtzdz09\n\nMeeting ID: 906 303 9626\n\nPasscode: 8wbDYK\n\nOne tap mobile\n\n+13462487799,,9063039626#,,,,*411053# US (Houston)\n\n+14086380968,,9063039626#,,,,*411053# US (San Jose)\n\nDial by your location\n+1 346 248 7799 US (Houston)\+1 408 638 0968 US (San Jose)\n+1 646 876 9923 US (New York)\n+1 646 876 9923 US (New York)\n+1 669 900 6833 US (San Jose)\n+1 253 215 8782 US (Tacoma)\n+1 301 715 8592 US (Washington DC)\n+1 312 626 6799 US (Chicago)\n+1 301 715 8592 US (Washington DC)\n+1 312 626 6799 US (Chicago)\n\nMeeting ID: 906 303 9626\n\nPasscode: 411053\n\nFind your local number: https://us02web.zoom.us/u/kbXqgMtPOy\n\nSincerely,\n\nVitel Global Communications,\nsupport@vitelglobal.com"
        email = EmailMultiAlternatives(
            f" Vitel Global Live Demo @ Time: {Time} {Date} Eastern Time (US and Canada)",
            text_content,
            settings.EMAIL_HOST_USER,
            [UserEmail],
        )
        email.attach_file("invite.ics")
        email.send()
        # ==============sending mail to the admin==================
        text = f"""
        <p>
            <strong>
            From:
            </strong>
            {UserName} - {UserEmail}<br>
            <strong>
            Sent:
            </strong>{Date}-{Time}<br>
            <strong>
            To:
            </strong> websales@vitelglobal.com<br>
            <strong>
            Subject: 
            </strong>Requested For Demo Now<br><br>
        </p>
        <table cellpadding="5" cellpadding="0">
        <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
        <tr><td>Name</td><td>:</td><td>{UserName}</td></tr>
        <tr><td>Phone Number</td><td>:</td><td>{PhoneNumber}</td></tr>
        <tr><td>Email</td><td>:</td><td>{UserEmail}</td></tr>
        <tr><td>Date for Live Demo</td><td>:</td><td>{Date}</td></tr>
        <tr><td>Time for Live Demo</td><td>:</td><td>{Time}</td></tr>
        <tr><td>Url for Live Demo</td><td>:</td><td> https://us02web.zoom.us/j/9063039626?pwd=elI3Mm1PZ203RjhoZk40Mm1uWCtzdz09</td></tr>
        <tr><td>IP Address</td><td>:</td><td>{ip_address}</td></tr></table><br>
        <p>
            Sincerely, <br><br>
            Vitel Global Communications, <br>
            contact@vitelglobal.com
        </p>
        """
        Admintext_content = text
        Adminemail = EmailMultiAlternatives(
            "Requested For Demo",
            Admintext_content,
            "contact@vitelglobal.com",
            # ["suresh.k@pranathiss.com"],
            ["websales@vitelglobal.com"],
            # ["enquiry@vitelglobal.in"],
            # cc=["mukesh@vitelglobal.in","salman@vitelglobal.in","kumar@vitelglobal.in","vamsi@vitelglobal.in","sajid@vitelglobal.in","jimmy.kola@vitelglobal.in","vamsi@vitelglobal.com","rajashekar@vitelglobal.com","shamim.ahmad@vitelglobal.com"]
        )
        Adminemail.content_subtype = "html"
        Adminemail.send()

        return redirect("demo-thankyou")
    else:
        form = CaptchaForm(use_required_attribute=False)
        return render(request, "businessphone.html", {"form": form})
    
def thankyou_demo_land(request):
    return render(request, "thankyou-demo.html")

# Thankyou for unsubscribe
def Unsubscribe_Thankyou(request):
    return render(request, "unsubscribe-thankyou.html")

############### Un- Subscription #####################

def unsubscribe(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST, use_required_attribute=False)
        if not form.is_valid():
            return render(
                request, "unsubscribe.html", {"form": form, "error": "*Invalid Captcha!"}
            )
        yourname = request.POST.get('yourname')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        unsubscribe_promotional = 'checkme' in request.POST
        unsubscribe_notifications = 'checkmes' in request.POST
        unsubscribe_all = 'checkmed' in request.POST
        ip_address = get_ip(request)
        submission_date = timezone_now().date()
        date_time = timezone_now()
        print("CheckBoxes",unsubscribe_promotional,unsubscribe_notifications,unsubscribe_all)

        # Save the data to the database
        unsubscribe_request = UnsubscribeRequest.objects.create(
            yourname=yourname,
            email=email,
            phoneno=phoneno,
            unsubscribe_promotional=unsubscribe_promotional,
            unsubscribe_notifications=unsubscribe_notifications,
            unsubscribe_all=unsubscribe_all
        )
        promotional = "Active"
        if unsubscribe_promotional:
            promotional="InActive"
        notifications = "Active"
        if unsubscribe_notifications:
            notifications = "InActive"
        all="Active"
        if unsubscribe_all:
            all="InActive"
        print("ALL", promotional,notifications,all)
        email_context = {
                "name":yourname,
                "phone_number":phoneno,
                "email":email,
                "ip_adress":ip_address,
                "submission_date":submission_date,
                "date_time":date_time,
                "promotional":promotional,
                "notifications":notifications,
                "all":all
            }
        ######## Send Mail to User ##########
        body = render_to_string(
            template_name="mails/unsubscribe-email.html", 
            context= email_context
        )
        data={
            "subject":"Un-Subscription",
            "body":body,
            "to_email":email
        }
        Util.send_email(data,is_content_html=True)
        
        ########  Send Email to Admin #######
        body2 = render_to_string(
            template_name="mails/un-subscribe.html", 
            context= email_context
        ) 
        data2={
            "subject":"Request for Un-Subscription",
            "body":body2,
            "to_email":"suresh.k@pranathiss.com"
        }
        Util.send_email(data2,is_content_html=True)
            

        # Redirect to a thank you page or any other page after successful submission
        return redirect('unsubscribe-thankyou')  # Change '/thank-you/' to your desired URL

    return render(request, 'unsubscribe.html')  # Change 'unsubscribe.html' to your template name


####################### NEW URL Redirections ####################

# ---------------------------------------------
def texas(request):
    return redirect('business-texas', permanent=True)
def new_texas(request):
    return render(request, "texas.html")
#-----------------------------------------------

def california(request):
    return redirect('business-california', permanent=True)
def new_california(request):
    return render(request, "california.html")
#---------------------------------------------

def florida(request):
    return redirect('business-florida', permanent=True)
def new_florida(request):
    return render(request, "florida.html")
#-----------------------------------------------

def hawaii(request):
    return redirect('business-hawaii', permanent=True)
def new_hawaii(request):
    return render(request, "hawaii.html")
#-------------------------------------------------

def indiana(request):
    return redirect('business-indiana', permanent=True)
def new_indiana(request):
    return render(request, "indiana.html")
#-----------------------------------------------

def business_phone_features(request):
    return redirect('business-phone-features', permanent=True)
def new_business_phone_features(request):
    return render(request, "business-phone-features.html")
#-------------------------------------

def business_phone_features(request):
    return redirect('business-phone-features', permanent=True)
def new_business_phone_features(request):
    return render(request, "business-phone-features.html")
#-----------------------------------

def cloud_pbx_phone_system(request):
    return redirect("cloud-pbx-phone-system", permanent=True)
def new_cloud_pbx_phone_system(request):
    return render(request, "cloud-pbx-phone-system.html")
#------------------------------------------

def cloud_pbx_phone_system(request):
    return redirect("cloud-pbx-phone-system", permanent=True)
def new_cloud_pbx_phone_system(request):
    return render(request, "cloud-pbx-phone-system.html")



# ======= Viteldevelopment Code ===========

from rest_framework.views import APIView
from .utils import number_portablity_check, format_api_response, get_vitelity_tollfree_dids,get_voip_innovations_local_dids,get_vitelity_local_dids
from rest_framework import status

# ------ Viteldevelopment Code ---------
def setup_plan(request):
       
        if request.method == "POST":      
            toggler = request.POST.get("toggler")
            
            if toggler !='null':
                if toggler=='yes':
                    selectedstate = request.POST.get("stateselect")
                    selected_dids = request.POST.getlist("selected_dids")
                
                elif toggler=='no':
                    toll_free_number = request.POST.get("toll_free_number")
                    selected_dids = request.POST.get("toll_free_numbers")

                elif toggler=='check':
                    selected_dids = request.POST.get("portable_number")
                ip_address = get_ip(request)
                quantity  = request.POST.get("quant[1]") 
                firstname = request.POST.get("firstname")            
                lastname = request.POST.get("lastname")
                password = request.POST.get("password")
                Mobile = request.POST.get("Mobile")
                Email = request.POST.get("youremail")
                Businessname = request.POST.get("Businessname")
                Businessaddress = request.POST.get("Businessaddress")
                Suite = request.POST.get("Suite")
                city = request.POST.get("city")        
                zipcode = request.POST.get("zipcode")
                Suite = request.POST.get("Suite")
                state = request.POST.get("state")
                country = request.POST.get("country")
                
                DateTime = datetime.now(Timezone)
                DateTime = (str(DateTime)).split(".")[0]
                Date = DateTime.split(" ")[0]
                
                setup_plans(
                        firstname=firstname,
                        quantity=quantity,
                        lastname=lastname,
                        password=password,
                        email=Email,
                        mobile=Mobile,
                        businessname=Businessname,
                        businessaddress=Businessaddress,
                        Suite  = Suite,
                        city  = city,
                        zipcode = zipcode,
                        state = state,
                        country = country,
                        dids  = selected_dids,                            
                    ).save()
                
                html_content = render_to_string("contactus-email.html", {"First_Name": firstname})
                text_content = strip_tags(html_content)
                email = EmailMultiAlternatives(
                    "Thank you for Register",
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
                    {firstname} - {lastname}<br>
                    <strong>
                    Sent:
                    </strong>{Email}<br>
                    <strong>
                    Mobile:
                    </strong> {Mobile}<br>
                    <strong>
                    Subject: 
                    </strong>Register - Setup Plan <br><br>
                </p>
                <table cellpadding="5" cellpadding="0">
                <tr><td colspan="3"><strong>Personal Details :</strong></td></tr>
                <tr><td width="100">Name</td><td>:</td><td>{firstname} {lastname} </td></tr>
                <tr><td>Email</td><td>:</td><td>{Email}</td></tr>
                <tr><td>Phone</td><td>:</td><td>{Mobile}</td></tr>
                <tr><td>Selected Number </td><td>:</td><td>{selected_dids}</td></tr>
                <tr><td>Quantity</td><td>:</td><td>{quantity }</td></tr>
                <tr><td>Password</td><td>:</td><td>{password}</td></tr>
                <tr><td>Business Name</td><td>:</td><td>{Businessname}</td></tr>
                <tr><td>Business Address</td><td>:</td><td>{Businessaddress}</td></tr>
                <tr><td>Suite</td><td>:</td><td>{Suite}</td></tr>
                <tr><td>City</td><td>:</td><td>{city}</td></tr>
                <tr><td>Country</td><td>:</td><td>{country}</td></tr>
                <tr><td>State</td><td>:</td><td>{state}</td></tr>
                <tr><td>Zipcode</td><td>:</td><td>{zipcode}</td></tr>
                <tr><td>Requested Quote on</td><td>:</td><td>{Date}</td></tr></table><br>
                <tr><td>IP Adress</td><td>:</td><td>{ip_address}</td></tr>

                </table>
                
                <p>
                    Sincerely, <br><br>
                    Vitel Global Communications, <br>
                    contact@vitelglobal.com
                </p>
                """                
                
                Admintext_content = text
                Adminemail = EmailMultiAlternatives(
                    "Register for Contact-Us",
                    Admintext_content,
                    "contact@vitelglobal.com",
                    # ["suresh.k@pranathiss.com"]
                    ["websales@vitelglobal.com"],
                    
                )
                Adminemail.content_subtype = "html"
                Adminemail.send()
                return redirect("contactus-thankyou")
            else:
                print('please select the values')
                monthlyCost = '25.99'
                return render(request, 'setup_plan.html',{"monthlyCost": monthlyCost})
        else:
            monthlyCost = '25.99'
            return render(request, 'setup_plan.html',{"monthlyCost": monthlyCost})
        
class number_portablity(APIView):  

    def post(self, request):
        try:  
            
            tn       = request.data.get('number')                      
                            
            
            voip_inno_portable   = number_portablity_check(tn)

            response              = voip_inno_portable
            if response==True:
                message     = str(tn) + " is Portable"
                error_code  = 200
            else:
                message     = str(tn) + " is not Portable"
                error_code  = 200    

           
        except Exception as e: 
            print(e)
            message     = "Error"
            error_code  = 500
            response    = False

        return format_api_response(response, message, error_code)
    

# To get local did list using 4 vendor APIs
class getTollFreeDids(APIView):

    def post(self, request, *args, **kwargs):
        try:              
           
            if request.method == 'POST': 
               
                keyword     = request.data.get('keyword')
                       
                vitelity_dids       = get_vitelity_tollfree_dids(keyword)
                

                combined_array = []
                # Check if each variable is not empty and then combine them
                if vitelity_dids:
                    combined_array.extend(vitelity_dids)
                                  
                
                sorted_data_array = sorted(combined_array, key=lambda item: int(item['number']))
                # print(sorted_data_array)

                did_count           = len(combined_array)
                if did_count > 0:
                    message     = "Success"
                    error_code  = 200
                    response_data   = {'data':sorted_data_array}
                else:
                    message     = "No data available"
                    error_code  = status.HTTP_204_NO_CONTENT 
                    response_data   = {'data':{}}

               
                
            else:
                message     = "This API endpoint only accepts POST requests"
                error_code  = 405 
                response_data   = {'data':{}}
        
                      
        except Exception as e: 
            print(e)
            message     = "Error"
            error_code  = 500
            response_data        = {'data':{}}

        return format_api_response(response_data, message, error_code)
    
# To get local did list using 4 vendor APIs
class getLocalDids(APIView):

    def post(self, request, *args, **kwargs): 
        try:  
            
            combined_array = []
            
            try:
                if request.method == 'POST':                    
                                   
                            if request.data.get('state'):
                                
                                state       = request.data.get('state')  
                                 
                                
                                if state == "": 
                                    message     = "Please select state"
                                    error_code  = 500 
                                else:
                                    
                                    vitelity_local_dids    = get_vitelity_local_dids(state)                                    

                                    
                                    if vitelity_local_dids:
                                        combined_array.extend(vitelity_local_dids)
                                    
                                    
                                    sorted_data_array = sorted(combined_array, key=lambda item: int(item['number']))				        

                                    did_count               = len(sorted_data_array)
                                    
                                    if did_count > 0:
                                        message     = "Success"
                                        error_code  = 200
                                    else:
                                        message     = "No data available"
                                        error_code  = status.HTTP_204_NO_CONTENT
                                    response_data   = {
                                                    'data': sorted_data_array                                                    
                                                }

                            else:
                                message     = "Please select type"
                                error_code  = 500 
                            # Session creation
                           
                       
                else:
                    message     = "This API endpoint only accepts POST requests"
                    error_code  = 405 
                
                return format_api_response(response_data, message, error_code)
            

               
            except:
                message     = "Error"
                error_code  = 500
                response_data= {'data':{}}
                   
        except Exception as e: 
            print(e)
            message     = "Error"
            error_code  = 500
            response_data        = {'data':{}}

        return format_api_response(response_data, message, error_code)