from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Announcement

# Create your views here.
def news(request):
    announcements_list = Announcement.objects.all().order_by('-date', '-time')
    page = request.GET.get('page', 1)

    paginator = Paginator(announcements_list, 3)
    try:
        announcements = paginator.page(page)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {'announcements' : announcements})