from django.views.generic import ListView
from django.shortcuts import render_to_response
from banners.models import Banner
from cards_api.models import Card
from subscribed_people.forms import SubscribeForm


class MainPage(ListView):
    model = Card
    template_name = 'main_page/main_page.html'
    paginate_by = 10
    context_object_name = 'cards'

    def get_context_data(self, **kwargs):
        ctx = super(MainPage, self).get_context_data(**kwargs)
        ctx['banners'] = {b['slug']: b['image'] for b in Banner.objects.values()}
        ctx['form'] = SubscribeForm()
        ctx['is_json'] = self.request.GET.get('json')
        return ctx

    def render_to_response(self, context, **response_kwargs):
        if context['is_json']:
            return render_to_response('main_page/landing.html', context)
        response = super(MainPage, self).render_to_response(context)
        return response
