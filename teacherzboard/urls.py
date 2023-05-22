from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from schools.views import home, jobboard, schools

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("jobs/", jobboard, name="jobs"),
    path("schools/", schools, name="schools"),
]

# add this lines
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
