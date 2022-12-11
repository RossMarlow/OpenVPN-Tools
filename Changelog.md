1.1.9.0
  - Implemented host key caching to verify connections
    - The client will prompt to store the host key upon connecting to a server without a cached key
    - The user can select not to store the host key and the connection will continue as normal
    - If stored, future connections' host keys must match the cached key else the connection will be refused
  - Added WinSCP SFTP SSO
    - Host key cache is used to verify the SSO connection
  - Updated PuTTY SSO to use the cached host key
  - Add & Remove MAC/UUID merged into the same button with a user prompt upon click for Add or Remove
  - Capability added to delete a user from the OpenVPN Access Server
  - Fixed the bug where launched Notepad windows appear empty (Windows 11 issue)
  - Outputs previously forced to open in Notepad will now use the user's default text handler

1.1.8.0
  - Implented automatic MAC address formatting. If a MAC is entered with dashes rather than colons, and/or capital letters it's automatically re-formatted correctly
  - Fixed a bug where the password is displayed in the input box when using password authentication

1.1.7.0
  - Implemented 'friendly' display names. When connecting to an IP the user is prompted for a display name. The actual SSH address is stored in the log file with the SSH port.
  - 1.1.7.1
    - Fixed connecting to IP servers with friendly names
    - Patched PuTTy SSO to IP servers with friendly names

1.1.6.0
  - Implemented 90 day log retention. Retention runs automatically on connection to purge any lines older than 90 days from the log.
  - If there's an error connecting the error is now displayed in the popup rather than just "Error Connecting"
  - If the connection fails as the server refused, the error message suggests checking the ssh port
  - If still connected when trying to close the program, it prompts to disconnect and cancels if No is selected.
  - 1.1.6.1
    - Fixed the formatting/line breaks in the output console when querying server versions.
  - 1.1.6.2
    - Changed log entry "Warning" when deleting a MAC from a timestamped to indented line.
    - Bug Fix: Requesting whitelist for a non-existent user displayed values from the last valid user rather than prompting that the user doesn't exist.
  - 1.1.6.3
    - Added the '-a' switch to the command which retrieves the POST_AUTH log to ensure all records are retrieved.

1.1.5.0
  - Implemented dark mode. Controlled via a radio select in the preferences.
  - SSH port is stored in the server's log file and selecting the server from the hostname list will autofill the SSH port.
  - 1.1.5.1
    - Hostname is added to the list when connecting to a server for the first time to fix the empty log file name bug.
    - After disconnect the SSH Hostname list is repopulated to get them in to alphabetical order with the newly added server.
    - Reading the SSH port from the log file is no longer case sensitive.

1.1.4.0
  - Added a preferences window which can be launched via the gear icon in the top right.
  - Implemented an idle timeout which disconnects the active SSH session if no functions are used within the set limit.
  - Added "SSH Idle Timeout" to the preferences to configure the time limit in minutes.
  - Preferences are written to the registry in HKCU\SOFTWARE\OpenVPN Tools.
  - 1.1.4.1
    - Set the minimum timeout to 1 minute.
    - Create the registry key if it doesn't exist to prevent crashing on startup.

1.1.3.0
  - Added a prerequisite check when querying server versions; If UpdateNotifier is not installed, it offers to install it.
  - Optimized the process of writing to the log file (backend change).
  - Corrected MessageBox text when trying to remove a MAC or manage 2FA without filling out the required fields.

1.1.2.0
  - Added "Query Server Version" check. Checks for available OpenVPN and Linux updates. Requires UpdateNotifier to be installed.
  - SSH connection fields are read only while connected.
  - Property fields are read only when not connected.
