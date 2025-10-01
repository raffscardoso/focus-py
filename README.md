# Focus PY

A simple Python script to help you focus by blocking distracting websites.

## How it works

This script temporarily blocks a list of websites by adding entries to your `/etc/hosts` file. When the script is running, it will redirect the specified websites to your local machine (127.0.0.1), effectively blocking them. When the script is stopped (either by pressing any key or when the specified time is up), it restores your original `/etc/hosts` file.

## Requirements

- Python 3.x
- Administrator privileges (to modify the `/etc/hosts` file)

## Usage

1. Clone the repository:
```bash
git clone https://github.com/raffscardoso/focus-py.git
```

2. Navigate to the project directory:
```bash
cd focus-py
```

3. Run the script with administrator privileges:
```bash
sudo python main.py
```

4. Enter the amount of time you want to focus in minutes.

5. Press any key to stop the script at any time.

## Disclaimer

This script modifies your `/etc/hosts` file. It creates a backup of your original file before making any changes, and it should restore it automatically. However, it's always a good practice to be cautious when running scripts that modify system files.
