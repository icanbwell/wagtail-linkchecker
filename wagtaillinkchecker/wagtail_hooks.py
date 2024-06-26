from __future__ import unicode_literals

from django.urls import include, re_path, reverse
from django.utils.translation import gettext_lazy as _

from wagtaillinkchecker import urls

from wagtail.admin.menu import MenuItem
from wagtail.core import hooks



@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^link-checker/', include(urls)),
    ]


@hooks.register('register_settings_menu_item')
def register_menu_settings():
    return MenuItem(
        _('Link Checker'),
        reverse('wagtaillinkchecker'),
        classnames='icon icon-link',
        order=300
    )
