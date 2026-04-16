import json
import redis
from django.http import JsonResponse
from .models import Prompt

r = redis.Redis(host='redis', port=6379, db=0)

def get_prompts(request):
    prompts = list(Prompt.objects.values())
    return JsonResponse(prompts, safe=False)

def create_prompt(request):
    if request.method == "POST":
        data = json.loads(request.body)

        if len(data.get("title", "")) < 3:
            return JsonResponse({"error": "Title too short"}, status=400)

        prompt = Prompt.objects.create(
            title=data["title"],
            content=data["content"],
            complexity=data["complexity"]
        )
        return JsonResponse({"id": prompt.id})

def get_prompt_detail(request, id):
    try:
        prompt = Prompt.objects.get(id=id)

        # Redis view count
        key = f"prompt:{id}:views"
        views = r.incr(key)

        data = {
            "id": prompt.id,
            "title": prompt.title,
            "content": prompt.content,
            "complexity": prompt.complexity,
            "view_count": views
        }
        return JsonResponse(data)

    except Prompt.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
