from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .predict import detect_objects

def test_api(request):
    return JsonResponse({"message": "Interior AI POC working"})

def home(request):
    return JsonResponse({"message": "Interior AI Project Running"})

@csrf_exempt
def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):

        image = request.FILES["image"]

        path = "temp.jpg"

        with open(path, "wb+") as f:
            for chunk in image.chunks():
                f.write(chunk)

        result = detect_objects(path)

        return JsonResponse(result)

    return JsonResponse({"error": "Invalid request"})