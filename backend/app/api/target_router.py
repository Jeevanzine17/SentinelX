from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.target import (
    TargetCreate,
    TargetResponse,
    TargetUpdate,
)
from app.services.project_service import ProjectService
from app.services.target_service import TargetService

router = APIRouter(
    prefix="/targets",
    tags=["Targets"],
)


@router.post(
    "/",
    response_model=TargetResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_target(
    target: TargetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project = ProjectService.get_project(
        db,
        target.project_id,
        current_user,
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return TargetService.create(
        db,
        target,
    )


@router.get(
    "/",
    response_model=list[TargetResponse],
)
def get_targets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return TargetService.get_all(db)


@router.get(
    "/{target_id}",
    response_model=TargetResponse,
)
def get_target(
    target_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    target = TargetService.get_by_id(
        db,
        target_id,
    )

    if not target:
        raise HTTPException(
            status_code=404,
            detail="Target not found",
        )

    return target


@router.put(
    "/{target_id}",
    response_model=TargetResponse,
)
def update_target(
    target_id: int,
    update: TargetUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    target = TargetService.get_by_id(
        db,
        target_id,
    )

    if not target:
        raise HTTPException(
            status_code=404,
            detail="Target not found",
        )

    return TargetService.update(
        db,
        target,
        update,
    )


@router.delete(
    "/{target_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_target(
    target_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    target = TargetService.get_by_id(
        db,
        target_id,
    )

    if not target:
        raise HTTPException(
            status_code=404,
            detail="Target not found",
        )

    TargetService.delete(
        db,
        target,
    )