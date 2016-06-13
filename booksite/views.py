import os
from django.conf import settings
from django.shortcuts import render
from .models import Tale


def tale_list(request):
    tales = Tale.objects.all()
    img_path = os.path.join(settings.STATIC_URL, 'booksite/tales/tale1/preview/p1.jpg')

    return render(request, 'booksite/index.html', {'tale_list': tales, 'img_path': img_path})


def tale_details(request, tale_id):
    tale = Tale.objects.get(pk=tale_id)

    preview_dir = os.path.join(os.path.dirname(tale.pdf_path), 'preview')
    preview_path = os.path.join(settings.BASE_DIR, 'booksite/static', preview_dir)

    img_paths = []
    for (dirpath, dirnames, filenames) in os.walk(preview_path):
        for filename in filenames:
            img_paths.append(os.path.join(settings.STATIC_URL, preview_dir, filename))
        break

    return render(request, 'booksite/tale_details.html', {'tale': tale, 'img_paths': img_paths})


def create_tale(request, tale_id):
    tale=Tale.objects.get(pk=tale_id)
    return render(request, 'booksite/create_tale.html', {"tale" : tale})


    tale = Tale.objects.get(pk=tale_id)
    return render(request, 'booksite/create_tale.html', {"tale": tale})

