import json

from django.shortcuts import render, HttpResponse
from .models import FileUpload
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from src.backend.main import get_result
import base64


classification = [
    'Air conditioner',
    'Car horn',
    'Children playing',
    'Dog bark',
    'Drilling',
    'Engine idling',
    'Gun shot',
    'Jackhammer',
    'Siren',
    'Street music']

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
        'result': 'Check my WAV'
    }

    if request.method == "POST":
        try:
            fileUPD = request.FILES["file"]
            if fileUPD.name.split(".")[-1] == "wav":
                document = FileUpload.objects.create(file=fileUPD)
                document.save()
                print("save")
                num = get_result(fileUPD.name)
                context['result'] = classification[num]
                with open("media/audio.png", "rb") as imageFile:
                    str = base64.b64encode(imageFile.read())
                    context['img_src'] = "data:image/png;base64," + str.decode("utf-8")

            else:
                context['result'] = 'Only .wav allowed'
        except:
            context['result'] = 'No file :('
    return render(request, 'index.html', context)


class LineChartJSONView(BaseLineChartView):
    file_name = None
    chart_name = None
    color = None

    def get_labels(self):
        data_x, data_y = pars_json_data(self.file_name)
        """Return 7 labels for the x-axis."""
        return data_x[::1]

    def get_providers(self):
        """Return names of datasets."""
        return [self.chart_name]

    def get_data(self):
        data_x, data_y = pars_json_data(self.file_name)
        """Return 3 datasets to plot."""
        print(len(data_y))
        return [data_y[::1]]

    def get_colors(self):
        return my_next_color(self.color)


line_chart = TemplateView.as_view(template_name='line_chart.html')

line_chart_json = LineChartJSONView.as_view(file_name="1_1.json", chart_name="Accuracy", color=[(255, 0, 0)])
line_chart_json2 = LineChartJSONView.as_view(file_name="1_2.json", chart_name="Loss", color=[(255, 153, 0)])
line_chart_json3 = LineChartJSONView.as_view(file_name="2_1.json", chart_name="Batch accuracy", color=[(255, 216, 0)])
line_chart_json4 = LineChartJSONView.as_view(file_name="2_2.json", chart_name="Batch loss", color=[(0, 255, 0)])
line_chart_json5 = LineChartJSONView.as_view(file_name="3_1.json", chart_name="Val accuracy", color=[(0, 0, 255)])
line_chart_json6 = LineChartJSONView.as_view(file_name="3_2.json", chart_name="Val loss", color=[(255, 0, 255)])
