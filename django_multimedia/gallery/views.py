from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MediaItem
from .forms import MediaUploadForm

def media_list(request):
    media_items = MediaItem.objects.all()
    filter_type = request.GET.get('type')
    
    if filter_type in ['image', 'video']:
        media_items = media_items.filter(media_type=filter_type)

    return render(request, 'gallery/media_list.html', {'media_items': media_items, 'selected_type': filter_type})

def media_detail(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)
    return render(request, 'gallery/media_detail.html', {'item': item})

@login_required
def upload_media(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.uploaded_by = request.user
            media.save()
            return redirect('media_list')
    else:
        form = MediaUploadForm()
    return render(request, 'gallery/upload.html', {'form': form})
