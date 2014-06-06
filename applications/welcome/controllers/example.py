def index():
	if not session.counter:
		session.counter = 1
	else:
		session.counter += 1

	return dict(message="Samuel App's", counter=session.counter)