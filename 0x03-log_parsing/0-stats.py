#!/usr/bin/python3
import sys
import signal

# Initialize global variables
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))

def signal_handler(sig, frame):
    """Handles the signal for keyboard interruption (Ctrl + C)."""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin
try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 6:
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                total_file_size += file_size
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            except (ValueError, IndexError):
                continue

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

