from rest_framework import authentication

class BearerAuthentication(authentication.TokenAuthentication):
    keyword = 'Bearer' # Замена стандартного Token на Bearer в заголовках авторизации по токену