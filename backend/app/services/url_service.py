from sqlalchemy.orm import Session

from app.models.url import URL


class URLService:

    @staticmethod
    def create(
        db: Session,
        url: str,
        subdomain_id: int,
    ):

        existing = (
            db.query(URL)
            .filter(
                URL.url == url,
                URL.subdomain_id == subdomain_id,
            )
            .first()
        )

        if existing:
            return existing

        item = URL(
            url=url,
            path=url,
            subdomain_id=subdomain_id,
        )

        db.add(item)
        db.commit()
        db.refresh(item)

        return item