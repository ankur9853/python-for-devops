#Task 3 — Log Parser:

#Create a list of log lines like ["ERROR: disk full", "INFO: server ok", "ERROR: timeout"]
#Filter only ERROR logs into a new list
#Handle exception if the log list is empty


def parse_logs(log_list):
    # Requirement 3: Handle exception if the log list is empty
    if not log_list:
        raise ValueError("Log list is empty")

    # Requirement 2: Filter only ERROR logs into a new list
    error_logs = []
    for log in log_list:
        if log.startswith("ERROR"):
            error_logs.append(log)
    
    return error_logs

def main():
    # Requirement 1: Create a list of log lines
    loglist = ["ERROR: disk full", "INFO: server ok", "ERROR: timeout"]
    
    try:
        errors = parse_logs(loglist)
        print("Filtered Error Logs:", errors)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
