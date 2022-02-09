import json
import logging
from http import HTTPStatus
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import ListView
from news_feed.models import NewsData

# Create your views here.
logger = logging.getLogger("news_authenticity")


class HomePageView(View):

    def get(self, request):
        return HttpResponseRedirect("/news")


class NewsFeedListing(ListView):

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = NewsData.objects.filter(category__in=user.preferences.values_list("id", flat=True))
        else:
            queryset = NewsData.objects.all()
        return queryset

    template_name = "news_feed/news_list.html"
    model = NewsData
    paginate_by = 10
    context_object_name = 'news_list'
    ordering = '-positive_votes'


class ChangeVoteCount(LoginRequiredMixin, View):

    def put(self, request):
        try:
            data = json.loads(request.body)
            vote_type = str(data.get('voteType'))
            news_id = data.get('newsId')
            if vote_type and news_id:
                news_obj = NewsData.objects.filter(pk=news_id).first()
                if int(vote_type) == 0:
                    news_obj.negative_votes += 1
                elif int(vote_type) == 1:
                    news_obj.positive_votes += 1
                news_obj.save()
                resp = {'success': 'vote done.'}
                logger.info(
                    dict(
                        message="Vote done",
                        class_name="ChangeVoteCount",
                        method_name="post",
                    )
                )
            return JsonResponse(resp, status=HTTPStatus.OK)
        except Exception as e:
            logger.error(
                dict(
                    message="'Exception in change vote'",
                    class_name="ChangeVoteCount",
                    method_name="post",
                    errors=e,
                )
            )
            return JsonResponse({"message": "failed"}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
