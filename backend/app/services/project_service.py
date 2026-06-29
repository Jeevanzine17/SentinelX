from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectService:

    @staticmethod
    def create_project(
        db: Session,
        project: ProjectCreate,
        owner: User,
    ):
        db_project = Project(
            name=project.name,
            description=project.description,
            owner_id=owner.id,
        )

        db.add(db_project)
        db.commit()
        db.refresh(db_project)

        return db_project

    @staticmethod
    def get_projects(
        db: Session,
        owner: User,
    ):
        return (
            db.query(Project)
            .filter(Project.owner_id == owner.id)
            .all()
        )

    @staticmethod
    def get_project(
        db: Session,
        project_id: int,
        owner: User,
    ):
        return (
            db.query(Project)
            .filter(
                Project.id == project_id,
                Project.owner_id == owner.id,
            )
            .first()
        )

    @staticmethod
    def update_project(
        db: Session,
        project: Project,
        update: ProjectUpdate,
    ):
        if update.name is not None:
            project.name = update.name

        if update.description is not None:
            project.description = update.description

        db.commit()
        db.refresh(project)

        return project

    @staticmethod
    def delete_project(
        db: Session,
        project: Project,
    ):
        db.delete(project)
        db.commit()