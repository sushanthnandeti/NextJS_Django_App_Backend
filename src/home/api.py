from ninja import NinjaAPI, Schema
import helpers
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/waitlists/", "waitlists.api.router")



class UserSchema(Schema):
    username : str
    is_authenticated: bool
    email : str

@api.get("/hello")  
def hello(request):
    print(request)
    return {"message" : "hello world"}


@api.get("/me", response=UserSchema, auth=helpers.api_auth_user_required)
def me(request):
    return request.user
