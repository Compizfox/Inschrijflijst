from abc import ABCMeta

from django.utils.decorators import classonlymethod
from django.core.exceptions import PermissionDenied
from django import http


class BetterView(metaclass=ABCMeta):
	"""
	Better class based view base class.
	"""
	# 2d lookup table with routes and HTTP methods, returns name of handler method
	# a 'route' in this case is an unique URL pattern
	handler_method_names = {}

	def __init__(self, route, request):
		"""
		Constructor (called for every single request in the function generated by as_view)
		Store route variable in instance so that dispatch() can access it.
		"""
		self.route = route
		self.request = request

	@classonlymethod
	def as_view(cls, route):
		"""
		Define and return a function-based view depending on the route (provided as argument).
		"""
		def view(request, *args):
			# Instantiate class
			self = cls(route, request)

			# Return Response generated by handler
			return self.dispatch(request, *args)

		# Return ephemeral function-based view to URLconf
		return view

	def dispatch(self, request, *args):
		"""
		Dispatch to the right class method by looking up the route and HTTP method in the lookup table.
		"""
		method = request.method
		if '_method' in request.POST and request.POST['_method'].lower() in ['put', 'patch', 'delete']:
			method = request.POST['_method']

		try:
			handler = getattr(self, self.handler_method_names[self.route][method.lower()])
		except KeyError:
			# If route/method doesn't exist, return 405 Method Not Allowed with the allowed methods for current route
			allowed_methods = self.handler_method_names[self.route]
			return http.HttpResponseNotAllowed(allowed_methods)

		return handler(request, *args)

	def check_user(self, user):
		"""
		Compare the passed object to the current user and raise PermissionDenied if they are not equal.
		"""
		if user != self.request.user:
			raise PermissionDenied

	def check_admin_of(self, committee):
		"""
		Check if the current user is admin of the passed committee and raise PermissionDenied if not
		"""
		if not self.request.user.is_admin_of_committee(committee):
			raise PermissionDenied


class StaffRequiredMixin:
	"""
	Verify that the current user is staff.
	"""
	def dispatch(self, request, *args, **kwargs):
		if not request.user.is_staff:
			raise PermissionDenied

		return super().dispatch(request, *args, **kwargs)
