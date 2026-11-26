API service for managing meals.

## Run locally

Python version: 3.12

Create the virtual environment:

    python3.12 -m venv .venv
    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Commands:

- `make run`: start the server on http://localhost:8000
- `make test`: run the tests
- `make lint`: check (and fix) the code style

## Database (PostgreSQL)

The API needs a PostgreSQL server running on your machine (no Docker yet).

### Install

Ubuntu / WSL:

```
sudo apt update && sudo apt install postgresql
```

macOS:

```
brew install postgresql@16
brew services start postgresql@16
```

Check it is running:

```
psql --version
sudo systemctl status postgresql     # WSL without systemd: sudo service postgresql start
```

### Create the user and the database

Open psql as the admin (Ubuntu/WSL: `sudo -u postgres psql`, macOS: `psql postgres`), then:

```sql
CREATE ROLE meals WITH LOGIN PASSWORD 'choose-a-password';
CREATE DATABASE protein_dev OWNER meals;
\q
```

Use letters and digits only in the password, to avoid encoding problems in the URL.

Check the connection:

```
psql "postgresql://meals:choose-a-password@localhost:5432/protein_dev" -c "SELECT now();"
```

### Configure the app

```
cp .env.example .env
```

Edit `.env` and replace `change-me` with your real password. `.env` is ignored by Git and must never be committed.

### Check

```
make run
```

You should see `Database: connected`. Then `curl -i http://localhost:8000/healthz` returns `200` with `{"status": "ok", "database": "ok"}`. If PostgreSQL is stopped it returns `503` with `{"status": "degraded", "database": "unreachable"}`.

### Troubleshooting

| Error | Cause |
|---|---|
| `password authentication failed` | The password in `.env` differs from the one set in PostgreSQL |
| `connection refused` | PostgreSQL is not running: `sudo systemctl start postgresql` |
| `KeyError: 'DATABASE_URL'` | `.env` is missing or not in the folder you run from |
| `ModuleNotFoundError: dotenv` | The venv is not active: `source .venv/bin/activate` |
