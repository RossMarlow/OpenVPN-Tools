# OpenVPN Access Server MAC address checking post_auth script.
# Johan Draaisma
#
# This script can be used with LOCAL, PAM, LDAP, and RADIUS authentication.
# It adds an additional check when authentication is done through the VPN connection.
# It applies to all 3 connection profiles types (server-locked, user-locked, auto-login).
# Windows, Linux, and macOS will be reporting MAC addresses. However, Android and iOS
# devices will not, due to technical reasons. They will instead by reporting UUID. For
# simplicity and legacy reasons we will just call it MAC address from here on in, but
# it can be in theory any unique hardware-based string that the client reports to us.
#
# Please note: RADIUS/LDAP case insensitivity may lead to the system recognizing
# Billy.Bob and billy.bob as 2 separate accounts, when using RADIUS/LDAP.
#
#
# Full documentation and explanation can be found here:
# https://openvpn.net/vpn-server-resources/access-server-post-auth-script-host-checking/
#
# Script last updated in January 2020


import re

from pyovpn.plugin import *

# Optionally set this string to a known public IP address (such as the
# public IP address of machines connecting from a trusted location, such
# as the corporate LAN). If set, all users must do the first login from this
# IP address, so the machine's hardware (MAC/UUID) address can be recorded.
#
# If this is empty, which it is by default, then registrations for the first
# MAC address for a user account will be done automatically on first login.
#
# If this is set to "NONE" or "DISABLED" then the server administrator must
# always manually register each MAC/UUID address by hand on the command line.
# For that, we refer you to our documentation.
first_login_ip_addr = ""

# If False or undefined, AS will call us asynchronously in a worker thread.
# If True, AS will call us synchronously (server will block during call),
# however we can assume asynchronous behavior by returning a Twisted
# Deferred object.
SYNCHRONOUS=False

# this function is called by the Access Server after normal VPN or web authentication
def post_auth(authcred, attributes, authret, info):
    #print("********** POST_AUTH %s %s %s %s" % (authcred, attributes, authret, info))

    # get user's property list, or create it if absent
    proplist = authret.setdefault('proplist', {})

    # user properties to save - we will use this to pass the hw_addr_save property to be
    # saved in the user property database.
    proplist_save = {}

    error = ""

    # If a VPN client authentication attempt is made, do these steps:
    # Check if there is a known MAC address for this client
    # If not, register it
    # If yes, check it
    #
    # An additional optional requirement is that first time registration must occur
    # from a specific IP address, as specified in the first_login_ip_addr set above
    #
    # The 'error' text goes to the VPN client and is shown to the user.
    # The 'print' lines go to the log file at /var/log/openvpnas.log (by default).

    if attributes.get('vpn_auth'):                  # only do this for VPN authentication
        hw_addr = authcred.get('client_hw_addr')    # MAC address reported by the VPN client
        username = authcred.get('username')         # User name of the VPN client login attempt
        clientip = authcred.get('client_ip_addr')   # IP address of VPN client login attempt

        if hw_addr:				    # If a MAC/UUID was received from the connecting client
            whitelistedAddresses = []
            hw_addr_save = proplist.get('pvt_hw_addr')
            hw_addr_save2 = proplist.get('pvt_hw_addr2')
            hw_addr_save3 = proplist.get('pvt_hw_addr3')
            hw_addr_save4 = proplist.get('pvt_hw_addr4')
            hw_addr_save5 = proplist.get('pvt_hw_addr5')
            hw_addr_save6 = proplist.get('pvt_hw_addr6')
            hw_addr_save7 = proplist.get('pvt_hw_addr7')
            hw_addr_save8 = proplist.get('pvt_hw_addr8')
            hw_addr_save9 = proplist.get('pvt_hw_addr9')
            hw_addr_save10 = proplist.get('pvt_hw_addr10')
            if hw_addr_save:
                whitelistedAddresses.append(hw_addr_save)
            if hw_addr_save2:
                whitelistedAddresses.append(hw_addr_save2)
            if hw_addr_save3:
                whitelistedAddresses.append(hw_addr_save3)
            if hw_addr_save4:
                whitelistedAddresses.append(hw_addr_save4)
            if hw_addr_save5:
                whitelistedAddresses.append(hw_addr_save5)
            if hw_addr_save6:
                whitelistedAddresses.append(hw_addr_save6)
            if hw_addr_save7:
                whitelistedAddresses.append(hw_addr_save7)
            if hw_addr_save8:
                whitelistedAddresses.append(hw_addr_save8)
            if hw_addr_save9:
                whitelistedAddresses.append(hw_addr_save9)
            if hw_addr_save10:
                whitelistedAddresses.append(hw_addr_save10)

            if hw_addr_save:
                if hw_addr not in whitelistedAddresses:
                    error = "The hardware MAC/UUID address reported by this VPN client does not match any of the registered addresses."
                    print("***** POST_AUTH MAC CHECK: account user name         : %s" % username)
                    print("***** POST_AUTH MAC CHECK: client IP address         : %s" % clientip)
                    print("***** POST_AUTH MAC CHECK: client MAC/UUID address   : %s" % hw_addr)
                    print("***** POST_AUTH MAC CHECK: expected MAC/UUIDs : %s" % whitelistedAddresses)
                    print("***** POST_AUTH MAC CHECK: connection attempt        : FAILED")
                else:
                    print("***** POST_AUTH MAC CHECK: account user name         : %s" % username)
                    print("***** POST_AUTH MAC CHECK: client IP address         : %s" % clientip)
                    print("***** POST_AUTH MAC CHECK: client MAC/UUID address   : %s" % hw_addr)
                    print("***** POST_AUTH MAC CHECK: expected MAC/UUIDs : %s" % whitelistedAddresses)
                    print("***** POST_AUTH MAC CHECK: connection attempt        : SUCCESS")

            else:
                # First login by this user, save MAC addr.
                if not first_login_ip_addr or first_login_ip_addr == clientip:
                    proplist_save['pvt_hw_addr'] = hw_addr
                    print("***** POST_AUTH MAC CHECK: account user name         : %s" % username)
                    print("***** POST_AUTH MAC CHECK: client IP address         : %s" % clientip)
                    print("***** POST_AUTH MAC CHECK: client MAC/UUID address   : %s" % hw_addr)
                    print("***** POST_AUTH MAC CHECK: action taken              : MAC address learned and locked.")
                    print("***** POST_AUTH MAC CHECK: connection attempt        : SUCCESS")
                else:
                    error = "Your attempt to login from an address not approved for MAC/UUID address registration has been denied."
                    print("***** POST_AUTH MAC CHECK: account user name         : %s" % username)
                    print("***** POST_AUTH MAC CHECK: client IP address         : %s" % clientip)
                    print("***** POST_AUTH MAC CHECK: action taken              : attempt to register client MAC/UUID address from restricted address denied.")
                    print("***** POST_AUTH MAC CHECK: connection attempt        : FAILED")

        else:
            error = "VPN client is not reporting a MAC/UUID address. Please verify that a suitable OpenVPN client is being used."
            print("***** POST_AUTH MAC CHECK: account user name         : %s" % username)
            print("***** POST_AUTH MAC CHECK: client IP address         : %s" % clientip)
            print("***** POST_AUTH MAC CHECK: client MAC/UUID address   : NONE REPORTED")
            print("***** POST_AUTH MAC CHECK: action taken              : VPN connection denied with a suitable error message.")
            print("***** POST_AUTH MAC CHECK: connection attempt        : FAILED")

    # process error, if one occurred
    if error:
        authret['status'] = FAIL
        authret['reason'] = error          # this error string is written to the server log file
        authret['client_reason'] = error   # this error string is reported to the client user

    return authret, proplist_save
