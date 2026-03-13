import json
import subprocess

result = subprocess.check_output(["python3", "scripts/security_score.py"]).decode()

tests = "PASS" if "PASS" in result else "FAIL"
score = result.split("Security Score:")[1].strip()

readme = f"""
![Tests](https://img.shields.io/badge/tests-{tests}-green)
![Security Score](https://img.shields.io/badge/security_score-{score}%25-blue)
"""

with open("BADGES.md", "w") as f:
    f.write(readme)
