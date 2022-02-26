from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': "681730350?h=a247ca87c2"}
    return render(request, 'aperitivos/video.html', context={'video': video})