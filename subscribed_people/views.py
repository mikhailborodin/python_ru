from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from subscribed_people.models import SubscribedPerson


class SubscribeCreate(CreateView):
    model = SubscribedPerson
    fields = ['email']
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        db_email = SubscribedPerson.objects.filter(email=email)
        if not db_email:
            return super(SubscribeCreate, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')
