from django.urls import path
from newsletter import views

urlpatterns = [
    path('SMS-Campaign-Registry',views.sms_campaign_registry, name='sms-campaign-registry'),
    path('SMS-Pricing-Updates',views.sms_pricing_updates, name='sms-pricing-updates')
]