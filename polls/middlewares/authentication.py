from django.shortcuts import redirect

class checkAuthenticated:
    MUST_NOT = ['/auth/login/', '/auth/login/check/', '/auth/register/', '/auth/register/check/'] # must not be authenticated
    NOT_MATTER = ['/profiles/', '/api/'] # be authenticated or not doesnt matter
    
    def __init__(self, get_reponse=None):
        self.get_reponse = get_reponse

    def __call__(self, request):
        response = self.get_reponse(request)
        
        return response
    
    def check_url_match(self, url, list_):
        for i in list_:
            if url.startswith(i):
                return True
        return False
        
    def process_view(self, request, func, args, kwargs):
        url = request.path + '/' if not request.path.endswith('/') else request.path
        logged_in = 'user' in request.session.keys()
        
        if url != '/':
            if self.check_url_match(url, self.MUST_NOT):
                if logged_in:
                    return redirect('/home')
                else:
                    return None
            elif self.check_url_match(url, self.NOT_MATTER):
                return None
            else:
                if logged_in:
                    return None
                else:
                    return redirect('/auth/login')
                
        return None