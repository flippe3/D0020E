import development.NetworkHandler as nh
from OauthDev.OAuth import OAuth
#
han = nh.NetworkHandler()
han.setup_server(81, OAuth.OAuthServer)
