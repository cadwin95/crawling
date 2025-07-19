# Asiad CC Reservation Helper

This folder contains a basic script for automating tee time reservations on the Asiad CC website. The logic is intentionally minimal and uses placeholder URLs because the actual endpoints may change.

## Setup

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Export your login credentials as environment variables or provide them through command-line options:

```
export ASIAD_ID=your_id
export ASIAD_PASSWORD=your_password
python reserver.py --date 2024-01-01 --time 07:00
```

You can also pass `--id` and `--password` directly. The script logs in and performs a POST request to the reservation endpoint. Because the actual Asiad CC reservation API is not public, you will need to adjust the `LOGIN_URL` and `RESERVE_URL` constants in `reserver.py` for your environment.
