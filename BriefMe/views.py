from django.shortcuts import render, redirect
from .forms import BriefForm
from .models import Brief


def create_brief(request):
    form = BriefForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('briefs_list')

    return render(request, 'form.html', {'form': form})


def briefs_list(request):
    briefs = Brief.objects.all().order_by('-created_at')
    return render(request, 'brief_list.html', {'briefs': briefs})
