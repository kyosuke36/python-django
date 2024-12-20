from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse
from django.template import loader
from event.models import Choice, Event


def index(request):
    events = Event.objects.all()
    template = loader.get_template("event/index.html")
    context = {"event_list": events}
    return HttpResponse(template.render(context, request))


def create(request):
    event_text = request.POST["text"]

    e = Event()
    e.event_text = event_text
    e.save()

    return HttpResponseRedirect(reverse("event:index"))


def edit(request, event_id):
    template = loader.get_template("event/edit.html")
    target_event = Event.objects.get(id=event_id)
    context = {"event": target_event}
    return HttpResponse(template.render(context, request))


def update(request, event_id):
    target_event = Event.objects.get(id=event_id)
    target_event.event_text = request.POST.get("text")
    target_event.save()
    return HttpResponseRedirect(reverse("event:index"))


def delete(request, event_id):
    target_event = Event.objects.get(id=event_id)
    target_event.delete()

    return HttpResponseRedirect(reverse("event:index"))


def date(request, event_id):
    template = loader.get_template("event/date.html")
    target_event = Event.objects.get(id=event_id)

    context = {"event": target_event}
    return HttpResponse(template.render(context, request))


def create_date(request, event_id):
    e = Event.objects.get(id=event_id)
    choice_text = request.POST.get("choice")
    c = Choice()
    c.event = e
    c.text = choice_text
    c.save()
    return HttpResponseRedirect(reverse("event:date", args=(event_id,)))


def choice_delete(request, choice_id):
    target_choice = Choice.objects.get(id=choice_id)
    event_id = target_choice.event.id
    target_choice.delete()

    return HttpResponseRedirect(reverse("event:date", args=(event_id,)))
