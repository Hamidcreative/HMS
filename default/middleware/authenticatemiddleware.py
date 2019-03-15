from django.http import HttpResponseRedirect,  HttpResponse
import requests
from django.shortcuts import render, redirect

class AuthenticateMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		# One-time configuration and initialization.

	def __call__(self, request):
		# Code to be executed for each request before
		# the view (and later middleware) are called.

		return self.loginCheck(request)

	def loginCheck(self, request):
		if '/api/' not in request.path:
			if request.session.has_key('token') and (request.path == '/login' or request.path == '/api/login'):
				  return redirect('/users-dashboard')
			elif not request.session.has_key('token') and request.path != '/login' and request.path != '/api/login':
				  return redirect('/login')
		return self.get_response(request)