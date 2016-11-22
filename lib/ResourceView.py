from django import http
from django.utils.decorators import classonlymethod


class ResourceView:
	"""
	Simple Laravel-style RESTful resource controller/view base class.
	"""

	# 2d lookup table with pages and HTTP methods, returns name of handler method
	# a 'page' in this case is an unique URL pattern
	handler_method_names = {
		'index': {
			'get': 'index',
			'post': 'store'
		},
		'show': {
			'get': 'show',
			'put': 'update',
			'delete': 'destroy'
		},
		'create': {'get': 'create'},
		'edit': {'get': 'edit'}
	}

	def __init__(self, page, request):
		"""
		Constructor (called for every single request in the function generated by as_view)
		Store page variable in instance so that dispatch() can access it.
		"""
		self.page = page
		self.request = request

	@classonlymethod
	def as_view(cls, page):
		"""
		Define and return a function-based view depending on the page (provided as argument).
		"""
		def view(request, **kwargs):
			# Instantiate class
			self = cls(page, request)

			# Return Response generated by handler
			return self.dispatch(request, **kwargs)

		# Return ephemeral function-based view to URLconf
		return view

	def dispatch(self, request, **kwargs):
		"""
		Dispatch to the right class method by looking up the page and HTTP method in the lookup table.
		"""
		try:
			handler = getattr(self, self.handler_method_names[self.page][request.method.lower()])
		except KeyError:
			# If page/method doesn't exist, return 405 Method Not Allowed with the allowed methods for current page
			allowed_methods = self.handler_method_names[self.page]
			handler = http.HttpResponseNotAllowed(allowed_methods)

		return handler(request, **kwargs)

	# Handler methods, must be overridden in child class

	def index(self, request):
		raise NotImplementedError

	def store(self, request):
		raise NotImplementedError

	def show(self, request, pk):
		raise NotImplementedError

	def update(self, request, pk):
		raise NotImplementedError

	def destroy(self, request, pk):
		raise NotImplementedError

	def create(self, request):
		raise NotImplementedError

	def edit(self, request, pk):
		raise NotImplementedError
