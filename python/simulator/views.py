from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .form import InterviewDocumentForm


@csrf_exempt
def upload_documents(request):
    if request.method == 'POST':
        form = InterviewDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Files uploaded successfully!'}, status=201)
        else:
            return JsonResponse(form.errors, status=400)
