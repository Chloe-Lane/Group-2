from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Tweet

# Create your views here.
def tweet_detail_view(request, pk=None):
    obj = Tweet.objects.get(pk=pk)
    print(obj)
    context = {
        'object': obj,
    }
    return render(request, 'tweets/detail_view.html', {})


def tweet_list_view(request):
    qs = Tweet.objects.all()
    print(qs)
    context = {
        'query': qs,
    }
    return render(request, 'tweets/list_view.html', {})




class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/list_view.html'




class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/detail_view.html'

    def get_object(self, queryset=Tweet.objects.all()):
        print(self.kwargs)
        pk=self.kwargs.get('pk')
        print(pk)
        return Tweet.object.get(id=pk)