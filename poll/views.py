from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage

from .forms import PdfForm
from .models import Pdf


# Create your views here.
def index(request):
    docs = Pdf.objects.all().order_by('-date')[:24]
    return render(request, 'index.html', {'docs': docs})


def search(request):
    context = {}

    if request.method == 'GET':
        searches = request.GET.get('searcher')

        if searches is not None:
            files = Pdf.objects.filter(Q(title__contains=searches) | Q(tags__contains=searches) |
                                       Q(uploader__contains=searches)).order_by('-date')

            paginator = Paginator(files, 18)
            page_number = request.GET.get('page', 1)

            try:
                files = paginator.page(page_number)
            except EmptyPage:
                files = paginator.page(paginator.num_pages)

            # choose a few
            context['search'] = searches
            context['docs'] = files
            return render(request, 'search.html', context)
        else:
            pass

    context['doc'] = Pdf.objects.all().order_by('-date')[:24]
    return render(request, 'search.html', context)


def download(request, pk):
    doc = Pdf.objects.get(id=pk)

    tags = doc.tags.split(',')
    new_tags = []

    for i in tags:
        new_tags.append(i.strip(' '))

    related = Pdf.objects.filter(Q(uploader__contains=doc.uploader) | Q(title__in=new_tags) |
                                 Q(tags__in=new_tags) | Q(uploader__in=new_tags))

    context = {
        "download": doc,
        "docs": related[:24],
    }
    return render(request, 'download.html', context)


def upload_(request):
    if request.method == "POST":
        form = PdfForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Document was successfully uploaded.")
            return redirect('index')
        else:
            messages.success(request, "An error occurred, enter valid data [urls].")
            return redirect('upload')
    else:
        form = PdfForm()

    context = {'form': form}
    return render(request, 'upload.html', context)
