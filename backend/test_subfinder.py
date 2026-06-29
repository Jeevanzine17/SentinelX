from app.recon.subfinder import SubfinderRunner

subs = SubfinderRunner.run("hackerone.com")

print(f"Found {len(subs)} subdomains")

for sub in subs:
    print(sub)