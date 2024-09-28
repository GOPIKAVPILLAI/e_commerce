from django.shortcuts import render
from .models import product
from django.http import JsonResponse
from .tasks import run_spider
from django.core.paginator import Paginator

# def start_scraping(request):
#     run_spider.delay()
#     return JsonResponse({'status': f'Scraping started!\n','note':'result in http://127.0.0.1:8080/results/'})
def start_scraping(request):
    return render(request, 'start_scraping.html')

def trigger_scraping(request):
    try:
        # Trigger the spider asynchronously with Celery
        run_spider.delay()
        return JsonResponse({'status': 'Scraping started successfully!'})
    except Exception as e:
        return JsonResponse({'status': 'Error', 'message': str(e)}, status=500)

def display(request):

    products=product.objects.all()
    paginator = Paginator(products, 5)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'results.html',{'page_obj':page_obj})