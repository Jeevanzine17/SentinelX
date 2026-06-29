import json
import subprocess


class KatanaRunner:

    @staticmethod
    def run(host: str):

        cmd = [
            "katana",
            "-u",
            host,
            "-silent",
            "-jsonl",
            "-depth",
            "2",
            "-concurrency",
            "10",
            "-rate-limit",
            "25",
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
        )

        urls = []

        for line in result.stdout.splitlines():
            if not line.strip():
                continue

            try:
                data = json.loads(line)

                if "request" in data:
                    urls.append(data["request"]["endpoint"])
                elif "url" in data:
                    urls.append(data["url"])

            except Exception:
                pass

        return list(set(urls))