import os
import argparse
import requests

# Placeholder URLs for login and reservation actions.
LOGIN_URL = "https://www.asiadcc.co.kr/login"  # TODO: replace with actual endpoint
RESERVE_URL = "https://www.asiadcc.co.kr/reserve"  # TODO: replace with actual endpoint


def login(user_id: str, password: str) -> requests.Session:
    """Authenticate and return a session."""
    session = requests.Session()
    resp = session.post(LOGIN_URL, data={"id": user_id, "pw": password})
    resp.raise_for_status()
    return session


def make_reservation(session: requests.Session, date: str, time_slot: str) -> str:
    """Send a reservation request and return response text."""
    resp = session.post(RESERVE_URL, data={"date": date, "time": time_slot})
    resp.raise_for_status()
    return resp.text


def main() -> None:
    parser = argparse.ArgumentParser(description="Reserve a tee time on Asiad CC")
    parser.add_argument("--date", required=True, help="Reservation date (YYYY-MM-DD)")
    parser.add_argument("--time", required=True, help="Time slot")
    parser.add_argument("--id", default=os.getenv("ASIAD_ID"), help="Login ID")
    parser.add_argument(
        "--password",
        default=os.getenv("ASIAD_PASSWORD"),
        help="Login password",
    )

    args = parser.parse_args()

    if not args.id or not args.password:
        parser.error("ID and password must be provided via options or env vars")

    session = login(args.id, args.password)
    result = make_reservation(session, args.date, args.time)
    print(result)


if __name__ == "__main__":
    main()
