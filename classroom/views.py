from django.shortcuts import render
from django.core.files.base import ContentFile
from django.views import View
from django.http import JsonResponse



# Create your views here.
def room(request):
    return render(request,"index.html")

from django.shortcuts import render
from django.http import JsonResponse

# Global variable to store the current progress
current_progress = 0

def index(request):
    return render(request, 'index.html')

# def upload_video(request):
#     if request.method == 'POST':
#         # Handle the uploaded video file
#         video_file = request.FILES.get('video')
#         # Perform slicing and concatenation logic
#         # ...
#         # Return the path or URL of the final video
#         final_video_path = '/path/to/final_video.mp4'
#         return JsonResponse({'video_path': final_video_path})
#     return JsonResponse({'error': 'Invalid request method'})

# def progress(request):
#     global current_progress
#     return JsonResponse({'progress': current_progress})
