import json

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

COLORS = [
    (150, 231, 188),  # Light gray
]


def pars_json_data(file_path=None):
    if file_path is None:
        print("lol")
        return

    with open(file_path, "r") as data_file:
        data = json.load(data_file)[0]
        data_x, data_y = data["x"], data["y"]

    return data_x, data_y


# x, y = pars_json_data("music_maker_ai_accuracy_chart_data.json")

def my_next_color(color_list=COLORS):
    step = 0
    while True:
        for color in color_list:
            yield list(map(lambda base: (base + step) % 256, color))
        step += 197


def app(request):
    context = {
        'result': ''
    }
    try:
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
    except:
        pass
    return render(request, 'index.html', context)


class LineChartJSONView(BaseLineChartView):

    def get_labels(self):
        data_x, data_y = pars_json_data("1.json")
        """Return 7 labels for the x-axis."""
        return data_x[::9]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central"]

    def get_data(self):
        data_x, data_y = pars_json_data("1.json")
        """Return 3 datasets to plot."""
        print(len(data_y))
        return [data_y[::9]]


    def get_colors(self):
        return my_next_color()


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
