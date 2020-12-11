from django.urls import path
from .views import app, line_chart, line_chart_json
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('app/', app),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
