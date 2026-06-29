import json
import subprocess


class SubfinderRunner:

    @staticmethod
    def run(domain: str):

        cmd = [
            "subfinder",
            "-d",
            domain,
            "-oJ",
            "-silent",
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
        )

        subdomains = []

        for line in result.stdout.splitlines():
            if line.strip():
                try:
                    data = json.loads(line)
                    subdomains.append(data["host"])
                except Exception:
                    pass

        return subdomains