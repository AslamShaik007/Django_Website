from django.http import HttpResponsePermanentRedirect

class RemoveSlashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        excluded_urls = ['/admin']

        if any(request.path.startswith(url) for url in excluded_urls):
            response = self.get_response(request)
        else:
            if request.path.endswith('/') and not request.path == '/':
                redirect_url = request.path[:-1]
                return HttpResponsePermanentRedirect(redirect_url)
            
            response = self.get_response(request)

        return response