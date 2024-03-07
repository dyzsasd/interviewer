from django.http import JsonResponse

from .form import InterviewDocumentForm


def upload_documents(request):
    if request.method == 'POST':
        form = InterviewDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Files uploaded successfully!'}, status=201)
        else:
            return JsonResponse(form.errors, status=400)