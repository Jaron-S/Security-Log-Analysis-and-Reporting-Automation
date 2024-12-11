#!/bin/bash

# Variables
OUTPUT_FILE="/var/log/weekly_auth.log"

# Overwrite the weekly_auth.log file at the start
> "$OUTPUT_FILE"

# Get the date 7 days ago in seconds since epoch
SEVEN_DAYS_AGO=$(date -d "7 days ago" '+%s')

# Process all auth logs
for FILE in /var/log/auth.log*; do
	if [ -f "$FILE" ]; then
    	# Use zcat for compressed files, cat for regular files
    	if [[ "$FILE" == *.gz ]]; then
        	CMD="zcat"
    	else
        	CMD="cat"
    	fi

    	# Read and filter log entries
    	$CMD "$FILE" | awk -v cutoff="$SEVEN_DAYS_AGO" '
    	{
        	# Construct date string from log entry
        	date_str = $1 " " $2 " " $3 " " strftime("%Y")
        	# Convert date string to seconds since epoch
        	cmd = "date -d \"" date_str "\" +%s 2>/dev/null"
        	cmd | getline log_time
        	close(cmd)
        	# If log entry is within the past 7 days, append to weekly_auth.log
        	if (log_time >= cutoff) {
            	print $0 >> "'"$OUTPUT_FILE"'"
        	}
    	}'
	fi
done

# Run the log analysis script
python3 /usr/local/bin/analyze_logs.py
