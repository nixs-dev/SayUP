from django.shortcuts import redirect

class checkAuthenticated:
	def __init__(self, get_reponse=None):
		self.get_reponse = get_reponse

	def __call__(self, request):
		response = self.get_reponse(request)

		return response

	def process_view(self, request, func, args, kwargs):
		if request.path == '/':
			try:
				user = request.session['user']
			except:
				return redirect('auth/login')

		return None
