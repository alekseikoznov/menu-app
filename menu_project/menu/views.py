from django.views.generic import TemplateView


class MenuPageView(TemplateView):
    template_name = 'menu_app/menu_page.html'
