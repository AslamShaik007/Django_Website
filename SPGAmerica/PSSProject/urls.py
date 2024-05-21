from django.contrib import admin
from django.urls import path
from PSSApp import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index, name = 'index'),
    path('about-us',views.About_Us,name = 'about-us'),
    #=====URL Routings for SERVIVES ============
    path('education',views.education,name = 'education'),
    path('ar_vr_app_developemnt',views.ar_vr_app_developemnt, name = 'ar-vr-app-developemnt'),
    path('contact',views.New_Contact, name='contact'),
    path('contact-us',views.Contact_Us, name='contact'),
    path('business-modernization',views.business_modernization, name = 'business-modernization'),
    path('career-counsellings',views.career_counsellings, name = 'career-counsellings'),
    path('customized-training-programs',views.customized_training_programs, name = 'customized-training-programs'),   
   
    

    #=======URL Routings for Success Stories======
    path('podcasts',views.podcasts, name = 'podcasts'),
    path('promotional-videos',views.promotional_videos, name = 'promotional-videos'),
    path('ebooks',views.e_books, name = 'e-books'),
    path('ebooks-innerpage/<str:ebook>',views.ebooks_innerpage, name = 'ebooks-innerpage'),
    path('whitepapers',views.white_papers, name = 'white-papers'),
    path('whitepaper-innerpage/<str:ebook>', views.whitepapers_pages, name = 'whitepaper-innerpage'),
    path('blog',views.blog, name = 'blog'),
    path('csr',views.csr, name = 'csr'),
    path('careers',views.careers, name = 'careers'),
    path('graduates',views.graduates, name = 'graduates'),
    path('experienced-professionals',views.experienced_professionals, name = 'experienced-professionals'),
    path('students-internships',views.students_internships, name = 'students-internships'),
    path('explore-opportunities',views.explore_opportunities, name = 'explore-opportunities'),
    path('news-room',views.news_room, name = 'news-room'),
    path('press-releases',views.press_releases, name = 'press-releases'),   
    path('features',views.features, name = 'features'),
    path('newsletter',views.Newsletter, name = 'newsletter'),

    # new urls start

    path('services/growth-optimization',views.growth_optimization, name = 'growth-optimization'),
    path('services/talent-acceleration',views.talent_acceleration, name = 'talent-acceleration'),
    path('services/generative-ai-advisory',views.generative_ai_advisory, name = 'generative-ai-advisory'),
    path('services/cx-strategy-and-design',views.cx_strategy_and_design, name = 'cx-strategy-and-design'),
    # path('services/next-gen-marketing',views.next_gen_marketing, name = 'next-gen-marketing'),
    # path('services/next-gen-marketing',views.next_gen_marketing, name = 'next-gen-marketing'),
    path('services/workforce-experience',views.workforce_experience, name = 'workforce-experience'),
    path('services/react-js-practice',views.react_js_practice, name = 'react-js-practice'),
    path('services/managed-detection-response',views.managed_detection_response, name = 'managed-detection-response'),
    path('services/digital-risk-management',views.digital_risk_management, name = 'digital-risk-management'),
    path('services/ransomware-protection',views.ransomware_protection, name = 'ransomware-protection'),
    path('services/zero-trust-implementation',views.zero_trust_implementation, name = 'zero-trust-implementation'),
    path('services/next-gen-marketing',views.next_gen_marketing, name = 'next-gen-marketing'),
    path('services/embedded-system-development',views.embedded_system_development, name = 'embedded-system-development'),
    path('services',views.services, name = 'services'),
    






     # ====Urls for new industries
    path('industries',views.industries, name = 'industries'),
    path('industries/consumer-packaged-goods',views.consumer_packaged_goods, name = 'consumer-packaged-goods'),
    path('industries/travel-and-hospitality',views.travel_and_hospitality, name = 'travel-and-hospitality'),
    path('industries/retail',views.retail, name = 'retail'),
    path('industries/wealth-management',views.wealth_management, name = 'wealth-management'),
    path('industries/commercial-banking',views.commercial_banking, name = 'commercial-banking'),
    path('industries/telecommunications',views.telecommunications, name = 'telecommunications'),
    path('industries/media-and-entertainment',views.media_and_entertainment, name = 'media-and-entertainment'),
    path('industries/gaming',views.gaming, name = 'gaming'),
    path('industries/business-information-and-publishing',views.business_information_and_publishing, name = 'business-information-and-publishing'),
    path('industries/sports',views.sports, name = 'sports'),
    path('industries/regulations',views.regulations, name = 'regulations'),
    path('industries/metahuman-assistant',views.metahuman_assistant, name = 'metahuman-assistant'),
    path('industries/medtech',views.medtech, name = 'medtech'),
    path('industries/software-and-tech',views.software_and_tech, name = 'software-and-tech'),
    path('industries/education',views.education, name = 'education'),
    path('industries/energy-and-resources',views.energy_and_resources, name = 'energy-and-resources'),


    

    path('corporate-responsibility',views.corporate_responsibility, name = 'corporate-responsibility'),
    path('ethics-and-compliance',views.ethics_and_compliance, name = 'ethics-and-compliance'),
    path('events',views.events, name = 'events'),
    # path('contactus',views.contactus, name = 'contactus'),
    path('faqs',views.faqs, name = 'faqs'),


    path('get-on-board',views.get_on_board, name = 'get-on-board'),
    path('relocate-with-spg',views.relocate_with_spg, name = 'relocate-with-spg'),
    path('referral-program',views.referral_program, name = 'referral-program'),

    
    path('spg-insights',views.spg_insights, name = 'spg-insights'),

    # path('ebooks-innerpage/<str:ebook>/',views.ebooks_innerpage, name = 'ebooks-innerpage'),
    # path('whitepapers-innerpage/<str:wbook>/',views.whitepapers_innerpage, name = 'whitepapers-innerpage'),            


  
   



###########NEW URLS_REDIRECTS
 path('ai-ml-automation',views.ai_ml_automation,name = 'ai-ml-automation'),
 path('services/ai-ml-research-and-development',views.ai_ml_research_and_development, name = 'ai-ml-research-and-development'),
 
 path('digital-marketing-agency',views.digital_marketing_agency,name = 'digital-marketing-agency'),
 path('services/digital-transformation',views.digital_transformation, name = 'digital-transformation'),
 
path('spg-metaverse',views.spg_metaverse, name = 'spg-metaverse'),
path('services/metaverse',views.metaverse, name = 'metaverse'),
 
 
path('cloud-tech',views.cloud_tech, name = 'cloud-tech'), 
path('services/cloud-data-security',views.cloud_data_security, name = 'cloud-data-security'),

path('web-development',views.web_development, name = 'web-development'), 
path('services/digital-transformation',views.web_digital_transformation, name = 'digital-transformation'), 


path('programming',views.programming, name = 'programming'),
path('services/python-practice',views.python_practice, name = 'python-practice'),

path('networking',views.networking, name = 'networking'),
path('services/cybersecurity-advisory',views.cybersecurity_advisory, name = 'cybersecurity-advisory'),

path('technical-training-programs',views.technical_training_programs, name = 'technical-training-programs'),
path('',views.tech_Index, name = 'index'),


path('itconsulting-services',views.itconsulting_services,name = 'itconsulting-services'),
path('',views.it_Index, name = 'index'),


path('spg-mission-statement',views.spg_mission_statement, name = 'spg-mission-statement'),
path('',views.mission_Index, name = 'index'),


path('inclusion-and-diversity',views.inclusion_and_diversity, name = 'inclusion-and-diversity'),
path('',views.inclusion_Index, name = 'index'),

path('all-in-one-services',views.all_in_one_services, name = 'all-in-one-services'),
path('services',views.new_all_in_one,name='new-services'),
 
path('fraud-warning',views.fraud_warning, name = 'fraud-warning'), 
path('privacy-policy',views.privacy_policy, name = 'privacy-policy'),
 
 













    


    






    # new urls start






    #=========URL for terms and conditions and PrivacyPolicy=====
  
    # path('api/test',views.apitest, name='api/test'),
    # path('404',views.test_404, name='404'),

    # path('joborder_id=<str:joborderid>',views.Careers_listing, name='joborder'),
    path('sitemap.xml',views.sitemap, name = 'sitemap.xml'),
    path('robots.txt',views.robots, name = 'robots.txt'),
]

if settings.DEBUG:     
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)