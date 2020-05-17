1.1.1.6
  - Implemented 90 day log retention. Upon connecting to SSH log retention runs automatically to purge any lines older than 90 days from     the text file.
  - If there's an error connecting the error is now displayed in the popup rather than just "Error Connecting"
  - If the connection fails as the server refused, the error message suggests checking the ssh port
  - If still connected when trying to close the program, it prompts to disconnect and cancels if No is selected.

1.1.1.5
  - Implemented dark mode. Controlled via a radio select in the preferences.
  - SSH port is stored in the server's log file and selecting the server from the hostname list will autofill the SSH port.
  - Patch 1
    - Hostname is added to the list when connecting to a server for the first time to fix the empty log file name bug.
    - After disconnect the SSH Hostname list is repopulated to get them in to alphabetical order with the newly added server.
    - Reading the SSH port from the log file is no longer case sensitive.

1.1.1.4
  - Added a preferences window which can be launched via the gear icon in the top right.
  - Implemented an idle timeout which disconnects the active SSH session if no functions are used within the set limit.
  - Added "SSH Idle Timeout" to the preferences to configure the time limit in minutes.
  - Preferences are written to the registry in HKCU\SOFTWARE\OpenVPN Tools.
  - Patch 1
    - Set the minimum timeout to 1 minute.
    - Create the registry key if it doesn't exist to prevent crashing on startup.

1.1.1.3
  - Added a prerequisite check when querying server versions; If UpdateNotifier is not installed, it offers to install it.
  - Optimized the process of writing to the log file (backend change).
  - Corrected MessageBox text when trying to remove a MAC or manage 2FA without filling out the required fields.

1.1.1.2
  - Added "Query Server Version" check. Checks for available OpenVPN and Linux updates. Requires UpdateNotifier to be installed.
  - SSH connection fields are read only while connected.
  - Property fields are read only when not connected.
