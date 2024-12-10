from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.http import Http404
from polling.models import Poll


# class ListView():
#     def as_view(self):
#         return self.get
#
#     def get(self, request):
#         model_list_name = self.model.__name__.lower() + '_list'
#         context = {model_list_name: self.model.objects.all()}
#         return render(request, self.template_name, context)


class PollListView(ListView):
    model = Poll
    template_name = 'polling/list.html'


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polling/detail.html'

    def post(self, request, *args, **kwargs):
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()
        context = {"object": poll}
        return render(request, "polling/detail.html", context)
