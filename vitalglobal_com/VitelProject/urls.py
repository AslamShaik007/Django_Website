"""VitelProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from VitelApp import views
from django.conf import settings
from django.conf.urls.static import static

# ===Sitemap imports========
from django.views.generic.base import TemplateView

# ===== Viteldevelopment Code =======
from VitelApp.views import number_portablity, getTollFreeDids,getLocalDids

# from VitelApp.views import robots_txt


urlpatterns = [
    path("unsubscribe", views.unsubscribe, name="unsubscribe"),
    path('channel-partners', views.channel_partners , name= 'channel-partners'),
    path('itserve/', views.redirect_itserve , name= 'itserve'),
    path('qr/<str:qrcode>', views.DynamicQrCode , name= 'qrcode'),

    path("admin/", admin.site.urls),
    path("", views.index, name="index"),

    path("it_serve/", views.qrcode, name="it_serve"),
    path(
        "index_test",
        views.index_test2,
        name="index_test",
    ),
    path(
        "index-test",
        views.index_test,
        name="index-test",
    ),
    path(
        "test",
        views.test,
        name="test",
    ),
    # =======urls for Products====
    path("ucaas", views.ucaas, name="ucaas"),
    path(
        "cloud-based-business-phone",
        views.cloud_based_business_phone,
        name="cloud-based-business-phone",
    ),
    path("ip-phones", views.ip_phones, name="ip-phones"),
    #--------------------------------------------------
    path(
        "cloud-video-conferencing",
        views.voip_video_conference,
        name="voip-video-conference",
    ),
    path(
        "cloud-video-conference",
        views.redirect_voip_video_conference,
    ),
    path(
        "voip-video-conference",
        views.redirect_voip_video_conference,
    ),
    #-------------------------------------------------------
    path("team-messaging", views.team_messaging, name="team-messaging"),
    path("communication-apis", views.communication_apis, name="communication-apis"),
    path(
        "email-server-services",
        views.email_server_services,
        name="email-server-services",
    ),
    path("mobile-voip-app", views.mobile_voip_app, name="mobile-voip-app"),
    path("desktop-voip-app", views.desktop_voip_app, name="desktop-voip-app"),
    # =======urls for Solutions====
    path(
        "corporate-business-phone-solutions",
        views.corporate_business_phone_solutions,
        name="corporate-business-phone-solutions",
    ),
    path(
        "enterprise-business-phone-service",
        views.enterprise_business_phone_service,
        name="enterprise-business-phone-service",
    ),
    path(
        "business-phone-solutions-non-profit",
        views.business_phone_solutions_non_profit,
        name="business-phone-solutions-non-profit",
    ),
    path('small-business-phone-service',
        views.small_business_phone_service,
        name ='small-business-phone-service'),

    # =======urls for Sector====
    path(
        "it-staffing-cloud-phone-system",
        views.it_staffing_cloud_phone_system,
        name="it-staffing-cloud-phone-system",
    ),
    path(
        "education-cloud-phone-system",
        views.education_cloud_phone_system,
        name="education-cloud-phone-system",
    ),
    path(
        "healthcare-cloud-phone-services",
        views.healthcare_cloud_phone_services,
        name="healthcare-cloud-phone-services",
    ),
    path(
        "manufacturing-business-phone-service",
        views.manufacturing_business_phone_service,
        name="manufacturing-business-phone-service",
    ),
    path(
        "business-phone-service-retail-stores",
        views.business_phone_service_retail_stores,
        name="business-phone-service-retail-stores",
    ),
    path(
        "real-estate-business-phone-service",
        views.real_estate_business_phone_service,
        name="real-estate-business-phone-service",
    ),
    path(
        "business-phone-technical-services",
        views.business_phone_technical_services,
        name="business-phone-technical-services",
    ),
    path(
        "transportation-warehousing-phone-service",
        views.transportation_warehousing_phone_service,
        name="transportation-warehousing-phone-service",
    ),
    path(
        "business-communications-for-financial-services",
        views.business_communications_for_financial_services,
        name="business-communications-for-financial-services",
    ),
    # =======urls for By Need====
    path(
        "cloud-voip-solutions", views.cloud_voip_solutions, name="cloud-voip-solutions"
    ),
    path("SIP-trunking", views.SIP_trunking, name="SIP-trunking"),
    #======================================================================
    path("global-voip-services", views.global_scope, name="global-scope"),
    path("global-scope", views.redirect_global_scope),
    #======================================================================
    path("crm-integration", views.crm_integration, name="crm-integration"),
    path("ats-integration", views.ats_integration, name="ats-integration"),
    path(
        "voip-api-integration", views.voip_api_integration, name="voip-api-integration"
    ),
    
        # ===========urls for Pricing======
    path(
        "unlimited-calling-plans",
        views.unlimited_calling_plans,
        name="unlimited-calling-plans",
    ),
    path("pay-as-you-go", views.pay_as_you_go, name="pay-as-you-go"),
    # =======urls for By Resources====
    path("promo-videos", views.promo_videos, name="promo-videos"),
    path("e-books", views.e_books, name="e-books"),
    path("e-books/<str:ebook>", views.ebook_page, name="e-book-page"),
    path("podcasts", views.podcasts, name="podcasts"),
    path("factsheet", views.factsheet, name="factsheet"),
    # path("partners-program", views.partners_program, name="partners-program"),
    path("press-release", views.press_release, name="press-release"),
    path("white-papers", views.white_papers, name="white-papers"),
    path(
        "white-papers/<str:whitepaper>",
        views.whitepapers_page,
        name="white-papers-page",
    ),
    path("newsroom", views.newsroom, name="newsroom"),
    path(
        "rewards-by-cio-coverage-magazine",
        views.rewards_by_cio_coverage_magazine,
        name="rewards-by-cio-coverage-magazine",
    ),
    path(
        "inc5000-press-release",
        views.inc5000_press_release,
        name="inc5000-press-release",
    ),
    path(
        "platinum-sponsor-of-itserve",
        views.platinum_sponsor_of_itserve,
        name="platinum-sponsor-of-itserve",
    ),
    path("inclusion", views.inclusion, name="inclusion"),
    path("csr", views.csr, name="csr"),
    path("careers", views.Careers, name="careers"),
    path("joborder_id=<str:joborderid>", views.Careers_listing, name="joborder"),
    path("hybrid-workforce", views.hybrid_workforce, name="hybrid-workforce"),
    # =======urls for company====
    path("overview", views.overview, name="overview"),
    path("why-vitelglobal", views.why_vitelglobal, name="why-vitelglobal"),
    path("why-voip", views.why_voip, name="why-voip"),
    path(
        "contact-center-solutions",
        views.contact_center_solutions,
        name="contact-center-solutions",
    ),
    # =======urls for All Forms====
    path("newsletter", views.Newsletter, name="newsletter"),
    path("get-rolling", views.get_rolling, name="get-rolling"),
    path("feedback", views.Feedback, name="feedback"),
    path("partners-program", views.partners, name="partners-program"),
    # =======urls for features====
    path("features/local-dialling", views.local_dialling, name="local-dialling"),
    path("features/extensions", views.extensions, name="extensions"),
    path("features/call-delegation", views.call_delegation, name="call-delegation"),
    path("features/call-forwarding", views.call_forwarding, name="call-forwarding"),
    path("features/call-flip", views.call_flip, name="call-flip"),
    path("features/call-screening", views.call_screening, name="call-screening"),
    path("features/omnipresence", views.omnipresence, name="omnipresence"),
    path("features/local-numbers", views.local_numbers, name="local-numbers"),
    path("features/local-numbers", views.local_numbers, name="local-numbers"),
    path(
        "features/one-touch-calling", views.one_touch_calling, name="one-touch-calling"
    ),
    path("features/call-park", views.call_park, name="call-park"),
    path(
        "features/answering-methods", views.answering_methods, name="answering-methods"
    ),
    path("features/visual-voicemail", views.visual_voicemail, name="visual-voicemail"),
    path(
        "features/phones-accessories",
        views.phones_accessories,
        name="phones-accessories",
    ),
    path("features/paging", views.paging, name="paging"),
    path("features/internet-fax", views.internet_fax, name="internet-fax"),
    path("features/shared-lines", views.shared_lines, name="shared-lines"),
    path(
        "features/voicemail-to-email",
        views.voicemail_to_email,
        name="voicemail-to-email",
    ),
    path("features/cloud-pbx", views.cloud_pbx, name="cloud-pbx"),
    path("features/greetings", views.greetings, name="greetings"),
    path("features/multi-level-ivr", views.multi_level_ivr, name="multi-level-ivr"),
    path("features/music-on-hold", views.music_on_hold, name="music-on-hold"),
    path(
        "features/dial-by-name-directory",
        views.dial_by_name_directory,
        name="dial-by-name-directory",
    ),
    path("features/number-porting", views.number_porting, name="number-porting"),
    path(
        "features/multi-site-management",
        views.multi_site_management,
        name="multi-site-management",
    ),
    path("features/call-monitoring", views.call_monitoring, name="call-monitoring"),
    path("features/call-logs", views.call_logs, name="call-logs"),
    path(
        "features/automatic-call-recording",
        views.automatic_call_recording,
        name="automatic-call-recording",
    ),
    path("features/audit-trail", views.audit_trail, name="audit-trail"),
    path(
        "features/brilliant-desking", views.brilliant_desking, name="brilliant-desking"
    ),
    path("features/caller-id", views.caller_id, name="caller-id"),
    path(
        "features/list-of-directory", views.list_of_directory, name="list-of-directory"
    ),
    path("features/user-templates", views.user_templates, name="user-templates"),
    path(
        "features/international-numbers",
        views.international_numbers,
        name="international-numbers",
    ),
    path(
        "features/international-calling",
        views.international_calling,
        name="international-calling",
    ),
    path(
        "features/video-conferencing",
        views.video_conferencing,
        name="video-conferencing",
    ),
    path(
        "features/audio-conferencing",
        views.audio_conferencing,
        name="audio-conferencing",
    ),
    path("features/cloud", views.cloud, name="cloud"),
    path(
        "features/collaboration-with-teams",
        views.collaboration_with_teams,
        name="collaboration-with-teams",
    ),
    path(
        "features/business-sms-and-mms",
        views.business_sms_and_mms,
        name="business-sms-and-mms",
    ),
    path("features/message-alerts", views.message_alerts, name="message-alerts"),
    path(
        "features/secure-voip-service",
        views.secure_voip_service,
        name="secure-voip-service",
    ),
    path(
        "features/single-registration",
        views.single_registration,
        name="single-registration",
    ),
    path(
        "features/data-center-overview",
        views.data_center_overview,
        name="data-center-overview",
    ),
    path(
        "features/roles-and-permissions",
        views.roles_and_permissions,
        name="roles-and-permissions",
    ),
    path("features/analytics-portal", views.analytics_portal, name="analytics-portal"),
    path(
        "features/performance-reports",
        views.performance_reports,
        name="performance-reports",
    ),
    path("features/qos-reports", views.qos_reports, name="qos-reports"),
    path("features/live-reports", views.live_reports, name="live-reports"),
    # =======urls for states====
    path("state/alabama", views.alabama, name="alabama"),
    path("state/kentucky", views.kentucky, name="kentucky"),
    path("state/missouri", views.missouri, name="missouri"),
    path("state/alaska", views.alaska, name="alaska"),
    path("state/colorado", views.colorado, name="colorado"),
    path("state/georgia", views.georgia, name="georgia"),
    path("state/michigan", views.michigan, name="michigan"),
    path("state/montana", views.montana, name="montana"),
    path("state/new-jersey", views.new_jersey, name="new-jersey"),
    path("state/north-dakota", views.north_dakota, name="north-dakota"),
    path("state/massachusetts", views.massachusetts, name="massachusetts"),
    path("state/illinois", views.illinois, name="illinois"),
    path("state/pennsylvania", views.pennsylvania, name="pennsylvania"),
    path("state/tennessee", views.tennessee, name="tennessee"),
    path("state/virginia", views.virginia, name="virginia"),
    path("state/wisconsin", views.wisconsin, name="wisconsin"),
    path("state/new-hampshire", views.new_hampshire, name="new-hampshire"),
    path("state/north-carolina", views.north_carolina, name="north-carolina"),
    path("state/oregon", views.oregon, name="oregon"),
    path("state/south-dakota", views.south_dakota, name="south-dakota"),
    path("state/vermont", views.vermont, name="vermont"),
    path("state/west-virginia", views.west_virginia, name="west-virginia"),
    path("state/arizona", views.arizona, name="arizona"),
    path("state/connecticut", views.connecticut, name="connecticut"),
    path("state/iowa", views.iowa, name="iowa"),
    path("state/maine", views.maine, name="maine"),
    path("state/minnesota", views.minnesota, name="minnesota"),
    path("state/nebraska", views.nebraska, name="nebraska"),
    path("state/new-mexico", views.new_mexico, name="new-mexico"),
    path("state/ohio", views.ohio, name="ohio"),
    path("state/rhode-island", views.rhode_island, name="rhode-island"),
    path("state/washington", views.washington, name="washington"),
    path("state/wyoming", views.wyoming, name="wyoming"),
    path("state/arkansas", views.arkansas, name="arkansas"),
    path("state/delaware", views.delaware, name="delaware"),
    path("state/idaho", views.idaho, name="idaho"),
    path("state/kansas", views.kansas, name="kansas"),
    path("state/maryland", views.maryland, name="maryland"),
    path("state/mississippi", views.mississippi, name="mississippi"),
    path("state/nevada", views.nevada, name="nevada"),
    path("state/new-york", views.new_york, name="new-york"),
    path("state/oklahoma", views.oklahoma, name="oklahoma"),
    path("state/south-carolina", views.south_carolina, name="south-carolina"),
    path("state/utah", views.utah, name="utah"),
    path("state/washington-dc", views.washington_dc, name="washington-dc"),
    path("state/louisiana", views.louisiana, name="louisiana"),
    
    # =======urls for Area Codes ====
    path("area-codes", views.area_codes, name="area-codes"),
    path("area-codes-1", views.area_codes_1, name="area-codes-1"),
    
    path("local-numbers", views.local_numbers_ac, name="local-numbers-ac"), 
    path("local-numbers/washington-ac", views.washington_ac, name="washington-ac"),
    path("local-numbers/alabama-ac", views.alabama_ac, name="alabama-ac"),
    path("local-numbers/arizona-ac", views.arizona_ac, name="arizona-ac"),
    path("local-numbers/arkansas-ac", views.arkansas_ac, name="arkanssas-ac"),
    path("local-numbers/california-ac", views.california_ac, name="california-ac"),
    path("local-numbers/colorado-ac", views.colorado_ac, name="colorado-ac"),
    path("local-numbers/connecticut-ac", views.connecticut_ac, name="connecticut-ac"),
    path("local-numbers/delaware-ac", views.delaware_ac, name="delaware-ac"),
    path("local-numbers/florida-ac", views.florida_ac, name="florida-ac"),
    path("local-numbers/district-of-columbia", views.district_of_columbia, name="district-of-columbia"),
    path("local-numbers/georgia-ac", views.georgia_ac, name="georgia-ac"),
    path("local-numbers/hawaii-ac", views.hawaii_ac, name="hawaii-ac"),
    path("local-numbers/idaho-ac", views.idaho_ac, name="idaho-ac"),
    path("local-numbers/illinois-ac", views.illinois_ac, name="illinois-ac"),
    path("local-numbers/iowa-ac", views.iowa_ac, name="iowa-ac"),
    path("local-numbers/kansas-ac", views.kansas_ac, name="kansas-ac"),
    path("local-numbers/kentucky-ac", views.kentucky_ac, name="kentucky-ac"),
    path("local-numbers/louisiana-ac", views.louisiana_ac, name="louisiana-ac"),
    path("local-numbers/maine-ac", views.maine_ac, name="maine-ac"),
    path("local-numbers/maryland-ac", views.maryland_ac, name="maryland-ac"),
    path("local-numbers/massachusetts-ac", views.massachusetts_ac, name="massachusetts-ac"),
    path("local-numbers/michigan-ac", views.michigan_ac, name="michigan-ac"),
    path("local-numbers/minnesota-ac", views.minnesota_ac, name="minnesota-ac"),
    path("local-numbers/mississippi-ac", views.mississippi_ac, name="mississippi-ac"),
    path("local-numbers/montana-ac", views.montana_ac, name="montana-ac"),
    path("local-numbers/nebraska-ac", views.nebraska_ac, name="nebraska-ac"),
    path("local-numbers/nevada-ac", views.nevada_ac, name="nevada-ac"),
    path("local-numbers/new-jersey-ac", views.new_jersey_ac, name="new-jersey-ac"),
    path("local-numbers/new-mexico-ac", views.new_mexico_ac, name="new-mexico-ac"),
    path("local-numbers/new-york-ac", views.new_york_ac, name="new-york-ac"),
    path("local-numbers/north-carolina-ac", views.north_carolina_ac, name="north-carolina-ac"),
    path("local-numbers/north-dakota-ac", views.north_dakota_ac, name="north-dakota-ac"),
    path("local-numbers/ohio-ac", views.ohio_ac, name="ohio-ac"),
    path("local-numbers/oklahoma-ac", views.oklahoma_ac, name="oklahoma-ac"),
    path("local-numbers/oregon-ac", views.oregon_ac, name="oregon-ac"),
    path("local-numbers/pennsylvania-ac", views.pennsylvania_ac, name="pennsylvania-ac"),
    path("local-numbers/rhode-island-ac", views.rhode_island_ac, name="rhode-island-ac"),
    path("local-numbers/south-carolina-ac", views.south_carolina_ac, name="south-carolina-ac"),
    path("local-numbers/south-dakota-ac", views.south_dakota_ac, name="south-dakota-ac"),
    path("local-numbers/tennessee-ac", views.tennessee_ac, name="tennessee-ac"),
    path("local-numbers/texas-ac", views.texas_ac, name="texas-ac"),
    path("local-numbers/utah-ac", views.utah_ac, name="utah-ac"),
    path("local-numbers/vermont-ac", views.vermont_ac, name="vermont-ac"),
    path("local-numbers/virginia-ac", views.virginia_ac, name="virginia-ac"),
    path("local-numbers/west-virginia-ac", views.west_virginia_ac, name="west-virginia-ac"),
    path("local-numbers/wisconsin-ac", views.wisconsin_ac, name="wisconsin-ac"),
    path("local-numbers/wyoming-ac", views.wyoming_ac, name="wyoming-ac"),

    
    
    # =======urls for Vitel-center====
    path("vitel-center", views.center, name="vitel-center"),
    path("faq", views.faq, name="faq"),
    # =======urls for Footer====
    path("itserve-offer", views.itserve_offer, name="itserve-offer"),
    path("contact", views.contact, name="contact"),
    path(
        "terms-and-conditions", views.terms_and_conditions, name="terms-and-conditions"
    ),
    path("privacy-policy", views.privacy_policy, name="privacy-policy"),
    path("campaign-registry", views.campaign_registry, name="campaign-registry"),
    path("sms-registration", views.sms_registration, name="sms-registration"),
    path("mms-sms-registry", views.mms_sms_registry, name="mms-sms-registry"),
    # urls for Thankyou pages
    path("contact/thankyou", views.Contactus_Thankyou, name="contactus-thankyou"),
    path("getrolling/thankyou", views.getrolling_Thankyou, name="getrolling-thankyou"),
    path("live-demo/thankyou", views.Live_Demo_Thankyou, name="live-demo-thankyou"),
    path("e-book/thankyou", views.e_books_Thankyou, name="e-books-thankyou"),
    path("newsletter/thankyou", views.Newsletter_Thankyou, name="newsletter-thankyou"),
    path("feedback/thankyou", views.Feedback_Thankyou, name="feedback-thankyou"),
    path("partners/thankyou", views.partners_Thankyou, name="partners-thankyou"),
    path("careers/thankyou", views.Careers_Thankyou, name="careers-thankyou"),
    path(
        "white-paper/thankyou",
        views.white_papers_Thankyou,
        name="white-papers-thankyou",
    ),
     path("unsubscribe/thankyou", views.Unsubscribe_Thankyou, name="unsubscribe-thankyou"),
    # Landing Page Urls
    path('businessphone',views.landing_page_business_phone, name='land-business-phone'),
    path('quote-thankyou',views.business_phone_thankyou, name='businessphone-thankyou'),
    path('demo-thankyou',views.thankyou_demo_land, name='demo-thankyou'),
    path('request-demo-now',views.request_demo_land_page,name = 'request-demo-now'),
    # robots.txt
    path("robots.txt", views.robots, name="robots.txt"),
    path("sitemap.xml", views.sitemap, name="sitemap.xml"),

    # =========urls for captcha ===========
    path('captcha/', include('captcha.urls')),
    
    # ======== NEW URLS Redirections =======
    path("state/texas", views.texas, name="texas"),
    path("business-phone-service/texas-tx",views.new_texas,name="business-texas"),
    #-----------------------------------
    path("state/california", views.california, name="california"),
    path("business-phone-service/california-ca", views.new_california, name="business-california"),
    #-----------------------------------------
    path("state/florida", views.florida, name="florida"),
    path("business-phone-service/florida-fl", views.new_florida, name="business-florida"),
    #------------------------------------------
    path("state/hawaii", views.hawaii, name="hawaii"),
    path("business-phone-service/hawaii-hi", views.new_hawaii, name="business-hawaii"),
    #----------------------------------------------
    path("state/indiana", views.indiana, name="indiana"),
    path("business-phone-service/indiana-in", views.new_indiana, name="business-indiana"),
    #-----------------------------------------------
    path("live-demo", views.Redirect_to_live_demo, name="voip-live-demo"),
    path("voip-live-demo", views.voip_live_demo, name="voip-live-demo"),
    #--------------------------------------------
    path("features",views.business_phone_features,name="business-phone-features"),
    path("business-phone-features",views.new_business_phone_features,name="business-phone-features"),
    #---------------------------------------
    path("benefits",views.business_phone_features,name="business-phone-features"),
    path("business-phone-features",views.new_business_phone_features,name="business-phone-features"),
    #---------------------------------------
    path("hosted-pbx-unlimited",views.cloud_pbx_phone_system,name="cloud-pbx-phone-system"),
    path("cloud-pbx-phone-system",views.new_cloud_pbx_phone_system,name="cloud-pbx-phone-system"),
    #------------------------------------
    path("cloud-pbx-voip",views.cloud_pbx_phone_system,name="cloud-pbx-phone-system"),
    path("cloud-pbx-phone-system",views.new_cloud_pbx_phone_system,name="cloud-pbx-phone-system"),
    
    # ------ viteldevelopment code ---------
    path("setup-plan",views.setup_plan,name="setup-plan"),
    path('number_portablity', number_portablity.as_view() , name= 'number-portablity'),
    path('toll_free_dids', getTollFreeDids.as_view() , name= 'get-Toll-Free-Dids'),
    path('get_local_dids', getLocalDids.as_view() , name= 'get-Toll-Free-Dids'),
    
]

# handler404 = "VitelApp.views.handler404"

# urlpatterns = [
#     path('newsletter/',include('newsletter.urls')),
#     path('emailtem/',include('emailtem.urls')),
#     path("admin/", admin.site.urls),
#     path("", views.Index, name="index"),
#     path('voip-live-demo',views.voip_live_demo,name='voip-live-demo'),
#     path('ucaas',views.ucass,name= 'ucass'),
#     path("kick-start", views.kick_start, name="kick-start"),
#     path("voip-service", views.voip_service, name="voip-service"),
#     path("thankyou", views.Thankyou, name="thankyou"),
#     path("contact-us", views.Contact_Us, name="contact-us"),
#     path("feedback", views.Feedback, name="feedback"),
#     path('newsletter',views.Newsletter,name='newsletter'),

#     #=======urls for company====
#     path('overview',views.overview,name= 'overview'),
#     path('why-vitelglobal',views.why_vitelglobal,name= 'why-vitelglobal'),
#     path('why-voip',views.why_voip,name ='why-voip'),
#     path('contact-center-solutions',views.contact_center_solutions,name ='contact-center-solutions'),

#     #=======urls for homepage innerpages====
#     path('hybrid-work-culture',views.hybrid_work_culture,name= 'hybrid-work-culture'),
#     path('team-collaboration',views.team_collaboration,name= 'team-collaboration'),
#     path('boost-customer-interaction',views.boost_customer_interaction,name ='boost-customer-interaction'),
#     path('omni-channel-experience',views.omni_channel_experience,name ='omni-channel-experience'),
#     path('video-conference-solution',views.video_conference_solution,name= 'video-conference-solution'),

#     #=======urls for FOOTER ==============
#     path('terms-and-conditions',views.terms_and_conditions,name= 'terms-and-conditions'),
#     path('privacy-policy',views.privacy_policy,name= 'privacy-policy'),
#     path('toll-free-number',views.toll_free_number,name= 'toll-free-number'),
#     path('ivr-solution',views.ivr_solution,name= 'ivr-solution'),

#     # ========= urls for PRODUCTS========
#     #Business Communications
#     path("cloud-based-business-phone",views.cloud_based_business_phone,name="cloud-based-business-phone"),
#     path("ip-phones",views.ip_phones,name="ip-phones"),
#     path('text-messaging',views.business_messages,name= 'business-messages'),
#     path('video-conferencing',views.video_call_solution_for_business,name= 'video-call-solution-for-business'),
#     path('desktop-mobile-app',views.vitelglobal_web_mobile_app,name= 'vitelglobal-web-mobile-app'),
#     # ========= urls for SOLUTIONS  ======
#     # On Demand
#     path('corporate-business-phone-service',views.corporate_voip_cloud_phone_solution,name= 'corporate-voip-cloud-phone-solution'),
#     path('enterprise-communications',views.enterprise_voip_solution,name= 'enterprise-voip-solution'),
#     path('industries',views.voip_for_small_medium_enterprises,name= 'voip-for-small-medium-enterprises'),
#     #By Bussiness
#     path('healthcare-business-cloud-phone-service',views.healthcare_voip_cloud_phone_services,name= 'healthcare-voip-cloud-phone-services'),
#     path('it-staffing-business-phones',views.voip_phone_for_it_staffing,name= 'voip-phone-for-it-staffing'),
#     path('retail-business-cloud-phone-solution',views.retail_business_cloud_phone_solution,name ='retail-business-cloud-phone-solution'),
#     path('education-cloud-phone-solution',views.education_voip_phone_solution,name= 'education-voip-phone-solution'),
#     path('business-phone-legal-services',views.voip_phone_for_financial_services,name='voip-phone-for-financial-services'),
#     path('nonprofit-organisations',views.voip_services_for_nonprofits_organization,name= 'voip-services-for-nonprofits-organization'),
#     #By Rush
#     path('cloud-voice-solution',views.cloud_voice_solution,name ='cloud-voice-solution'),
#     path('cloud-pbx-system',views.cloud_pbx_system_solution,name= 'cloud-pbx-system-solution'),
#     path('global-expansion',views.global_expansion_cloud_pbx_phone,name= 'global-expansion-cloud-pbx-phone'),
#     path('cloud-based-crm-integration',views.voip_crm_integration,name= 'voip-crm-integration'),
#     path('ats-integration',views.voip_ats_integration,name= 'voip-ats-integration'),
#     path('api-integration',views.voip_api_integration,name= 'voip-api-integration'),
#     path('all-in-one-features',views.all_in_features,name= 'all-in-features'),
#     #=========urls for PRICING =======
#     path('plans-and-pricing',views.voip_plans,name= 'voip-plans'),
#     #=========urls for RESOURCES =====
#     path('promotions',views.promotions,name= 'promotions'),
#     path("webinars", views.Webinars, name="webinars"),
#             #webinars inner pages
#     path("webinar-watch", views.Webinar_Watch, name="webinar-watch"),
#     path("webinar-view", views.Webinar_View, name="webinar-view"),
#             #--------------------
#     path('e-books',views.e_books,name= 'e-books'),
#     path('podcasts',views.podcasts,name= 'podcasts'),
#     path('partners',views.partners,name='partners'),
#     path('case-studies',views.case_studies_voip_cloud_system,name='case-studies-voip-cloud-system'),
#     path('white-papers',views.voip_white_papers,name= 'voip-white-papers'),
#     path('newsroom',views.newsroom,name= 'newsroom'),
#     path('inclusion',views.inclusion,name= 'inclusion'),
#     path('csr',views.csr,name= 'csr'),
#     path('corporate-events',views.corporate_event_registration,name= 'corporate-event-registration'),
#     path("careers", views.Careers, name="careers"),

#     #========Url for Thankyou pages=====
#     path('live-demo/thankyou',views.Live_Demo_Thankyou,name='live-demo-thankyou'),
#     path('kick-start/thankyou',views.kickstart_Thankyou,name='kickstart-thankyou'),
#     path('contact/thankyou',views.Contactus_Thankyou,name='contactus-thankyou'),
#     path('voipservice/thankyou',views.voipservice_Thankyou,name='voipservice-thankyou'),

#     #======url for 404 PAGE ====
#     path('404',views.Page404,name= 'page404'),

#     #===========path for Robots.txt========
#     path(
#         "robots.txt",
#         TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
#     ),
#     path("robots.txt", robots_txt),
#     path('sitemap.xml',views.sitemap, name = 'sitemap.xml'),
# ]


# if settings.DEBUG:
#      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
