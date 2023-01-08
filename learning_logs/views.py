from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import Topicform, Entryform
from .models import Entry, Topic


# Create your views here.
def index(request):
    """Render the home page of the application"""
    return render(request, 'learning_logs/index.html')

@login_required
def Topics(request):
    """Display all the topics order by date"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {
        'topics': topics
    }
    return render(request, 'learning_logs/topics.html', context=context)

@login_required
def topic(request, Topic_id):
    topic = Topic.objects.get(id=Topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic' : topic,
        'entries' : entries
    }
    return render(request, 'learning_logs/topic.html', context=context)

@login_required
def new_topic(request):
    """Add a topic"""
    if request.method != 'POST':
        """create empty form"""
        form = Topicform()
    else:
        """create valid form"""
        form = Topicform(request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('Topic'))
    context = {
        'form' : form
    }
    return render(request, 'learning_logs/new_topic.html', context=context)

@login_required
def new_entry(request, Entry_id):
    """Enter new options"""
    topic = Topic.objects.get(id=Entry_id)
    if request.method != 'POST':
        """create empty form"""
        form = Entryform()
    else:
        """create valid form"""
        form = Entryform(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[Entry_id]))
    context = {
        'form' : form,
        'topic' : topic
    }
    return render(request, 'learning_logs/new_entry.html', context=context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        #The initial request, so prefill form with the current entry
        form = Entryform(instance=entry)
    else:
        #else post data submitted, so we process it.
        form = Entryform(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    context = {
        'entry':entry,
        'topic':topic,
        'form': form
    }
    return render(request, 'learning_logs/edit_entry.html', context=context)