from django.shortcuts import render

class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', '681730350?h=a247ca87c2'),
    Video('instalaco-windows', 'Instalação Windows', 251497668),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})