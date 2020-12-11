from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('app/', app),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
    path('chartJSON2', line_chart_json2, name='line_chart_json2'),
    path('chartJSON3', line_chart_json3, name='line_chart_json3'),
    path('chartJSON4', line_chart_json4, name='line_chart_json4'),
    path('chartJSON5', line_chart_json5, name='line_chart_json5'),
    path('chartJSON6', line_chart_json6, name='line_chart_json6')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
