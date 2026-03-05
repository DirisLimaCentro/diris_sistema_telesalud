from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from .forms import VideoForm
from django.contrib.auth.decorators import login_required, user_passes_test
def es_admin(user):
    return user.is_staff

def video_list(request):
    query = request.GET.get('q')
    videos = Video.objects.all().order_by('-fecha_subida')

    if query:
        videos = videos.filter(titulo__icontains=query)

    return render(request, 'capacitaciones/video_list.html', {'videos': videos})


@login_required
@user_passes_test(es_admin)
def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()

    return render(request, 'capacitaciones/video_form.html', {'form': form})


@login_required
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'capacitaciones/video_detail.html', {'video': video})


@login_required
@user_passes_test(es_admin)
def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_detail', pk=video.pk)
    else:
        form = VideoForm(instance=video)

    return render(request, 'capacitaciones/video_form.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)

    if request.method == 'POST':
        video.delete()
        return redirect('video_list')

    return render(request, 'capacitaciones/video_confirm_delete.html', {'video': video})

