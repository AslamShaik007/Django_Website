from django.shortcuts import render

# Create your views here.

# def business_operate(request):
#     return render(request,'emailtemplates/business-operate.html')
def sms_campaign_registry(request):
    return render(request,'emailtemplates/SMS-Campaign-Registry.html')

def sms_pricing_updates(request):
    return render(request,'emailtemplates/SMS-Pricing-Updates.html')

