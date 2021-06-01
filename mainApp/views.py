from builtins import int
import random
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from django.core.mail import send_mail, BadHeaderError

from regMembers.settings import DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL
from .models import Conference, Member, auth
from .forms import ConferenceForm


def home(request):
    conference_list = Conference.objects.order_by('-date')[:99]
    context = {'conference_list': conference_list}
    return render(request, 'mainApp/home.html', context)


def result(request, conference_id):
    data = request.POST
    name = data['name']
    last_name = data['last_name']
    email = data['email']
    phone = data['phone']
    invite_code = rand_x_digit_num(6)
    member = Member(name=name, last_name=last_name, email=email, phone=phone, invitation_code=invite_code,
                    conference_id=conference_id)
    member.save()

    context = {'members': member}
    try:
        send_mail(f'Привет от ','fsdf',
                  DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
    except BadHeaderError:
        return HttpResponse('Ошибка!')
    return render(request, 'mainApp/result.html', context)


def edit(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    if request.method == "POST":
        form = ConferenceForm(request.POST, instance=conference)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('admin')
    else:
        form = ConferenceForm(instance=conference)
    return render(request, 'mainApp/edit.html', {'form': form})


def requests(request, conference_id):
    conference_id = conference_id
    context = {
        'conference_id': conference_id,
        'members_list': Member.objects.order_by('conference_id'),
        'conference': Conference.objects.get(id=conference_id),
    }
    return render(request, 'mainApp/requests.html', context)


def create_conference(request):
    error = ''
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.admin_id = request.user.id
            obj.save()
            return redirect('admin')
        else:
            error = 'Ошибка заполнения формы!'

    form = ConferenceForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainApp/create_conference.html', data)


class RegConference(DetailView):
    model = Conference
    template_name = 'mainApp/reg_conference.html'


def admin_conference(request):
    conference_list = Conference.objects.order_by('-date')[:99]
    none = ''
    context = {
        'conference_list': conference_list,
        'members_list': Member.objects.order_by('conference_id'),
        'none': none
    }
    return render(request, 'mainApp/admin.html', context)


def delete(request, conference_id):
    Conference.objects.get(id=conference_id).delete()
    return redirect('admin')


def rand_x_digit_num(x, leading_zeroes=True):
    if not leading_zeroes:
        # wrap with str() for uniform results
        return random.randint(10 ** (x - 1), 10 ** x - 1)
    else:
        if x > 6000:
            return ''.join([str(random.randint(0, 9)) for i in xrange(x)])
        else:
            return '{0:0{x}d}'.format(random.randint(0, 10 ** x - 1), x=x)
