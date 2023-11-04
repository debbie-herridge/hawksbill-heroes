handler404 = 'app_name.views.custom_404_view_name'

def page_not_found(request, exception):
    """
    Custom 404 error page
    """
    return render(request, '404.html', status=404)