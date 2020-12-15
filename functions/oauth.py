from flask_dance.contrib.github import make_github_blueprint, github
def init_google(client_id, client_secret, oauth):
	google = oauth.register(
	name='google',
	client_id = client_id,
	client_secret = client_secret,
	access_token_url = 'https://accounts.google.com/o/oauth2/token',
	access_token_params = None,
	authorize_url = 'https://accounts.google.com/o/oauth2/auth',
	authorize_params = None,
	api_base_url = 'https://www.googleapis.com/oauth2/v1/',
	userinfo_endpoint = 'https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
	client_kwargs = {'scope': 'openid email profile'},
	)
	return google
def init_github(client_id, client_secret):
	github_blueprint = make_github_blueprint(client_id=client_id, client_secret=client_secret)
	return github_blueprint