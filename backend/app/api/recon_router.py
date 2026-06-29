from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.services.recon_service import ReconService

router = APIRouter(
    prefix="/recon",
    tags=["Recon"],
)


@router.post("/subfinder/{target_id}")
def run_subfinder(
    target_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    results = ReconService.run_subfinder(
        db,
        target_id,
    )

    if results is None:
        raise HTTPException(
            status_code=404,
            detail="Target not found",
        )

    return {
        "discovered": len(results),
        "subdomains": [
            s.hostname
            for s in results
        ],
    }


@router.post("/httpx/{target_id}")
def run_httpx(
    target_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    results = ReconService.run_httpx(
        db,
        target_id,
    )

    if results is None:
        raise HTTPException(
            status_code=404,
            detail="Target not found",
        )

    return {
        "updated": len(results),
        "hosts": [
            s.hostname
            for s in results
        ],
    }

@router.post("/katana/{target_id}")
def run_katana(
    target_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    results = ReconService.run_katana(
        db,
        target_id,
    )

    if results is None:
        raise HTTPException(
            status_code=404,
            detail="Target not found",
        )

    return {
        "saved_urls": len(results),
    }