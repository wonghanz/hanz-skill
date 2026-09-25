import sys
import os

# Ensure CapriGuard nodigo is on path
ROOT_DIR = r"c:\Users\iplan\Downloads\CapriGuard"
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from nodigo.security.aegis_guard import AegisGuard

def inspect(text: str):
    guard = AegisGuard()
    in_check = guard.inspect_input(text)
    out_check = guard.inspect_and_harden_output(text)
    print("=== Aegis-Guard Audit Report ===")
    print("Input Safe:", in_check["is_safe"])
    if not in_check["is_safe"]:
        print("Threats Detected:", in_check["threats"])
    print("DLP Blocked (Secrets Found):", out_check["blocked"])
    if out_check["blocked"]:
        print("Leaks Detected:", out_check["leaks_detected"])
    if out_check["mvp_flaws"]:
        print("Anti-MVP Flaws:", out_check["mvp_flaws"])
    return in_check["is_safe"] and not out_check["blocked"]

if __name__ == "__main__":
    content = sys.argv[1] if len(sys.argv) > 1 else ""
    inspect(content)
