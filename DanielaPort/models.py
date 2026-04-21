from django.db import models


class user(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=100)
    Age = models.CharField(max_length=35)
    numero = models.CharField(max_length=100)

    def __str__(self):
        return self.nom + " " + self.prenom


TYPE_CHOICES = [
    ('MONTAGE VIDÉO', 'Montage Vidéo'),
    ('REEL', 'Reel'),
    ('COURT-MÉTRAGE', 'Court-Métrage'),
    ('AFTERMOVIE', 'Aftermovie'),
    ('TIKTOK', 'TikTok'),
    ('PLANNING ÉDITORIAL', 'Planning Éditorial'),
    ('COMMUNITY MANAGEMENT', 'Community Management'),
    ('BRANDING', 'Branding'),
    ('AUTRE', 'Autre'),
]


class Projet(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='MONTAGE VIDÉO')
    client = models.CharField(max_length=200, blank=True, default='')
    date = models.CharField(max_length=100, blank=True, default='')
    desc = models.TextField(blank=True, default='')
    media = models.FileField(upload_to='projets/', blank=True, null=True)
    media_type = models.CharField(max_length=10, blank=True, default='')  # 'image' or 'video'
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


PLATFORM_CHOICES = [
    ('ig', 'Instagram'),
    ('tk', 'TikTok'),
    ('yt', 'YouTube'),
    ('fb', 'Facebook'),
    ('tw', 'Twitter/X'),
    ('ot', 'Autre'),
]


class NetworkStat(models.Model):
    platform = models.CharField(max_length=5, choices=PLATFORM_CHOICES, unique=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.get_platform_display()} — {self.views} vues"
