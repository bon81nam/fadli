from django.shortcuts import render
from .forms import InputForm
from .models import InputFormModel
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .filter import ActivityFilter


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required(login_url=settings.LOGIN_URL)
def forms(request):
    if request.POST:
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            form = InputForm
            pesan = "Data Berjaya Disimpan. Terima Kasih"
            context = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'forms.html', context)
    else:
        form = InputForm
        context = {
               'form': form,
        }

        return render(request, 'forms.html', context)


@login_required(login_url=settings.LOGIN_URL)
def activity(request):
    aktiviti = InputFormModel.objects.all()
    act_filter = ActivityFilter(request.GET, queryset=aktiviti)
    aktiviti = act_filter.qs
    konteks = {
        'aktiviti': aktiviti,
        'act_filter': act_filter
    }
    return render(request, 'activity.html', konteks)


def borang_akt(request):
    aktiviti = InputFormModel.objects.all()
    act_filter = ActivityFilter(request.GET, queryset=aktiviti)
    aktiviti = act_filter.qs
    konteks = {
        'aktiviti': aktiviti,
        'act_filter': act_filter
    }
    return render(request, 'borang_akt.html', konteks)


def PEO(request):
    return render(request, 'PEO.html')
