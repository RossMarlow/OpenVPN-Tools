# OpenVPN Tools

I originally built this software for my fellow technicians to use. As an MSP, we have a lot of OpenVPN servers to manage and whitelisting MAC addresses and completing basic functions was taking up a lot of their time via SSH consoles.

### Features
 - [x] Detailed log file for each VPN server
 - [x] SSH port autofilled for past VPN servers
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
 - [ ] Log file retention policy

Both password and private key (with or without encryption) SSH authentication are supported.

The software outputs (what I consider to be) a detailed log to a text file within a "Logs" folder inside the application directory. A text file is created for each SSH server; vpn.domain1.co.uk.txt, vpn.domain2.co.uk.txt etc. All the MACs which have been added, deleted and/or overwritten are noted in the logs, so if someone accidently replaces the wrong MAC, the original can be easily retrieved.

Light GUI | Dark Mode
:--------:|:--------:
![](/Wiki/OpenVPNToolsGUI_Light.PNG) | ![](/Wiki/OpenVPNToolsGUI_Dark.PNG)
