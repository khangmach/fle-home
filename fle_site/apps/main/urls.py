
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView, RedirectView
from django.http import HttpResponseRedirect

from .views import process_donation, kolibri #, cc_indiegogo_signup

urlpatterns = patterns(__package__ + '.views',
    url(r'^$', TemplateView.as_view(template_name='main/homepage.html'), name='home'),
    # url(r'^cc_indiegogo_signup/$', 'cc_indiegogo_signup', name='cc_indiegogo_signup'),
    url(r'^indiegogo/', lambda request: HttpResponseRedirect(reverse('kolibri')), name='indiegogo'),
    url(r'^kolibri/$', kolibri, name='kolibri'),
    url(r'^indiegogo/.+$', lambda request: HttpResponseRedirect("https://www.generosity.com/fundraisers/kolibri-free-offline-app-for-universal-education/")),
    url(r'^map/$', RedirectView.as_view(url=reverse_lazy('map'))),
    url(r'^give/$', RedirectView.as_view(url=reverse_lazy('donate'))),
    url(r'^donationpage/$', RedirectView.as_view(url=reverse_lazy('donate'))),
    url(r'^directions/$', TemplateView.as_view(template_name='main/directions.html'), name='directions'),
    url(r'^donate/$', TemplateView.as_view(template_name='main/donationpage.html'), name='donate', kwargs={"STRIPE_PUBLISHABLE_API_KEY": settings.STRIPE_PUBLISHABLE_API_KEY}),
    url(r'^donate/process/$', process_donation, name='process_donation'),
    url(r'^donate/thankyou/$', TemplateView.as_view(template_name='main/donationpage_thankyou.html'), name='donationpage_thankyou'),
    url(r'^translate/$',  TemplateView.as_view(template_name='main/translate.html'), name='translate'),
    url(r'^download/$',  TemplateView.as_view(template_name='main/download.html'), name='download'),
    url(r'^documentation/$',  TemplateView.as_view(template_name='main/documentation.html'), name='docs'),
    url(r'^hardware_grant/$',  TemplateView.as_view(template_name='main/hardware_grant.html'), name='hardware_grant')
)
