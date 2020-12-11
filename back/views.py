from django.shortcuts import render, HttpResponse
from .models import FileUpload
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from src.backend.main import get_result

classification = ['dog_bark',
                  'children_playing',
                  'car_horn',
                  'air_conditioner',
                  'street_music',
                  'gun_shot',
                  'siren',
                  'engine_idling',
                  'jackhammer',
                  'drilling']


def app(request):
    context = {
        'result': ''
    }

    if request.method == "POST":
        fileUPD = request.FILES["file"]
        if fileUPD.name.split(".")[-1] == "wav":
            document = FileUpload.objects.create(file=fileUPD)
            document.save()
            print("save")
            num = get_result()
            context['result'] = classification[num]
        else:
            context['result'] = 'Можно только WAV, Понял ДА НЕТ????'
    return render(request, 'index.html', context)


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""
        return [[0, 100, 0, 100, 0, 100, 0],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
