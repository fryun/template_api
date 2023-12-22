from fastapi import APIRouter

from app.delivery.sample_route.v1.some_controller import sample_router as bdd_v1_router

router = APIRouter()
router.include_router(bdd_v1_router, tags=["Sample Routing"])

__all__ = ["router"]
