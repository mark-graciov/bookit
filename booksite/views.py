import os
import re
import ast

from django.conf import settings
from django.contrib.staticfiles import finders
from django.shortcuts import render, redirect
from docx import Document
from .forms import TaleForm
from .models import Tale, TaleTag


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
            # do something
            return redirect('generate_tale', tale_id)
    else:
        doc = Document(finders.find(tale.doc_path))
        pattern = re.compile(r'<([a-zA-Z0-9_]+)>')

        tags = []
        for p in doc.paragraphs:
            matches = re.findall(pattern, p.text)
            tags.extend(matches)
        tags = set(tags)

        defined = TaleTag.objects.filter(name__in=tags).order_by('id')
        fields = []
        for tag in defined:
            fields.append((tag.name, tag.label, tag.help))
            tags.remove(tag.name)

        for tag in tags:
            fields.append((tag, tag, ''))

        form = TaleForm(fields=fields)

    return render(request, 'booksite/create_tale.html', {'tale': tale, 'form': form, 'fields': str(fields)})
