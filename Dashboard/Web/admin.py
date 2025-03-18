from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SeoPointBox, Logo, NavLinks, Dropdown, NewHomeBanner, 
    Counter, OfferVideo, TourVideo, UmrahBanner, WhyBookUs
)

# ✅ Admin for WhyBookUs
@admin.register(WhyBookUs)
class WhyBookUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview_image', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('preview_image',)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="50" style="border-radius:5px;" />', obj.image.url)
        return "No Image"

    preview_image.short_description = "Image Preview"

# ✅ Admin for SeoPointBox
@admin.register(SeoPointBox)
class SeoPointBoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'icon_preview')
    search_fields = ('title',)
    ordering = ('id',)
    readonly_fields = ('icon_preview',)

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;" />', obj.icon.url)
        return "No Image"

    icon_preview.short_description = "Icon Preview"

# ✅ Admin for OfferVideo
@admin.register(OfferVideo)
class OfferVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'video_preview', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def video_preview(self, obj):
        if obj.video_file:
            return format_html('<video width="100" height="50" controls><source src="{}" type="video/mp4"></video>', obj.video_file.url)
        return "No Video"
    
    video_preview.short_description = "Video Preview"

# ✅ Admin for TourVideo
@admin.register(TourVideo)
class TourVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'video_preview', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def video_preview(self, obj):
        if obj.video_file:
            return format_html(
                '<video width="100" height="50" controls>'
                '<source src="{}" type="video/mp4"></video>',
                obj.video_file.url
            )
        return "No Video"

    video_preview.short_description = "Video Preview"

# ✅ Admin for Counter
@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'half')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('id',)

# ✅ Admin for Logo
@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="50" style="border-radius: 5px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Logo Preview"

# ✅ Admin for NewHomeBanner
@admin.register(NewHomeBanner)
class NewHomeBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_gif', 'created_at')
    readonly_fields = ('preview_gif',)

    def preview_gif(self, obj):
        if obj.gif_image:
            return format_html('<img src="{}" width="100" height="50" style="border-radius:5px;" />', obj.gif_image.url)
        return "No Image"

    preview_gif.short_description = "GIF Preview"

# ✅ Admin for UmrahBanner
@admin.register(UmrahBanner)
class UmrahBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_image', 'created_at')
    readonly_fields = ('preview_image',)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="50" style="border-radius:5px;" />', obj.image.url)
        return "No Image"

    preview_image.short_description = "Image Preview"

# ✅ Admin for NavLinks
@admin.register(NavLinks)
class NavLinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('id',)

# ✅ Admin for Dropdown
@admin.register(Dropdown)
class DropdownAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('id',)
