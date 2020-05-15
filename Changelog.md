#OpenVPN Tools Changelog

1.1.1.5
  - Implemented dark mode. Controlled via a radio select in the preferences.
  - SSH port is stored in the server's log file and selecting the server from the hostname list will autofill the SSH port.

1.1.1.4
  - Added a preferences window which can be launched via the gear icon in the top right
  - Implemented an idle timeout which disconnects the active SSH session if no functions are used within the set limit
  - Added "SSH Idle Timeout" to the preferences to configure the time limit in minutes
  - Preferences are written to the registry in HKCU\SOFTWARE\OpenVPN Tools
  - Patch 1
    - Set the minimum timeout to 1
    - Create the registry key if it doesn't exist to prevent crashing on startup

1.1.1.3
  - Added a prerequisite check when querying server versions; If UpdateNotifier is not installed, it offers to install it.
  - Optimized the process of writing to the log file (backend change).
  - Corrected MessageBox text when trying to remove a MAC or manage 2FA without filling out the required fields.

1.1.1.2
  - Added "Query Server Version" check. Checks for available OpenVPN and Linux updates. Requires UpdateNotifier to be installed.
  - SSH connection fields are read only while connected.
  - Property fields are read only when not connected.
