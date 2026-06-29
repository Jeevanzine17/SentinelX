from app.recon.httpx_runner import HttpxRunner

result = HttpxRunner.run("api.hackerone.com")

print(result)