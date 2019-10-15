from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import TemplateView
from . import plots


# Create your views here.
def history(request):
    return render(request, 'index.html')


class Graphs(TemplateView):
    template_name = 'plot.html'

    def get_graphs(self, **kwargs):
        context = super(Graphs, self).get_graphs(**kwargs)
        context['3dplot'] = plots.get_graph()
        return context

