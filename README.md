# OpenVPN Tools

I originally built this software for my fellow technicians to use. As an MSP, we have a lot of OpenVPN servers to manage and whitelisting MAC addresses and completing basic functions was taking up a lot of their time via SSH consoles.

###OpenVPN Tools Features
 - View MAC whitelist
 - Add/Update a whitelisted MAC
 - Remove MAC from whitelist
 - Manage 2FA; View existing QR code or reset secret
 - Clear server lockouts
 - View POST_AUTH log
 - SSO into PuTTY session
 - Check for server updates
 
 
Both password and private key (with or without encryption) SSH authentication are supported.

The software also outputs (what I consider to be) a detailed log to a text file within a "Logs" folder inside the application directory. A text file is created for each SSH server; vpn.domain1.co.uk.txt, vpn.domain2.co.uk.txt etc.
