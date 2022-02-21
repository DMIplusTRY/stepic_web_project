def wsgi_application(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    body = str()
    for i in environ['QUERY_STRING'].split("&"):
    	body += str(i) +"\n"
    start_response(status, headers)
    return [body.encode()]
