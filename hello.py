def application (env, start_response):
	status='200 OK'
	headers=[('Content-type','text/plain')]

    body=env['QUERY_STRING'].split('&')
	

	start_response(status,headers)
	return body
