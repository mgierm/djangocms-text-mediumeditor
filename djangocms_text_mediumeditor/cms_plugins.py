# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.utils.conf import get_cms_setting

from .forms import MediumEditorTextForm
from .models import MediumEditorText


class MediumEditorTextPlugin(CMSPluginBase):
    model = MediumEditorText
    form = MediumEditorTextForm
    name = _("Text")
    render_template = "cms/plugins/mediumeditor_text.html"
    change_form_template = "cms/plugins/mediumeditor_text_change_form.html"

    def render(self, context, instance, placeholder):
        context.update({
            "body": instance.body,
            "placeholder": placeholder,
            "object": instance,
        })
        return context

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        """
        We just need the popup interface here
        """
        context.update({
            'preview': "no_preview" not in request.GET,
            'is_popup': False,
            'plugin': obj,
            'CMS_MEDIA_URL': get_cms_setting('MEDIA_URL'),
        })

        return super().render_change_form(request, context, add, change, form_url, obj)


plugin_pool.register_plugin(MediumEditorTextPlugin)
