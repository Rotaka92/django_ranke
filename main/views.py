from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from .models import Event, EventCategory
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='main/categories.html',
                  context={"categories": EventCategory.objects.all})
 

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})


def single_slug(request, single_slug):
    # first check to see if the url is in categories.

    categories = [c.category_slug for c in EventCategory.objects.all()]
    if single_slug in categories:
        matching_events = Event.objects.filter(event_category__category_slug=single_slug)
        event_urls = {}

        for m in matching_events.all():
            part_one = Event.objects.filter(event_category__event_category=m.event_category).earliest("event_published")
            event_urls[m] = part_one.event_slug

        return render(request=request,
                      template_name='main/category.html',
                      context={"event_title": matching_events, "part_ones": event_urls})


    events = [t.event_slug for t in Event.objects.all()]

    if single_slug in events:
        this_event = Event.objects.get(event_slug=single_slug)
        events_from_cat = Event.objects.filter(event_category__event_category=this_event.event_category).order_by('event_published')
        this_event_idx = list(events_from_cat).index(this_event)

        return render(request=request,
                      template_name='main/event.html',
                      context={"event": this_event,
                               "sidebar": events_from_cat,
                               "this_event_idx": this_event_idx})