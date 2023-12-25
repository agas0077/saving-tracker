# Third Party Library
from django.conf import settings
from django.shortcuts import redirect


class LoginRequiredMiddleware:
    """
    Проверяет авторизован ли пользователь.
    При необходимости, перенаправляет его на страницу входа.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL
        self.open_urls = [self.login_url] + getattr(settings, "OPEN_URLS", [])

    def __call__(self, request):
        is_open_url = any(
            [True for url in self.open_urls if url in request.path_info]
        )
        if not request.user.is_authenticated and not is_open_url:
            return redirect(self.login_url)

        return self.get_response(request)
