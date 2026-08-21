Logging into the Edgestream Hub

Note: The installation process generates the initial administration tokens for the web interface and populates them in the file /root/edgestream_credentials. This contents of this file should be removed once the password details are stored in a password vault or similar.

To initially log into the Edgestream Hub, visit the IP address of the appliance with a web browser using https.

https://<edgestream-hub.local>

Log in using the initially provided credentials from /root/edgestream_credentials.

Navigate to the User management tab System -> Users and create a new admin user.

Log out of the Edgestream Hub and log in using the new user and credentials. Navigate to System -> Users and delete the default administration account admin@edgestream.local.

Additional administration accounts can be created either directly through this panel or admin users can register on the login page. Post registration a valid admin account can navigate to System -> Users and enable the additional accounts by editing the user and setting the enabled slider to true.