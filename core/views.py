from django.shortcuts import render, redirect

from core.forms import SearchForm
from core.models import LostDocuments
from core.related_funcs import upload_docs


def search_docs(request):
    upload_docs()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            ser_num = form.cleaned_data["ser_num"]
            if len(ser_num) == 9:
                ser_num.strip()
            ser = ser_num[:2]
            num = ser_num[2:]
            docs = LostDocuments.objects.filter(series=ser, doc_num=num)
            return render(request, "core/results.html", {"docs": docs})
    else:
        form = SearchForm()

    return render(request, 'core/index.html', {'form': form})

