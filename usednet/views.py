from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Content

def home(request):
    contents = Content.objects.all().order_by('-date_posted')[:3]  # Limit to latest 1-3 items
    return render(request, 'home.html', {'contents': contents})

from django.shortcuts import get_object_or_404

def content_detail(request, pk):
    content = get_object_or_404(Content, pk=pk)
    branches = content.branches.filter(parent__isnull=True)
    return render(request, 'content_detail.html', {'content': content, 'branches': branches})

def branch_detail(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    responses = branch.responses.all()
    return render(request, 'branch_detail.html', {'branch': branch, 'responses': responses})

from django.shortcuts import redirect
from .forms import BranchForm

def add_branch(request, content_pk=None, parent_pk=None):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            if content_pk:
                branch.content = get_object_or_404(Content, pk=content_pk)
            if parent_pk:
                branch.parent = get_object_or_404(Branch, pk=parent_pk)
            branch.save()
            return redirect('branch_detail', pk=branch.pk)
    else:
        form = BranchForm()
    return render(request, 'add_branch.html', {'form': form})

def tag_view(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    contents = tag.contents.all()
    return render(request, 'tag.html', {'tag': tag, 'contents': contents})

