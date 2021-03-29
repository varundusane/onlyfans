from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from scraped.models import Details,image,Video


def home_view(request):
    page_no = request.GET.get('page', 1)

    works = Details.objects.all().order_by('-id')
    # restaurents = Restaurents.objects.all().order_by('-avarage_ratings')
    paginator = Paginator(works, 20)
    try:
        j = paginator.page(page_no)

    except PageNotAnInteger:
        j = paginator.page(1)

    except EmptyPage:
        j = paginator.page(paginator.num_pages)
    context = {}
    context['jobs']=j
    return render(request, 'index.html', context)


def jobDetails(request, id):
    try:
        try:
            im = image.objects.filter(author=Details.objects.get(id=id))
        except image.DoesNotExist:
            pass
        try:
            vi = Video.objects.filter(author=Details.objects.get(id=id))
        except Video.DoesNotExist:
            pass
    except Details.DoesNotExist:
        return redirect('index')

    context = {
        "images": im,
        "videos":vi

    }
    return render(request, 'jobDetails.html', context)