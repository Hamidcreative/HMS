from django.http import HttpResponseRedirect,  HttpResponse
import requests

class AuthenticateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        return self.loginCheck(request)

    def loginCheck(self, request):
        if not request.user.is_authenticated and request.path != '/login':
            return HttpResponseRedirect('/login') # or http response
        elif request.user.is_authenticated:
            if request.path == 'api/login/' or request.path == '/login' or request.path == '/':
                return HttpResponseRedirect('/users-dashboard')
        return self.get_response(request)