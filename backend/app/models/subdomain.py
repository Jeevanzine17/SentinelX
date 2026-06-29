from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Subdomain(Base):
    __tablename__ = "subdomains"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    hostname: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    status_code: Mapped[int | None] = mapped_column(
    Integer,
    nullable=True,
)

    title: Mapped[str | None] = mapped_column(
    String(255),
    nullable=True,
)

    scheme: Mapped[str | None] = mapped_column(
    String(10),
    nullable=True,
)

    ip: Mapped[str | None] = mapped_column(
    String(50),
    nullable=True,
)

    webserver: Mapped[str | None] = mapped_column(
    String(100),
    nullable=True,
)

    technologies: Mapped[str | None] = mapped_column(
    Text,
    nullable=True,
)

    content_length: Mapped[int | None] = mapped_column(
    Integer,
    nullable=True,
)

    target_id: Mapped[int] = mapped_column(
        ForeignKey("targets.id", ondelete="CASCADE"),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    target = relationship(
        "Target",
        back_populates="subdomains",
    )
    urls = relationship(
    "URL",
    back_populates="subdomain",
    cascade="all, delete",
)