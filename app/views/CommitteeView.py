from lib.ResourceView import ResourceView, bind_model
from app.models import Committee
from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class CommitteeView(LoginRequiredMixin, ResourceView):
	models = [Committee]

	def index(self, request):
		# Get all committees for which the user is chairman
		committees = Committee.objects.filter(chairman=request.user)

		return render(request, 'app/committee_list.html', {'committees': committees})

	@bind_model
	def show(self, request, committee):
		return render(request, 'app/committee_detail.html', {'committee': committee})