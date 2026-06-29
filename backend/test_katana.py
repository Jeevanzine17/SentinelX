from app.recon.katana_runner import KatanaRunner

urls = KatanaRunner.run("https://api.hackerone.com")

print(f"Found {len(urls)} URLs")

for url in urls[:20]:
    print(url)