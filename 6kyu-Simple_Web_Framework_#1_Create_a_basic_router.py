class Router(object):
    def __init__(self):
        self._routes = {}
        
    def bind(self, url, method, func):
        self._routes[(url, method)] = func
    
    def runRequest(self, url, method):
        return self._routes.get((url, method), lambda: "Error 404: Not Found")()
