from stocks.serializers import UserSerializer

def my_jwt_response_header(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request':request}).data
    }