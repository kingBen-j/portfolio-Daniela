import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Projet, NetworkStat


def home(request):
    return render(request, 'index.html')


# ═══════════════════════════════════
# API PROJETS
# ═══════════════════════════════════

def api_projets_list(request):
    """GET — Retourne tous les projets en JSON."""
    projets = Projet.objects.all()
    data = []
    for p in projets:
        data.append({
            'id': p.id,
            'title': p.title,
            'type': p.type,
            'client': p.client,
            'date': p.date,
            'desc': p.desc,
            'media': p.media.url if p.media else None,
            'mediaType': p.media_type,
            'createdAt': p.created_at.isoformat(),
        })
    return JsonResponse({'projets': data})


@csrf_exempt
@require_POST
def api_projets_add(request):
    """POST — Ajouter un projet (FormData avec fichier optionnel)."""
    title = request.POST.get('title', '').strip()
    if not title:
        return JsonResponse({'error': 'Le titre est obligatoire'}, status=400)

    projet = Projet(
        title=title,
        type=request.POST.get('type', 'MONTAGE VIDÉO'),
        client=request.POST.get('client', '').strip(),
        date=request.POST.get('date', '').strip(),
        desc=request.POST.get('desc', '').strip(),
    )

    # Fichier média
    if 'media' in request.FILES:
        f = request.FILES['media']
        projet.media = f
        if f.content_type.startswith('video'):
            projet.media_type = 'video'
        else:
            projet.media_type = 'image'

    projet.save()

    return JsonResponse({
        'success': True,
        'projet': {
            'id': projet.id,
            'title': projet.title,
            'type': projet.type,
            'client': projet.client,
            'date': projet.date,
            'desc': projet.desc,
            'media': projet.media.url if projet.media else None,
            'mediaType': projet.media_type,
            'createdAt': projet.created_at.isoformat(),
        }
    })


@csrf_exempt
@require_POST
def api_projets_delete(request, projet_id):
    """POST — Supprimer un projet par son ID."""
    projet = get_object_or_404(Projet, id=projet_id)
    # Supprimer le fichier média associé
    if projet.media:
        projet.media.delete(save=False)
    projet.delete()
    return JsonResponse({'success': True})


# ═══════════════════════════════════
# API STATS RÉSEAU
# ═══════════════════════════════════

def api_stats_get(request):
    """GET — Retourne toutes les stats réseau en JSON."""
    platforms = ['ig', 'tk', 'yt', 'fb', 'tw', 'ot']
    networks = {}
    for code in platforms:
        stat, _ = NetworkStat.objects.get_or_create(platform=code)
        networks[code] = stat.views
    return JsonResponse({'networks': networks})


@csrf_exempt
@require_POST
def api_stats_update(request):
    """POST — Mettre à jour les vues d'une plateforme. Body JSON: {platform, views}"""
    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON invalide'}, status=400)

    platform = body.get('platform', '')
    views = body.get('views', 0)

    valid_platforms = ['ig', 'tk', 'yt', 'fb', 'tw', 'ot']
    if platform not in valid_platforms:
        return JsonResponse({'error': 'Plateforme invalide'}, status=400)

    try:
        views = int(views)
        if views < 0:
            views = 0
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Valeur invalide'}, status=400)

    stat, _ = NetworkStat.objects.get_or_create(platform=platform)
    stat.views = views
    stat.save()

    return JsonResponse({'success': True, 'platform': platform, 'views': views})