import requests

target = "http://127.0.0.1:3000"

print("=" * 60)
print("   AUTOMATED WEB VULNERABILITY ASSESSMENT")
print("=" * 60)

try:
    response = requests.get(target, timeout=5)

    print("\nTarget:", target)
    print("Status Code:", response.status_code)

    # Security Header Check
    headers_to_check = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Strict-Transport-Security",
        "Referrer-Policy"
    ]

    print("\n--- Security Headers ---")

    for header in headers_to_check:
        if header in response.headers:
            print("[PASS]    ", header)
        else:
            print("[MISSING] ", header)

    # Basic Web Checks
    print("\n--- Basic Web Checks ---")

    if response.status_code == 200:
        print("[PASS] Website is responding")

    if "Server" in response.headers:
        print("[INFO] Server:", response.headers["Server"])

except requests.RequestException as e:
    print("[-] Error:", e)
