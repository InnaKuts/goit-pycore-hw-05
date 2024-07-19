import re

def parse_log_line(line: str) -> dict:
    """
    Parses a single line of the log file into a dictionary.
    """
    # Regular expression to parse the log line
    pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.*)'
    match = re.match(pattern, line)
    if match:
        date, time, level, message = match.groups()
        return {'date': date, 'time': time, 'level': level, 'message': message}
    return {}
