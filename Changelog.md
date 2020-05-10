#OpenVPN Tools Changelog

1.1.1.3
  - Added a prerequisite check when querying server versions; If UpdateNotifier is not installed, it offers to install it.
  - Optimized the process of writing to the log file (backend change).
  - Corrected MessageBox text when trying to remove a MAC or manage 2FA without filling out the required fields.

1.1.1.2
  - Added "Query Server Version" check. Checks for available OpenVPN and Linux updates. Requires UpdateNotifier to be installed.
  - SSH connection fields are read only while connected.
  - Property fields are read only when not connected.
