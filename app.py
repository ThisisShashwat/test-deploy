import environ
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.db import connection
from django.http import HttpResponse
from django.urls import path

env = environ.Env()
database_url = env("DATABASE_URL", default="")

settings.configure(
    DEBUG=False, SECRET_KEY="dummy-not-a-secret", ALLOWED_HOSTS=["*"], ROOT_URLCONF=__name__,
    DATABASES={"default": env.db("DATABASE_URL")} if database_url else {},
)


def dbcheck(request):
    if not database_url:
        return HttpResponse("DATABASE_URL is not set", status=503)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
    except Exception as error:      # only the class name: the message can carry the host or user
        return HttpResponse(f"database connection failed: {type(error).__name__}", status=503)
    return HttpResponse(f"database connection ok ({connection.vendor})")


urlpatterns = [
    path("", lambda request: HttpResponse("<h1>Help Grandma Out</h1><p>Coming soon.</p>")),
    path("healthz", lambda request: HttpResponse("ok")),
    path("dbcheck", dbcheck),
]

application = get_wsgi_application()
