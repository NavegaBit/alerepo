import base64
from django.utils.html import mark_safe
from binary_database_files.models import File

from django.utils.translation import gettext_lazy as _


class ImageFieldShow:
    def image_tag(self):
        base_img = base64.b64encode(File.objects.get(name=self.image).content).decode('utf-8')
        return mark_safe(
            '<a href="{}"><img src = "data: image/png; base64, {}" width="150" height="100" loading="lazy"></a>'.
                format(
                    self.image.url,
                    base_img
                )
        )

    def image_ico(self):
        base_img = base64.b64encode(File.objects.get(name=self.ico).content).decode('utf-8')
        return mark_safe(
            '<a href="{}"><img src = "data: image/png; base64, {}" width="50" height="50" loading="lazy"></a>'.
                format(
                    self.ico.url,
                    base_img
                )
        )

    def image_logo(self):
        base_img = base64.b64encode(File.objects.get(name=self.logo).content).decode('utf-8')
        return mark_safe(
            '<a href="{}"><img src = "data: image/png; base64, {}" width="100" height="100" loading="lazy"></a>'.
                format(
                    self.logo.url,
                    base_img
                )
        )

    image_tag.short_description = _('Vista')
    image_tag.allow_tags = True


class Pagination:
    list_per_page = 25

