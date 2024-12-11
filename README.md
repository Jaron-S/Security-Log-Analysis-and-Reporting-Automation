## **Security Log Monitoring and Reporting Automation**

### **Overview**
This project automates the monitoring and analysis of security logs to detect unusual failed login attempts and generate detailed reports. The system improves incident detection and response through the use of Python, Bash scripting, and Cron scheduling. By streamlining the log analysis process, it enhances the organization’s security posture and compliance with government regulations.

### **Features**
- **Automated Log Collection**:
  - A Bash script gathers authentication logs from the past week, processing both compressed and uncompressed files.
  - Filters relevant entries to create a unified log file for analysis.
- **Log Analysis**:
  - A Python script scans collected logs, identifies unusual patterns (e.g., excessive failed login attempts), and generates concise reports.
  - Highlights potential security threats and anomalies using thresholds and regular expressions.
- **Scheduled Execution**:
  - Cron jobs ensure weekly automation of the log collection and analysis workflow.
- **Incident Reporting**:
  - Generates weekly reports summarizing flagged accounts and security concerns, ready for review by management.

### **Tools & Technologies**
- **Bash**: Collects and preprocesses log files.
- **Python**: Analyzes logs for suspicious activity and generates reports.
- **Cron**: Automates execution of the workflow on a weekly schedule.
- **Regular Expressions**: Extracts meaningful patterns from log data.

### **Installation & Setup**
#### **1. Clone the Repository**
```bash
git clone https://github.com/jaron-s/Security-Log-Analysis-and-Reporting-Automation.git
cd security-log-monitoring
```

#### **2. Configure the Environment**
- Install required Python libraries:
```bash
pip install -r requirements.txt
```
- Modify `log_config.json` to specify paths to log files and reporting directories.

#### **3. Make the Bash Script Executable**
- Set executable permissions for the Bash script:
```bash
chmod +x collect_logs.sh
```

#### **4. Schedule the Workflow**
- Add the Bash script to a Cron job for weekly execution:
```bash
crontab -e
```
Example Cron entry for Sunday at 23:59:
```bash
59 23 * * 0 /usr/local/bin/collect_logs.sh
```

### **Usage**
#### **Manual Execution for Testing**
Run the Bash script to collect logs:
```bash
./collect_logs.sh
```
Run the Python script for analysis:
```bash
python3 analyze_logs.py
```
#### **Review Reports**
- Check the `reports/` directory for the generated `weekly_report.txt`.
- Use the report to identify and address flagged accounts or potential threats.

### **Sample Output**
#### **1. Collected Logs**
File: `weekly_auth.log`
Contains authentication log entries from the past week.

#### **2. Analysis Report**
File: `weekly_report.txt`
Summarizes unusual activity, e.g.,
```
Weekly Failed Login Analysis Report
===================================

User 'john.doe' had 12 failed login attempts.
User 'admin' had 15 failed login attempts.
```

### **Future Enhancements**
- **Automated Email Alerts**:
  - Integrate email notifications for immediate escalation of flagged activity.
- **Centralized Log Management**:
  - Consolidate logs from multiple systems into a centralized repository for streamlined analysis.
- **Expanded Monitoring Scope**:
  - Include additional logs, such as web server access logs, to detect broader anomalies.
- **Real-Time Monitoring**:
  - Transition to continuous monitoring for faster threat detection using tools like Snort or OSSEC.

### **Conclusion**
This automated workflow significantly enhances the efficiency and effectiveness of log monitoring and reporting. Automating repetitive tasks and focusing on actionable insights, the scripts reduce manual effort and strengthen the organization’s security posture. The system’s design provides a strong foundation for future iterations and expanded capabilities.
