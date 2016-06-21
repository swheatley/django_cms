from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PollsApphook(CMSApp):
    name = ("Polls Application")
    app_name = "polls"
    _urls = ["polls.urls"]


apphook_pool.register(PollsApphook)
