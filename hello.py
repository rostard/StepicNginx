def application (environ, start_response):
	status='200 OK'
	headers=[('Content-type','text/plain')]
	
	with open("log.txt","w") as onf:
		onf.write(environ['QUERY_STRING'])
		body=environ['QUERY_STRING'].split('&')
		onf.write(str(body))


	start_response(status,headers)
	return body
