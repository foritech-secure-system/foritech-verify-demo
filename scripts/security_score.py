import subprocess
import os

score = 100

# test check
try:
    subprocess.check_output(["pytest", "-q"])
    tests_status = "PASS"
except:
    tests_status = "FAIL"
    score -= 30

# fuzz check
fuzz_dir = "fuzz/out"

if os.path.exists(fuzz_dir):
    fuzz_status = "ACTIVE"
else:
    fuzz_status = "NONE"
    score -= 10

# crash check
crashes = 0
if os.path.exists("fuzz/out/default/crashes"):
    crashes = len(os.listdir("fuzz/out/default/crashes"))

if crashes > 0:
    score -= 40

print("Tests:", tests_status)
print("Fuzz:", fuzz_status)
print("Crashes:", crashes)
print("Security Score:", score)
