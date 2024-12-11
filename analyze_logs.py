import re

# Path to the collected log file and report file
log_file_path = "/var/log/weekly_auth.log"
report_file_path = "/var/log/weekly_report.txt"

# Threshold for failed login attempts
THRESHOLD = 10

# Dictionary to track failed login attempts by user
login_attempts = {}

# Regex to extract the user field correctly
user_regex = re.compile(r"user=([^\s]+)")

# Function to parse the log line and extract the user
def parse_log_line(line):
	match = user_regex.search(line)
	if match:
    	return match.group(1)
	return None

# Read the log file and count failed login attempts
with open(log_file_path, 'r') as log_file:
	for line in log_file:
    	user = parse_log_line(line)
    	if user:
        	# If the user is not already in the dictionary, initialize their count to 0
        	if user not in login_attempts:
            	login_attempts[user] = 0
        	# Increment the count for this user
        	login_attempts[user] += 1

# Write the report
with open(report_file_path, 'w') as report_file:
	report_file.write("Weekly Failed Login Analysis Report\n")
	report_file.write("===================================\n\n")
    
	flagged_accounts = 0
	for user, count in login_attempts.items():
    	if count >= THRESHOLD:
        	report_file.write(f"User '{user}' had {count} failed login attempts.\n")
        	flagged_accounts += 1
    
	if flagged_accounts == 0:
    	report_file.write("No suspicious failed login attempts detected.\n")

print(f"Report generated at {report_file_path}")
