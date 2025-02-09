from ninja import Router 
from .schemas import WaitListEntryListSchema
from typing import List
from .models import WaitListEntry

router = Router()

@router.get("", response=List[WaitListEntryListSchema])
def list_waitlist_entries(request):
    qs = WaitListEntry.objects.all()
    return qs