from django.shortcuts import get_object_or_404
from ninja import Router 
from ninja_jwt.authentication import JWTAuth
from .schemas import WaitListEntryListSchema, WaitListEntryDetailSchema,WaitListEntryCreateSchema
from typing import List
from .models import WaitListEntry

import helpers

router = Router()

def allow_annon(request):
    if not request.user.is_authenticated:
        return True

@router.get("", response=List[WaitListEntryListSchema],auth=helpers.api_auth_user_required)
def list_waitlist_entries(request):
    qs = WaitListEntry.objects.all()
    return qs

# api/waitlist/

@router.post("", response=WaitListEntryDetailSchema, auth=[helpers.helpers.api_auth_user_or_annon])
def create_waitlist_entry(request, data: WaitListEntryCreateSchema):
    obj = WaitListEntry(**data.dict())
    print(request.user)
    obj.save()
    return obj

@router.get("{entry_id}", response=WaitListEntryDetailSchema,auth=helpers.api_auth_user_required)
def get_waitlist_entry(request, entry_id : int):
    obj = get_object_or_404(WaitListEntry, id = entry_id)
    return obj