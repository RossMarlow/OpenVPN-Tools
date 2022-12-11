# OpenVPN Tools

I have a lot of OpenVPN servers to manage and whitelisting MAC addresses and completing basic functions was taking up a lot of time via SSH consoles.

### Features
 - [x] Password and Private Key authentication support
 - [x] SSH port autofilled for past VPN servers
 - [x] Detailed log file for each VPN server
 - [x] View MAC whitelist: Single user or all accounts
 - [x] Add MAC to whitelist (& overwrite)
 - [x] Remove MAC from whitelist
 - [x] Manage 2FA: View existing QR code or reset secret
 - [x] Clear server lockouts
 - [x] View POST_AUTH log
 - [x] SSO into PuTTY session
 - [x] Check for server updates
 - [x] Customizable idle disconnect
 - [x] GUI dark mode
 - [x] Automated log retention (90 days)
 - [x] Server Display Names
 - [x] Delete User (Remove All Properties)
 - [x] SSO into WinSCP SFTP session
 - [x] Auto-select private key file
 - [x] Remember Host Keys for connection validation

The software outputs (what I consider to be) a detailed log to a text file within a "Logs" folder inside the application directory. A text file is created for each SSH server; vpn.domain1.co.uk.txt, vpn.domain2.co.uk.txt etc. All the MACs which have been added, deleted and/or overwritten are noted in the logs, so if someone accidently replaces the wrong MAC, the original can be easily retrieved.

Light GUI | Dark Mode
:--------:|:--------:
![](/Wiki/OpenVPNToolsGUI_Light.PNG) | ![](/Wiki/OpenVPNToolsGUI_Dark.PNG)
