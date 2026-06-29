from sqlalchemy.orm import Session

from app.models.target import Target
from app.schemas.target import TargetCreate, TargetUpdate


class TargetService:

    @staticmethod
    def create(db: Session, target: TargetCreate):
        db_target = Target(**target.model_dump())
        db.add(db_target)
        db.commit()
        db.refresh(db_target)
        return db_target

    @staticmethod
    def get_all(db: Session):
        return db.query(Target).all()

    @staticmethod
    def get_by_id(db: Session, target_id: int):
        return (
            db.query(Target)
            .filter(Target.id == target_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        db_target: Target,
        target: TargetUpdate,
    ):
        db_target.domain = target.domain

        db.commit()
        db.refresh(db_target)

        return db_target

    @staticmethod
    def delete(
        db: Session,
        db_target: Target,
    ):
        db.delete(db_target)
        db.commit()