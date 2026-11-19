# Class 2 — Test Evidence

## Test 1: Valid Configuration (`valid.env.example`) — PASS
**Command:**
```bash
python3 validator.py valid.env
echo "Exit code: $?"
Configuration accepted
Exit code: 0
```

## Test 2: Broken Configuration (`messy.env`) — PASS
**Command:**
```bash
python3 validator.py messy.env
echo "Exit code: $?"
Invalid key convention for key dbhost
APP_PORT must be an integer
DEBUG must be false
DB_PASSWORD must not be empty
Exit code: 1
```