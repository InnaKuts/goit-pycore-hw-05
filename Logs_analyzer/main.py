import sys
from utility import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_log_file> [log_level]")
        return

    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        display_log_counts(count_logs_by_level(logs))
        print(f"\nDetails of logs for level '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

if __name__ == "__main__":
    main()