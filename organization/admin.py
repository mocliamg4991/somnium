from django.contrib import admin
from .models import Position, Subdivision
from mptt.admin import DraggableMPTTAdmin
# Register your models here.
admin.site.register(
    Position,
    DraggableMPTTAdmin,
    list_display=(

        'tree_actions',
        'indented_title',
        'name',
        'parent',
    ),
    list_display_links=(
        'name',
    ),
)

admin.site.register(
    Subdivision,
    DraggableMPTTAdmin,
    list_display=(

        'tree_actions',
        'indented_title',
        'name',
        'parent',
    ),
    list_display_links=(
        'name',
    ),
)