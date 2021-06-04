from typing import ClassVar, Dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from reversion.views import RevisionMixin
from typing import ClassVar
import reversion

from . import models
from . import forms

class HintObjectView:
	kwargs : ClassVar[Dict] = {}
	def get_object(self, queryset=None):
		if queryset is None:
			queryset = self.get_queryset() # type: ignore
		return queryset.get(problem__puid=self.kwargs['puid'],
				number=self.kwargs['number'])
class ProblemObjectView:
	kwargs : ClassVar[Dict] = {}
	def get_object(self, queryset=None):
		if queryset is None:
			queryset = self.get_queryset() # type: ignore
		return queryset.get(puid=self.kwargs['puid'])

class HintList(LoginRequiredMixin, ListView):
	context_object_name = "hint_list"
	def get_queryset(self):
		self.problem = models.Problem.objects.get(**self.kwargs)
		return models.Hint.objects.filter(problem=self.problem).order_by('number')
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['problem'] = self.problem
		return context

class HintDetail(HintObjectView, LoginRequiredMixin, DetailView):
	context_object_name = "hint"
	model = models.Hint

class HintUpdate(LoginRequiredMixin, RevisionMixin, UpdateView, HintObjectView):
	context_object_name = "hint"
	model = models.Hint
	form_class = forms.HintUpdateFormWithReason
	object : ClassVar[models.Hint] = models.Hint()
	def form_valid(self, form):
		reversion.set_comment(form.cleaned_data['reason'] or form.cleaned_data['content'])
		return super().form_valid(form)
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['problem'] = self.object.problem
		return context

class ProblemUpdate(LoginRequiredMixin, RevisionMixin, UpdateView, ProblemObjectView):
	context_object_name = "problem"
	model = models.Problem
	form_class = forms.ProblemUpdateFormWithReason
	object : ClassVar[models.Problem] = models.Problem()
	def get_success_url(self):
		return reverse_lazy("hint-list", args=(self.object.id,))
	def form_valid(self, form):
		reversion.set_comment(form.cleaned_data['reason'] or form.cleaned_data['description'])
		return super().form_valid(form)

class HintCreate(LoginRequiredMixin, RevisionMixin, CreateView):
	context_object_name = "hint"
	fields = ('problem', 'number', 'keywords', 'content',)
	model = models.Hint
	def get_initial(self):
		initial = super(HintCreate, self).get_initial()
		initial = initial.copy()
		initial['problem'] = models.Problem.objects.get(puid=self.kwargs['puid'])
		return initial

class ProblemCreate(LoginRequiredMixin, RevisionMixin, CreateView):
	context_object_name = "problem"
	fields = ('puid', 'source', 'description', 'aops_url',)
	model = models.Problem

class HintDelete(LoginRequiredMixin, RevisionMixin, DeleteView, HintObjectView):
	context_object_name = "hint"
	model = models.Hint
	object : ClassVar[models.Hint] = models.Hint()
	def get_success_url(self):
		return reverse_lazy("hint-list", args=(self.object.problem.id,))

class ProblemDelete(LoginRequiredMixin, RevisionMixin, DeleteView, ProblemObjectView):
	context_object_name = "problem"
	model = models.Problem
	object : ClassVar[models.Problem] = models.Problem()
	def get_success_url(self):
		return reverse_lazy("arch-index")

@login_required
def index(request):
	context = {'title' : 'ARCH'}
	return render(request, "arch/index.html", context)
