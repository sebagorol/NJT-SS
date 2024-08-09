# Network Data Collector

## Overview
The Network Data Collector is a comprehensive Python script designed to automate the process of collecting, analyzing, and backing up network device configurations. It interacts with network devices such as routers and switches to gather various data points including VRF IDs, ARP entries, MAC addresses, interface information, port statuses, and VLAN configurations. The collected data is then processed, merged, and exported into an Excel file with conditional formatting for easier analysis.

## Features

### 1. Network Device Backup
The script utilizes the `netmiko` library to connect to network devices and execute commands that retrieve configuration and operational data. It supports both routers and switches, handling different templates for parsing command outputs.

**Key Points:**
- Connects to devices using SSH.
- Supports different types of network devices (routers and switches).
- Configurable command execution for data retrieval.

### 2. Data Collection
The script collects various types of network data:
- **VRF IDs**: Collects VRF (Virtual Routing and Forwarding) information from routers.
- **ARP Entries**: Gathers ARP (Address Resolution Protocol) entries for IP to MAC address mapping.
- **MAC Addresses**: Retrieves MAC address tables from switches.
- **Interface Information**: Collects information about network interfaces.
- **Port Statuses**: Gathers status information of network ports.
- **VLAN Configurations**: Collects VLAN configuration details from network devices.

**Key Points:**
- Uses `textfsm` templates to parse and structure raw command outputs.
- Supports multiple templates for different data types.
- Stores collected data in structured formats for further processing.

### 3. Multithreading
The script implements concurrent execution using Python's `concurrent.futures.ThreadPoolExecutor` to enhance efficiency by connecting to multiple devices simultaneously.

**Key Points:**
- Utilizes multithreading to perform concurrent data collection.
- Configurable number of threads to optimize performance.
- Ensures efficient use of resources during data collection.

### 4. Data Merging and Processing
Collected data from different sources is merged to create a comprehensive view of the network status. This involves:
- Normalizing MAC addresses.
- Adding IP addresses from ARP tables.
- Incorporating port statuses and ping results.
- Sorting and filtering VLAN configurations.

**Key Points:**
- Processes and merges data from multiple sources.
- Ensures data consistency and accuracy.
- Provides a holistic view of the network.

### 5. Ping Test
The script performs ping tests on IP addresses collected from ARP entries to determine their reachability. This helps in identifying network connectivity issues.

**Key Points:**
- Pings IP addresses to check their availability.
- Records ping results (Good/Bad) for further analysis.
- Helps in diagnosing network issues.

### 6. Data Export
The final merged data is exported into an Excel file using the `pandas` and `openpyxl` libraries. The script creates multiple sheets within the Excel file to categorize the data.

**Key Points:**
- Exports data to an Excel file for easy analysis.
- Creates multiple sheets for different data types.
- Applies conditional formatting to highlight important information.

### 7. Conditional Formatting
The script applies conditional formatting to the Excel file to visually highlight the status of interfaces and ping results. This makes it easier to quickly identify issues.

**Key Points:**
- Uses `openpyxl` to apply colors based on conditions.
- Highlights interface statuses (Up/Down) and ping results (Good/Bad).
- Enhances readability and usability of the exported data.

### 8. Logging
The script configures logging to record details of its execution, including any errors encountered during the process. This helps in troubleshooting and auditing.

**Key Points:**
- Logs execution details to a file.
- Records errors and exceptions for debugging.
- Provides an audit trail of the script's operations.

### 9. Customization
The script uses environment variables for sensitive information such as credentials. Paths to device lists, templates, and output files are also configurable.

**Key Points:**
- Uses environment variables for security.
- Configurable file paths for device lists and templates.
- Easy to customize based on user requirements.

## Usage

### Prerequisites
- Python 3.6+
- Required Python libraries: `netmiko`, `textfsm`, `pandas`, `openpyxl`, `python-dotenv`

### Installation

1. Download the ZIP file and UNZIP in your chosen PATH.

2. Open the folder and Copy the PATH address. By right clicking the Folder as shown. 

![Screenshot 2024-08-08 160502](https://github.com/user-attachments/assets/b1b3dfd1-8bdd-4668-b5fb-b36059f5d971)

3. Open Windows PowerShell and use "cd" command and paste within apostrophes '' to get to your PATH where your folder is located.
    ```bash
      cd '.\OneDrive - New Jersey Transit\Desktop\NJT-Network-Scraper-SS\'
    ```
4. Write this command before activating the Virtual Enviorment.
   ```bash
      Set-ExecutionPolicy RemoteSigned -Scope Process
   ```
5. Activate the Scraper venv by using this command.
   ```bash
      .\Scraper\Scripts\Activate
   ```  
6. Install the required libraries:
   ```bash
      pip install -r requirements.txt
   ```
   or
   ```bash
      pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
   ```

   
   If doesn't work than can also manually install using this command.
   
   ```bash
      pip install  --trusted-host pypi.org --trusted-host files.pythonhosted.org
   ```

8. Save your Network Credentials in the Keyring using password_encrpyt.py.

   ```script
      notepad password_encrypt.py
   ```

   ```python
      keyring.set_password("network", "username", "YOUR_USERNAME")
      keyring.set_password("network", "password", "YOUR_PASSWORD")
      keyring.set_password("network", "enable_pass", "YOUR_PASSWORD")
   ```
9. Run the script so your Credentials are saved the keyring. 
   ```script
      python password_encrypt.py
   ```

10. Now we will convert the PATH with the correct format using the PATH_CONVERTER.py.
    In PowerShell use this Command to edit the IPs
   ```script
       notepad PATH_CONVERTER.py
   ```

11. Insert PATH from Earlier in the highlighed AREA shown in the picture.

![image](https://github.com/user-attachments/assets/46ce1481-256f-4f73-957d-5a7dc6347852)

12. Run the script using the command as shown and copy the Converted output as shown.
   
   ```script
       python PATH_CONVERTER.py
   ```
![image](https://github.com/user-attachments/assets/f3b69117-3258-4c70-b727-cfca38ce0717)

12. Open Network_Scraper.py in Notepad using PowerShell with the commands shown.
   ```script
       notepad Network_Scraper.py
   ```
13. Insert the Converted PATH to the highlighted area as shown in the Image.



14. as

15. 

16. Place your device IPs in Switch.txt and Router.txt by double clicking the text file in the Folder.

    In PowerShell use these commands to edit the IPs.
   ```script
      notepad Switch.txt
      notepad Router.txt
   ```

13.  Place your device IPs in Switch.txt and Router.txt.
   ```script
      notepad Switch.txt
      notepad Router.txt
   ```
 

### Running the Script

1. Change directory to folder PATH.
```bash
   cd '.\OneDrive - New Jersey Transit\Desktop\NJT-Network-Scraper-SS\'
```
2. Activate the virtual environment if not already activated:
```bash
   Set-ExecutionPolicy RemoteSigned -Scope Process
```
```bash
.\Scraper\Scripts\Activate
```
3. Add IPs to Switch.txt and Router.txt
```script
      notepad Switch.txt
      notepad Router.txt
```
4. Run the script:
```bash
   python Network_Scraper.py
```
4. Deactivating the Virtual Environment
Once you're done working, deactivate the virtual environment:
```bash
   deactivate
```
 ### Configuration
 
- Device lists are read from Router.txt and Switch.txt.                                                                        
- TextFSM templates are read from the templates/ directory.                                                                             
- Output is saved to an Excel file in the project directory.                                                                                                                  
