from sqlalchemy.orm import Session

from app.models.subdomain import Subdomain
from app.models.target import Target
from app.recon.httpx_runner import HttpxRunner
from app.recon.katana_runner import KatanaRunner
from app.recon.subfinder import SubfinderRunner
from app.services.url_service import URLService


class ReconService:

    @staticmethod
    def run_subfinder(
        db: Session,
        target_id: int,
    ):

        target = (
            db.query(Target)
            .filter(Target.id == target_id)
            .first()
        )

        if not target:
            return None

        subdomains = SubfinderRunner.run(target.domain)

        created = []

        for host in subdomains:

            exists = (
                db.query(Subdomain)
                .filter(
                    Subdomain.hostname == host,
                    Subdomain.target_id == target.id,
                )
                .first()
            )

            if exists:
                continue

            sub = Subdomain(
                hostname=host,
                target_id=target.id,
            )

            db.add(sub)
            created.append(sub)

        db.commit()

        return created

    @staticmethod
    def run_httpx(
        db: Session,
        target_id: int,
    ):

        target = (
            db.query(Target)
            .filter(Target.id == target_id)
            .first()
        )

        if not target:
            return None

        subdomains = (
            db.query(Subdomain)
            .filter(Subdomain.target_id == target.id)
            .all()
        )

        updated = []

        for subdomain in subdomains:

            result = HttpxRunner.run(subdomain.hostname)

            if not result:
                continue

            subdomain.status_code = result.get("status_code")
            subdomain.title = result.get("title")
            subdomain.scheme = result.get("scheme")
            subdomain.ip = result.get("host_ip")
            subdomain.webserver = result.get("webserver")

            tech = result.get("tech")
            if tech:
                subdomain.technologies = ",".join(tech)

            subdomain.content_length = result.get("content_length")

            updated.append(subdomain)

        db.commit()

        return updated

    @staticmethod
    def run_katana(
        db: Session,
        target_id: int,
    ):

        target = (
            db.query(Target)
            .filter(Target.id == target_id)
            .first()
        )

        if not target:
            return None

        saved = []

        for subdomain in target.subdomains:

            host = (
                f"{subdomain.scheme}://{subdomain.hostname}"
                if subdomain.scheme
                else f"https://{subdomain.hostname}"
            )

            urls = KatanaRunner.run(host)

            for url in urls:

                item = URLService.create(
                    db,
                    url,
                    subdomain.id,
                )

                saved.append(item)

        return saved