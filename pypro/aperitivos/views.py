from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao':{'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': "681730350?h=a247ca87c2"},
        'instalacao-windows':{'titulo': 'Instalação Windows', 'vimeo_id': 251497668}
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})