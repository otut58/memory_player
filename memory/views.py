from django.http import HttpResponse 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from memory.models import Memory, Viewer_Comment
from memory.forms import MemoryForm, SearchForm, ViewerCommentForm

def top(request):
    memories = Memory.objects.order_by('-xp')
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        weapon_choiced = searchForm.cleaned_data['weapon_choiced']
        stage_choiced = searchForm.cleaned_data['stage_choiced']
        rule_choiced = searchForm.cleaned_data['rule_choiced']
        if (weapon_choiced != '') and (weapon_choiced != '---'):
            memories = memories.filter(weapon=weapon_choiced)
        if (stage_choiced != '') and (stage_choiced != '---'):
            memories = memories.filter(stage=stage_choiced)
        if (rule_choiced != '') and (rule_choiced != '---'):
            memories = memories.filter(rule=rule_choiced)
    weapons = [weapon[0] for weapon in Memory._meta.get_field('weapon').choices]
    stages = [stage[0] for stage in Memory._meta.get_field('stage').choices]
    rules = [rule[0] for rule in Memory._meta.get_field('rule').choices]
    context = {"memories" : memories, "weapons" : weapons, "stages" : stages, "rules" : rules, 'searchForm': searchForm}
    return render(request, "memory/top.html", context)

def memory_new(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.created_by = request.user
            memory.save()
            return redirect(top)
    else:
        form = MemoryForm()
    return render(request, "memory/memory_new.html", {'form' : form})

def memory_detail(request, memory_id):
    memory = get_object_or_404(Memory, pk=memory_id)
    viewer_comment = memory.viewer_comment_set.all()
    new_v_comment = list(reversed([c.viewer_comment for c in viewer_comment]))
    if len(new_v_comment) > 10:
        new_v_comment = new_v_comment[0:10]
    context = {
        'memory' : memory, 
        'new_v_comment' : new_v_comment, 
        'form' : ViewerCommentForm(),
    }
    return render(request, 'memory/memory_detail.html', context)


@require_POST
def create_comment(request, memory_id):
    form = ViewerCommentForm(request.POST)
    if form.is_valid():
        viewercomment = form.save(commit=False)
        viewercomment.memory = get_object_or_404(Memory, pk=memory_id)
        viewercomment.save()
        return redirect('memory_detail', memory_id)

    memory = get_object_or_404(Memory, pk=memory_id)
    viewer_comment = memory.viewer_comment_set.all()
    new_v_comment = list(reversed([c.viewer_comment for c in viewer_comment]))
    if len(new_v_comment) > 10:
        new_v_comment = new_v_comment[0:10]
    context = { 
        'memory' : memory, 
        'new_v_comment' : new_v_comment, 
        'form': form,
    }
    return render(request, 'memory/memory_detail.html', context)