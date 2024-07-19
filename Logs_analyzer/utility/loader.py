from typing import Callable, List, Dict
from .parser import parse_log_line

def load_logs(file_path: str) -> List[dict]:
    """
    Loads the logs from the specified file.
    """
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line)
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    return logs
