from django.conf import settings
from zeep.helpers import serialize_object
import zeep #A fast and modern Python SOAP client
from django.http import HttpResponse
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup
import re
from django.core.mail import EmailMessage
from django.utils import timezone
import pytz

# Voip Innovations - SOAP API
def number_portablity_check(tn):

    login       = settings.VOIP_API_LOGIN
    secret      = settings.VOIP_API_PASSWORD 
    wsdl_url    = settings.VOIP_API_WSDL_URL # set the WSDL URL
    service_url = settings.VOIP_API_SERVICE_URL # set service URL
    method_base_url = settings.VOIP_API_METHOD_BASE_URL # set Method base URL
    
    # set method URL
    method_url = method_base_url+"isPortable"
        

    # create the header element
    header = zeep.xsd.Element(
        "Header",
        zeep.xsd.ComplexType(
            [
                zeep.xsd.Element(
                    "{http://www.w3.org/2005/08/addressing}Action", zeep.xsd.String()
                ),
                zeep.xsd.Element(
                    "{http://www.w3.org/2005/08/addressing}To", zeep.xsd.String()
                ),
            ]
        ),
    )
    # set the header value from header element
    header_value = header(Action=method_url, To=service_url)


    try:
        # initialize zeep client
        client = zeep.Client(wsdl=wsdl_url)
    except:
        response_data   = {'data':{}}
        return response_data
    
    # make the service call
    result = client.service.isPortable(
        login=login,
        secret=secret,
        tn=tn,        
        _soapheaders=[header_value]
    )
    response = serialize_object(result) #converting to json   
    # Assuming 'val' is the key in the dictionary
    if 'IsPortable' in response:
        is_portable = response['IsPortable']
    
        if is_portable:
            return True
        else:
            return False
    else:
        return False
    
def format_api_response(data, message, error_code):
    response_data = {
        "results": data,
        "message": message,
        "error_code": error_code
    }
    return Response(response_data, status=error_code)

# Vitelity - Curl , response as html
def get_vitelity_tollfree_dids(keyword=""):

    login           = settings.VITELITY_API_LOGIN
    password        = settings.VITELITY_API_PASSWORD 
    base_api_url    = settings.VITELITY_API_URL   
    error_message   = ""
    # set method URL
    api_url = base_api_url+"?login="+login+"&pass="+password+"&cmd=listtollfree";  
    
    try:
        # Make the API GET request
        response = requests.post(api_url)
        if response.status_code == 200:
            soup    = BeautifulSoup(response.text, 'html.parser') 
            pre_tag = soup.find('pre') 
            if pre_tag:
                pre_content = pre_tag.get_text()
                pattern = r'x\[\[(.*?)\[\[x'
                matches = re.findall(pattern, pre_content, re.DOTALL)

                if matches:
                    extracted_data = matches[0] 
                    lines   = extracted_data.split('\n')
                    numbers = [line.split(',')[0] for line in lines]

                    data = []

                    # Iterate through the original array and add keys and additional key-value pairs
                    for index, item in enumerate(numbers):
                        # Create a dictionary for each item 
                        if item == "missingdata":
                            error_message ="Login details or command is missing"
                        elif item == "missing":
                            error_message ="State value is missing or incorrect state value"
                        elif item == "invalidauth":
                            error_message ="Invalid login details"
                        elif item == "missingrc":
                            error_message ="Ratecenter value missing"
                        elif item == "unavailable" or item=="":
                            error_message ="No Data available"
                        else:
                            item_dict = {
                                    "number": item,  # Add a numeric key
                                    "provider": "V",    # Add an existing value as a new key-value pair 
                                } 
                            data.append(item_dict)
                        
                        # Append the modified dictionary to the list
                        
                else:
                    data = [] 
                    error_message ="No matching response"
 
            else:
                data        = [] 
                error_message ="No response"
        else:
        # Handle API request failure
            data        = [] 
            error_message ="API failed"
        
    except Exception as e:
        # Handle any exceptions that occur during the API request 
        data        = []  
        error_message ="Try catch error"

    response_array  = {
                        "data": data,   
                        "error_message": error_message,    
                    } 
    if keyword:
        filtered_results = []
    
        for number in data:
            if number["number"].startswith(keyword):
                filtered_results.append(number)  
        return filtered_results
    
    
    return data


# Voip Innovations - SOAP API
def get_voip_innovations_local_dids(state="",npa="",nxx="",customer_id="",rate_center=""):

    login       = settings.VOIP_API_LOGIN
    secret      = settings.VOIP_API_PASSWORD 
    wsdl_url    = settings.VOIP_API_WSDL_URL # set the WSDL URL
    service_url = settings.VOIP_API_SERVICE_URL # set service URL
    method_base_url = settings.VOIP_API_METHOD_BASE_URL # set Method base URL
    
    # set method URL
    method_url = method_base_url+"getDIDs"
        

    # create the header element
    header = zeep.xsd.Element(
        "Header",
        zeep.xsd.ComplexType(
            [
                zeep.xsd.Element(
                    "{http://www.w3.org/2005/08/addressing}Action", zeep.xsd.String()
                ),
                zeep.xsd.Element(
                    "{http://www.w3.org/2005/08/addressing}To", zeep.xsd.String()
                ),
            ]
        ),
    )
    # set the header value from header element
    header_value = header(Action=method_url, To=service_url)    

    try:
        # initialize zeep client
        client = zeep.Client(wsdl=wsdl_url)
    except:
        response_data   = {'data':{}}
        return response_data
    
    # make the service call
    
    result = client.service.getDIDs(
        login=login,
        secret=secret,
        state=state, 
        npa=npa, 
        nxx=nxx, 
        rateCenter=rate_center,
        _soapheaders=[header_value]
    )
    
    response_dict = serialize_object(result) #converting to json
    print(response_dict)
    if response_dict['responseCode'] == 100:
        numbers        = response_dict['DIDLocators']['DIDLocator']
        data = []

        # Iterate through the original array and add keys and additional key-value pairs
        for index, item in enumerate(numbers):
            # Create a dictionary for each item
            item_dict = {
                "number": item['tn'],  # Add a numeric key
                "provider": "VI",    # Add an existing value as a new key-value pair 
                "rateCenter": item['rateCenter'],
                "state": item['state'],
                "t38": item['t38'], # Fax
                "sms": item['sms'],
            }
            
            # Append the modified dictionary to the list
            data.append(item_dict)
    else :
        data        = []

    return data


# Vitelity - Curl , response as html
def get_vitelity_local_dids(state=""):

    login           = settings.VITELITY_API_LOGIN
    password        = settings.VITELITY_API_PASSWORD 
    base_api_url    = settings.VITELITY_API_URL   
    error_message   = ""
    # set method URL
    api_url = base_api_url+"?login="+login+"&pass="+password+"&cmd=listlocal&ratecenter=&state="+state; 
    
    try:
        # Make the API GET request
        response = requests.post(api_url)
        if response.status_code == 200:
            soup    = BeautifulSoup(response.text, 'html.parser') 
            pre_tag = soup.find('pre') 
            if pre_tag:
                pre_content = pre_tag.get_text()
                pattern = r'x\[\[(.*?)\[\[x'
                matches = re.findall(pattern, pre_content, re.DOTALL)

                if matches:
                    extracted_data = matches[0] 
                    lines   = extracted_data.split('\n')
                    numbers = [line.split(',')[0] for line in lines]

                    data = []

                    # Iterate through the original array and add keys and additional key-value pairs
                    for index, item in enumerate(numbers):
                        # Create a dictionary for each item 
                        if item == "missingdata":
                            error_message ="Login details or command is missing"
                        elif item == "missing":
                            error_message ="State value is missing or incorrect state value"
                        elif item == "invalidauth":
                            error_message ="Invalid login details"
                        elif item == "missingrc":
                            error_message ="Ratecenter value missing"
                        elif item == "unavailable" or item=="":
                            error_message ="No Data available"
                        else:
                            item_dict = {
                                    "number": item,  # Add a numeric key
                                    "provider": "V",    # Add an existing value as a new key-value pair 
                                } 
                            data.append(item_dict)
                        
                        # Append the modified dictionary to the list
                        
                else:
                    data = [] 
                    error_message ="No matching response"
 
            else:
                data        = [] 
                error_message ="No response"
        else:
        # Handle API request failure
            data        = [] 
            error_message ="API failed"
        
    except Exception as e:
        # Handle any exceptions that occur during the API request 
        data        = []  
        error_message ="Try catch error"
    
    response_array  = {
                        "data": data,   
                        "error_message": error_message,    
                    }  
    return data

class Util:
    @staticmethod
    def send_email(data, multiple=False, is_content_html=False):
        to_email=[data["to_email"]]
        if multiple:
            to_email=data["to_email"]
        cc = data.get('cc',[])
        email = EmailMessage(
            subject=data["subject"],
            body=data["body"],
            from_email="contact@vitelglobal.com",
            to=to_email,
            cc=cc
        )
        if is_content_html:
            email.content_subtype = 'html'
        email.send()
        
        
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


def localize_dt(dt, tz=None):
    """
    Localize a datetime object

    """
    if tz is None:
        tz = settings.TIME_ZONE
    tz_obj = pytz.timezone(tz)

    return dt.astimezone(tz_obj) if dt.tzinfo else tz_obj.localize(dt)


def timezone_now(tz=settings.TIME_ZONE):
    """
    timezone.now() function with localized timezone

    """
    now = timezone.now()
    return localize_dt(now, tz)