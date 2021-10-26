from django.db import models
"""
Here pre_save is taken because over save method is before the
default save method like super().save if our defined function
is after the super then we will use post save
"""
from django.db.models.signals import pre_save
from django.utils import timezone
from DJANGOFLIX.db.models import PublishStateOptions
from DJANGOFLIX.db.receivers import publish_state_pre_save, slugify_pre_save
from videos.models import Video
# custom model manager and custom query set for filtering our data
# and not to repeat much

class PlaylistQuerySet(models.QuerySet):
    def published(self):
        now  = timezone.now()
        return self.filter(
            state=PublishStateOptions.PUBLISH,
            published_timestamp__lte = now
            )

class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()    

class Playlist(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    order = models.IntegerField(default=1)
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video = models.ForeignKey(Video, null=True, blank=True,
     related_name='playlist_featured', on_delete=models.SET_NULL) # one video per playlist
    videos = models.ManyToManyField(Video, related_name='playlist_item', 
    blank=True, through="PlaylistItem")
    active =  models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=2, choices=PublishStateOptions.choices,
    default=PublishStateOptions.DRAFT)
    published_timestamp = models.DateTimeField(auto_now_add=False,auto_now=False,
    blank=True, null=True)

    objects = PlaylistManager()

    """def __str__(self):
        return self.title """

    @property
    def  is_published(self):
        return self.active

pre_save.connect(publish_state_pre_save, sender=Playlist)
pre_save.connect(slugify_pre_save, sender=Playlist)

class TVShowProxyManager(PlaylistManager):
    def all(self):
        return self.get_queryset().filter(parent__isnull=True)

class TVShowProxy(Playlist):

    objects = TVShowProxyManager()

    class Meta:
        verbose_name = 'TV Show'
        verbose_name_plural = 'TV Shows'
        proxy = True

class TVShowSeasonProxyManager(PlaylistManager):
    def all(self):
        return self.get_queryset().filter(parent__isnull=False)

class TVShowSeasonProxy(Playlist):

    objects = TVShowSeasonProxyManager()

    class Meta:
        verbose_name = 'Season'
        verbose_name_plural = 'Seasons'
        proxy = True

class PlaylistItem(models.Model):
    # shows they are not video but playlist queryset
    # CASCADE is to just just remove relationship bw video and playlist on deleting video or playlist
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    # means: qs = PlaylistItem.objects.filter(playlist=my_playlist_obj).order_by('order)
    order =  models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-timestamp']
