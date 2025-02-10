from django.shortcuts import get_object_or_404
from ninja import Router 
from .schemas import WaitListEntryListSchema, WaitListEntryDetailSchema
from typing import List
from .models import WaitListEntry

router = Router()

@router.get("", response=List[WaitListEntryListSchema])
def list_waitlist_entries(request):
    qs = WaitListEntry.objects.all()
    return qs


@router.get("{entry_id}", response=WaitListEntryDetailSchema)
def get_waitlist_entry(request, entry_id : int):
    obj = get_object_or_404(WaitListEntry, id = entry_id)
    return obj