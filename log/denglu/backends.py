from  .models import Myuser

class EmailBackend(object):
    def authenticate(self,request,**credentials):
        email = credentials.get('email',credentials.get('username'))
        try:
            user = Myuser.objects.get(email=email)
        except Myuser.DoesNotExist:
            pass
        else:
            if user.check_password(credentials["password"]):
                return user

    def get_user(self,user_id):
        try:
            return Myuser.objects.get(pk=user_id)
        except Myuser.DoesNotExist:
            return None