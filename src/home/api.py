from ninja import NinjaAPI, Schema

api = NinjaAPI()

class UserSchema(Schema):
    username : str
    is_authenticated: bool
    email : str

@api.get("/hello")  
def hello(request):
    print(request)
    return "hello world"


@api.get("/me", response=UserSchema)
def me(request):
    return request.user
