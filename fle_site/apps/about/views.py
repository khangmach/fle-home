import json
import os
import random

from django.conf import settings

from annoying.decorators import render_to

from models import TeamMember, BoardMember, PressArticle, Internship, Job, SupportingOrganization, Translator

@render_to("about/team.html")
def team(request):
    return {
        "team_members": TeamMember.objects.current(),
        "alumni": TeamMember.objects.alumni(),
    }

@render_to("about/board.html")
def board(request):
    return {
        "board_members": BoardMember.objects.board(),
        "advisor_members": BoardMember.objects.advisor()
    }

@render_to("about/press.html")
def press(request):
    return {
        "press_articles": PressArticle.objects.order_by('-publish_date')
    }

@render_to("about/internships.html")
def internships(request):
    return {
        "internships": Internship.objects.all()
    }

@render_to("about/jobs.html")
def jobs(request):
    return {
        "jobs": Job.objects.active()
    }

@render_to("about/grants.html")
def grants(request):
    return {
        "jobs": Job.objects.active()
    }

@render_to("about/supporters.html")
def supporters(request):
    sponsors = SupportingOrganization.objects.filter(organization_type__title="sponsor")
    partners = SupportingOrganization.objects.filter(organization_type__title="partner")
    return {
        "sponsors": sponsors,
        "partners": partners
    }

@render_to("about/translators.html")
def translators(request):
    return {
        "translators": Translator.objects.order_by("?")
    }
