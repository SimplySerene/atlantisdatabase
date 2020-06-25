from django.shortcuts import render
from django.views.generic import ListView, DetailView
import elective_search.models as models
from .review import user_review_form
from django.shortcuts import redirect

# View where one can search for electives
def search(request):
    all_electives = models.Elective.objects.all()
    return render(request, 'elective_search/search.html', {'all_electives': all_electives,
                                                           'languages': models.Elective.LANGUAGE_CHOICES,
                                                           'utblocks': models.Elective.UT_BLOCK_CHOICES,
                                                           'elective_types': models.Elective.ELECTIVE_TYPE_CHOICES,
                                                           })


# View of search results
class SearchResultsView(ListView):
    template_name = 'elective_search/search_results.html'

    def get_queryset(self):
        """Return all electives satisfying the search"""
        title = self.request.GET.get('title')
        ec = self.request.GET.get('ec')
        utblock = self.request.GET.get('utblock')
        language = self.request.GET.get('language')
        electivetype = self.request.GET.get('electivetype')
        osiriscode = self.request.GET.get('osiriscode')
        keywords = self.request.GET.get('keywords')
        result = models.search(title=title, ec=ec, utblock=utblock, language=language, electivetype=electivetype,
                               osiriscode=osiriscode, keywords=keywords)
        return result


# Detail view of an elective
class ElectiveDetailView(DetailView):
    model = models.Elective
    template_name = 'elective_search/detail.html'

def user_review_view(request):
    form = user_review_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/thanks!/')
    context = {
        'form': form 
    }
    return render(request, "elective_search/user_review.html", context)

def thank_you_view(request, *args, **kwargs):
    return render(request, "elective_search/thank_you.html", {})
 