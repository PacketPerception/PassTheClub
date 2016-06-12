from django.http import JsonResponse
from django.views.generic.edit import FormView

from juggling.notation import Siteswap
from .forms import SiteswapValidator


class IndexView(FormView):
    template_name = 'index.html'
    form_class = SiteswapValidator
    success_url = '/'

    def form_invalid(self, form):
        response = super(IndexView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        siteswap = Siteswap(form.cleaned_data['siteswap'])
        if self.request.is_ajax():
            return JsonResponse(siteswap.to_JSON(), safe=False)
        else:
            response = super(IndexView, self).form_valid(form)
            return response