from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import Q

from .models import Task, Member
from .forms import TaskForm, SearchForm


# Landing page
def index(request):
    try:
        task_list = Task.objects.order_by('due_date')
        form = SearchForm()

    except Task.DoesNotExist:
        raise HttpResponse('No tasks available.')

    return HttpResponse(task_list)
    # return render(request, 'tasks/index.html', {'task_list': task_list, 'form': form})


# Show details of a task
def details(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    # Get members
    members = task.member_set.all()

    return render(request, 'tasks/details.html', {'task': task, 'members': members})


# Create a new task
def create(request):
    # If this is a POST request we need to process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = TaskForm(request.POST)

        # Check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            owner = form.cleaned_data['owner']
            status = form.cleaned_data['status']
            due_date = form.cleaned_data['due_date']

            task = Task(title=title, description=description, owner=owner, status=status, due_date=due_date)
            task.save()
            task_id = task.id

            # Redirect to a new URL:
            return HttpResponseRedirect(reverse('details', args=(task_id,)))

        else:
            return Http404('Something went wrong. Please try again.')

    # If a GET (or any other method) create a blank form
    else:
        form = TaskForm()
        return render(request, 'tasks/create.html', {'form': form})


# Edit a task
def edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    # Get members
    members = task.member_set.all()

    return render(request, 'tasks/edit.html', {'task': task, 'members': members})


# Save a task
def save(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    try:
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.owner = request.POST['owner']
        task.status = request.POST['status']
        task.due_date = request.POST['due_date']

        task.save()

        # Add member if input available
        if request.POST['member']:
            task.member_set.create(name=request.POST['member'])

    except(KeyError, Task.DoesNotExist):
        return render(request, 'tasks/details.html', {'task': task,
                                                      'error_message': "Input incorrect. Please try again."})

    # Delete any selected members
    Member.objects.filter(id__in=request.POST.getlist('member_delete')).delete()

    return HttpResponseRedirect(reverse('details', args=(task.id,)))


# Delete a task
# Any associated members are deleted in cascade
def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    try:
        task.delete()
        return HttpResponseRedirect(reverse('index'))

    except(KeyError, Task.DoesNotExist):
        return render(request, 'tasks/details.html', {'task': task,
                                                      'error_message': "Input incorrect. Please try again."})


# Search task by title, description, owner or status
def search(request):
    try:
        # Get search value
        search_value = request.GET['search_value']

        # Get tasks that match the search value (case-insensitive)
        search_task_list = Task.objects.filter(Q(title__icontains=search_value) |
                                               Q(description__icontains=search_value)|
                                               Q(owner__icontains=search_value)|
                                               Q(status__icontains=search_value)).order_by('due_date')
        # Create a form instance
        form = SearchForm()

        return render(request, 'tasks/search.html', {'task_list': search_task_list, 'form': form})

    except:
        return Http404('Something went wrong. Please try again.')
