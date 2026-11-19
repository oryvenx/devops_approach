## Four Validation Rules
1. `APP_PORT` must be an integer between 1024 and 65535
2. `DEBUG` must alway be false
3. `DB_HOST` must always be present
4. `DB_PASSWORD` must always be present

## Defects Identified in `messy.env`
1. `APP_PORT` is not a valid integer.
2. `DEBUG` is not set to `false`.
3. `DB_PASSWORD` is empty.
4. `dbhost` and `DB_HOST` represent the same concept, the name should always be in uppercase and use snake case.