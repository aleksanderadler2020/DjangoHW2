from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    bus_stations = []
    with open(settings.BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            bus_stations.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)
    # Не понял в чем разница? Текущая страница = срез общего списка станций,
    # и список станций на этой странице... это же одно и тоже.
    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
