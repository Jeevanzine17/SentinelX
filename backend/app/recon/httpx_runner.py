import json
import subprocess


class HttpxRunner:

    @staticmethod
    def run(host: str):

        cmd = [
            "httpx",
            "-silent",
            "-json",
            "-title",
            "-tech-detect",
            "-status-code",
            "-ip",
            "-web-server",
        ]

        result = subprocess.run(
            cmd,
            input=host,
            capture_output=True,
            text=True,
        )

        if not result.stdout.strip():
            return None

        try:
            return json.loads(result.stdout)

        except Exception:
            return None