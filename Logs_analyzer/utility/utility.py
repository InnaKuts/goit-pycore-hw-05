from typing import Callable, List, Dict
from itertools import groupby

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    """
    Filters the logs by the specified logging level.
    """
    return [log for log in logs if log['level'].lower() == level.lower()]

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    """
    Counts the number of log entries for each logging level.
    """
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    """
    Displays the log counts in a tabular format.
    """
    print("Logging Level | Count")
    print("---------------------")
    for level, count in counts.items():
        print(f"{level:<15} | {count}")