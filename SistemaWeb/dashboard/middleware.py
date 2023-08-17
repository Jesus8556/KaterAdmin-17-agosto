# middleware.py
from django.utils import timezone

from django.shortcuts import redirect
from django.urls import reverse


class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.session['last_activity'] = str(timezone.now())
        return self.get_response(request)
    

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not self.is_exempt(request):
            return redirect('login')

        response = self.get_response(request)
        return response

    def is_exempt(self, request):
        # Agrega aquí las URL que deseas excluir de la autenticación
        exempt_urls = [reverse('login'), reverse('password_reset'), reverse('registro')]
        return any(request.path.startswith(url) for url in exempt_urls)