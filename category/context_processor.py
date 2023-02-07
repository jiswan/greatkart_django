from .models import Category

def menu_link(reuquest):
    Links  = Category.objects.all()
    return dict(links=Links)


