from django.http import HttpResponse


def custom_handler404(request, exception):
    return HttpResponse(
        '<h2><b>404</b><br> Sorry, this page not found!</h2>',
        status=404,
    )


def custom_handler500(request):
    return HttpResponse(
        '<h2><b>500</b><br> Sorry, server error!</h2>',
        status=500,
    )
