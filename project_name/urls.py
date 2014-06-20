from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

from project_name.views import homepage
from project_name.profiles.views import ProfileDetailView, ProfileEditView, ProfileListView


from .lookups import user_wiki_lookup, team_wiki_lookup


urlpatterns = patterns(
    "",
    url(r"^$", homepage, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^invites/", include("kaleo.urls")),

    url(r"^profile/edit/", ProfileEditView.as_view(), name="profiles_edit"),
    url(r"^u/$", ProfileListView.as_view(), name="profiles_list"),

    url(r"^u/(?P<username>[\w\._-]+)/$", ProfileDetailView.as_view(), name="profiles_detail"),
    url(r"^u/(?P<username>[\w\._-]+)/w/$", "project_name.wiki.views.index", {"wiki_lookup": user_wiki_lookup}, name="user_wiki_index"),
    url(r"^u/(?P<username>[\w\._-]+)/w/(?P<slug>[^/]+)/$", "project_name.wiki.views.page", {"wiki_lookup": user_wiki_lookup}, name="user_wiki_page"),
    url(r"^u/(?P<username>[\w\._-]+)/w/(?P<slug>[^/]+)/edit/$", "project_name.wiki.views.edit", {"wiki_lookup": user_wiki_lookup}, name="user_wiki_page_edit"),

    url(r"^t/", include("project_name.teams.urls")),
    url(r"^t/(?P<team_slug>[\w\-]+)/w/$", "project_name.wiki.views.index", {"wiki_lookup": team_wiki_lookup}, name="team_wiki_index"),
    url(r"^t/(?P<team_slug>[\w\-]+)/w/(?P<slug>[^/]+)/$", "project_name.wiki.views.page", {"wiki_lookup": team_wiki_lookup}, name="team_wiki_page"),
    url(r"^t/(?P<team_slug>[\w\-]+)/w/(?P<slug>[^/]+)/edit/$", "project_name.wiki.views.edit", {"wiki_lookup": team_wiki_lookup}, name="team_wiki_page_edit"),

    url(r"^w/file-download/(\d+)/([^/]+)$", "project_name.wiki.views.file_download", name="wiki_file_download"),
    url(r"^a/file-upload/$", "project_name.wiki.views.file_upload", name="wiki_file_upload")
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
