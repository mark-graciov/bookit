import ast
import os
import string
from wsgiref.util import FileWrapper

from django.conf import settings
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.crypto import random
from .docx import read_docx_tags, replace_docx_tags
from .forms import TaleForm
from .models import Tale, TaleTag


def _random_id():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))


def tale_list(request):
    tales = Tale.objects.all()
    img_path = os.path.join(settings.STATIC_URL, 'booksite/tales/tale1/preview/p1.jpg')

    return render(request, 'booksite/index.html', {'tale_list': tales, 'img_path': img_path})


def tale_details(request, tale_id):
    tale = Tale.objects.get(pk=tale_id)

    preview_dir = os.path.join(os.path.dirname(tale.doc_path), 'preview')
    preview_path = os.path.dirname(finders.find(tale.doc_path))
    preview_path = os.path.join(preview_path, 'preview')

    img_paths = []
    for (dirpath, dirnames, filenames) in os.walk(preview_path):
        for filename in filenames:
            img_paths.append(os.path.join(preview_dir, filename))
        break

    return render(request, 'booksite/tale_details.html', {'tale': tale, 'img_paths': img_paths})


def create_tale(request, tale_id):
    tale = Tale.objects.get(pk=tale_id)

    if request.method == 'POST':
        fields = ast.literal_eval(request.POST['tale__fields'])
        form = TaleForm(request.POST, fields=fields)

        if form.is_valid():
            r_id = _random_id()
            while r_id in request.session:
                r_id = _random_id()

            values = form.collect()
            request.session[r_id] = (tale_id, values)
            tale.downloads += 1
            tale.save()
            return redirect('download_tale', r_id)
    else:
        tags = read_docx_tags(finders.find(tale.doc_path))

        defined = TaleTag.objects.filter(name__in=tags).order_by('id')
        fields = []
        for tag in defined:
            fields.append((tag.name, tag.label, tag.help))
            tags.remove(tag.name)

        for tag in tags:
            fields.append((tag, tag, ''))

        form = TaleForm(fields=fields)

    return render(request, 'booksite/create_tale.html', {'tale': tale, 'form': form, 'fields': str(fields)})


def download_tale(request, s_id):
    s_tuple = request.session[s_id]
    tale = Tale.objects.get(pk=s_tuple[0])

    return render(request, 'booksite/download_tale.html', {'tale': tale, 's_id': s_id})




def download_tale_doc(request, s_id):
    s_tuple = request.session[s_id]
    tale = Tale.objects.get(pk=s_tuple[0])
    values = s_tuple[1]

    file = replace_docx_tags(finders.find(tale.doc_path), values)
    wrapper = FileWrapper(file)
    response = HttpResponse(wrapper, content_type='application/docx')
    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(tale.doc_path)
    response['Content-Length'] = file.tell()
    file.seek(0)
    return response

def despre_noi(request):
    return render(request, 'booksite/despre_noi.html', )
