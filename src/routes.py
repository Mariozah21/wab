from fastapi import APIRouter
router = APIRouter()

@router.get('/coffee-shop')
async def get_coffee_shops():
    return[]