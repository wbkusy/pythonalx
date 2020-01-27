from django.http import HttpResponse


def funkcja_widoku(request):
    html = """<!doctype html>
    <html>
    <head></head>
    <body>
    Hello ALX!
    </body>
    </html>"""
    return HttpResponse(html)


def hello_name(request, name):
    html = f"""<!doctype html>
       <html>
       <head></head>
       <body>
       Hello {name}!
       </body>
       </html>"""
    return HttpResponse(html)

# Stwórz kalkulator

def operacje(request, op, a, b):
    pass