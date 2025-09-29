import time
import os
import shutil
from datetime import timedelta

HOST_FILE_PATH = "/etc/hosts"
BACKUP_HOST_FILE_PATH = "/etc/hosts.backup"

REDIRECT_IP = ["127.0.0.1", "::1"]

BLOCKED_SITES = [
    "www.youtube.com",
    "youtube.com",
    "www.reddit.com",
    "reddit.com",
    "www.twitter.com",
    "twitter.com",
    "www.instagram.com",
    "instagram.com",
    "www.x.com",
    "x.com",
]


def block_sites():
    try:
        shutil.copy(HOST_FILE_PATH, BACKUP_HOST_FILE_PATH)
        print(f"Blocking {len(BLOCKED_SITES)} websites...")

        with open(HOST_FILE_PATH, "a") as file:
            file.write("\n# -- Start of focus block -- \n")
            for site in BLOCKED_SITES:
                for ip in REDIRECT_IP:
                    file.write(f"{ip} {site}\n")

        print("Sites blocked successfully.")
    except PermissionError:
        print(
            "Permission denied. Run the script with administrator privileges (e.g., 'sudo python main.py)."
        )
        exit()
    except Exception as e:
        print(f"Exception error on blocking sites: {e}")


def unblock_sites():
    if os.path.exists(BACKUP_HOST_FILE_PATH):
        print("Unblocking site...")
        try:
            shutil.move(BACKUP_HOST_FILE_PATH, HOST_FILE_PATH)
            print("Sites unblocked successfully.")
        except Exception as e:
            print(f"Error on unblocking sites: {e}")

    else:
        print("No backup file found. Unblocking step skipped.")


def runtime(duration_seconds):
    print(f"Starting time for {timedelta(seconds=duration_seconds)}.")
    end_time = time.time() + duration_seconds
    while time.time() < end_time:
        remaining_time = end_time - time.time()
        print(f"Running for {timedelta(seconds=int(remaining_time))}", end="\r")

        time.sleep(1)

    print("\nFocus finished!")


if __name__ == "__main__":
    focus_duration_minute = 1
    focus_duration_seconds = focus_duration_minute * 60

    try:
        block_sites()
        runtime(focus_duration_seconds)
    finally:
        unblock_sites()
