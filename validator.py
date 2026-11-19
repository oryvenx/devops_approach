"""Student scaffold. Implement rules from Lab 2; never print secret values."""
import sys

def validate(values):
    errors = []
    # TODO: APP_PORT must be an integer in 1024..65535.
    # TODO: DEBUG must be false, DB_HOST and DB_PASSWORD must be nonempty.
    # Return useful errors naming keys, not secret values.
    try:
        if not values.get("APP_PORT").strip():
            errors.append("APP_PORT must not be empty")
        elif not (1024 <= int(values.get("APP_PORT")) <= 65535):
            errors.append("APP_PORT must be an integer between 1024 and 65535.")
    except ValueError:
        errors.append("APP_PORT must be an integer")

    if values.get("DEBUG") != 'false':
        errors.append("DEBUG must be false")

    if not values.get("DB_HOST").strip():
        errors.append("DB_HOST must not be empty")

    if not values.get("DB_PASSWORD").strip():
        errors.append("DB_PASSWORD must not be empty")

    return errors

def load(path):
    values = {}
    for line in open(path, encoding="utf8"):
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()
    return values

if __name__ == "__main__":
    issues = validate(load(sys.argv[1]))
    print("\n".join(issues) if issues else "Configuration accepted")
    sys.exit(bool(issues))
