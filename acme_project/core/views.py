from django.shortcuts import render



from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, 'core/404.html', status=404)

def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html', status=403)