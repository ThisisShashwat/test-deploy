from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path

settings.configure(DEBUG=False, SECRET_KEY="dummy-not-a-secret", ALLOWED_HOSTS=["*"], ROOT_URLCONF=__name__)

urlpatterns = [
    path("", lambda request: HttpResponse("<h1>Help Grandma Out</h1><p>Coming soon.</p>")),
    path("healthz", lambda request: HttpResponse("ok")),
]

application = get_wsgi_application()
