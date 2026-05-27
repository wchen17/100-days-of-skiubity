import glob

changed = []
failed = []

for path in glob.glob("**/*.py", recursive=True):
    if path.endswith("_emdash_cleanup.py"):
        continue
    try:
        with open(path, encoding="utf-8") as f:
            c = f.read()
    except Exception as e:
        failed.append((path, str(e)))
        continue
    if "—" not in c:
        continue
    # Only touch the em dash. Spaced forms first, then any stragglers.
    new = (c.replace(" — ", ": ")
             .replace(" —", ":")
             .replace("— ", ": ")
             .replace("—", ":"))
    with open(path, "w", encoding="utf-8") as f:
        f.write(new)
    changed.append(path)

print("changed:", len(changed))
for p, e in failed:
    print("FAILED:", p, e)
