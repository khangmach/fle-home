from django.conf.urls.defaults import *
from django.http import HttpResponseRedirect

from fle_site.apps.articles import views

urlpatterns = patterns('',

	# hardcoded redirects from old legacy blog URLs to the new locations on Medium
	url(r'^2016/learning-equality-nigeria-2/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/learning-equality-in-ekiti-state-nigeria-c37524ee48a0")),
	url(r'^2016/community-forums/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/were-bringing-back-our-community-forums-a23f82ad79cd")),
	url(r'^2016/yak-shaving-and-other-ways-change-world/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/learning-equality-core-values-learn-constantly-and-yak-shave-to-change-the-world-4e512c46744")),
	url(r'^2016/ka-lite-version-0166-released/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/ka-lite-version-0-16-6-released-5ae0cd3e0341")),
	url(r'^2016/learning-equality-nigeria/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/learning-equality-world-bank-group-ministry-of-education-bring-digital-learning-to-ekiti-state-fbd4f718f3df")),
	url(r'^2016/funsepa-rct/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/rural-guatemalan-schools-see-improvement-in-math-performance-through-the-use-of-education-a3257b97df2")),
	url(r'^2016/samuel-morris-scholars-program-returns/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/update-samuel-morris-scholars-program-returns-to-liberia-f71203cdb820")),
	url(r'^2015/ka-lite-015-released/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/ka-lite-0-16-released-64cd95ae5e73")),
	url(r'^2016/team4tech-around-world/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/deployment-spotlight-team4tech-deploys-ka-lite-in-south-africa-tanzania-and-india-5f95397eb5c4")),
	url(r'^2015/ka-lite-015-released/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/ka-lite-0-15-released-e3f4fb8d3547")),
	url(r'^2015/deployment-spotlight-ka-lite-making-great-strides-/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/deployment-spotlight-ka-lite-is-making-great-strides-in-rural-schools-in-south-africa-aaa30dd5237a")),
	url(r'^2015/ka-lite-014-release-blog-post/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/ka-lite-0-14-released-a56c95863b81")),
	url(r'^2015/give-it-whirl/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/give-it-a-whirl-1dcce45a8f04")),
	url(r'^2015/ka-lite-013-released/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/ka-lite-0-13-released-3d117dc14298")),
	url(r'^2015/deployment-spotlight-ashaiman-ghana/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/deployment-spotlight-ashaiman-ghana-22cdfa4eae28")),
	url(r'^2015/empower/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/learning-equality-core-values-empower-fb43f0ed2079")),
	url(r'^2014/education-behind-bars/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/how-to-get-an-education-behind-bars-94292607c52a")),
	url(r'^2014/core-value-series-be-proactive/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/learning-equality-core-values-be-proactive-e168545744ab")),
	url(r'^2014/small-cambodian-village-experiences-ka-lite/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/a-small-cambodian-village-experiences-ka-lite-67751a7f285f")),
	url(r'^2014/deployment-spotlight-ka-lite-rural-guatemala/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/deployment-spotlight-ka-lite-in-rural-guatemala-ec6d991ea802")),
	url(r'^2014/ka-lite-typhoon-stricken-mangorocoro/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/ka-lite-in-typhoon-stricken-mangorocoro-c781aa9c4cb4")),
	url(r'^2014/deployments-map-launch/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/is-ka-lite-in-your-neighborhood-see-fles-deployments-map-63544739ab1e")),
	url(r'^2014/ka-lite-update-012/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/announcing-ka-lite-version-0-12-15e28c178e05")),
	url(r'^2014/samuel-morris-scholars-program-unforgettable-impac/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/samuel-morris-scholars-program-an-unforgettable-impact-99f28a5faeff")),
	url(r'^2014/i18n-released/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/announcing-ka-lite-version-0-11-with-i18n-support-a0cbbcdeb221")),
	url(r'^2014/i18n-beta-release/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/i18n-beta-release-d4f1b02fe0be")),
	url(r'^2014/ka-lite-internationalization-coming-soon/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/ka-lite-internationalization-coming-soon-9f51b4ff12e4")),
	url(r'^2013/bringing-ka-lite-gitwe/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/bringing-ka-lite-to-gitwe-rwanda-38872419b1ac")),
	url(r'^2013/big-ideas-fest-2013/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/big-ideas-fest-2013-1cdaeaaf9c5")),
	url(r'^2013/fle-forums-place-share-learn-and-grow/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/fle-forums-a-place-to-share-learn-and-grow-4a186b275576")),
	url(r'^2013/inspiring-confidence-by-edward-j-hills/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/inspiring-confidence-a-guest-post-from-edward-j-hills-28719ed03196")),
	url(r'^2013/ka-lite-brings-offline-education-idaho-department-/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/ka-lite-brings-offline-education-to-idaho-department-of-corrections-90f7a5f1bf4b")),
	url(r'^2013/sparks-family/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/the-sparks-familys-overland-travel-from-alaska-to-argentina-dedde75a145")),
	url(r'^2013/announcing-version-0-point-ten-ka-lite/', lambda request: HttpResponseRedirect("https://blog.learningequality.org/announcing-version-0-10-0-of-ka-lite-e40c9fe1c405")),

	# redirect base blog URL to new base blog URL on Medium
	url(r'^', lambda request: HttpResponseRedirect("https://blog.learningequality.org/"), name="blog"),

    # url(r'^$', views.blog_filter_page, name="blog"),
    # url(r'^(?P<year>\d{4})/(?P<slug>.*)/$', views.display_article, name="articles_display_article"),

)
