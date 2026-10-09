# Interface Settings

The Edgestream Hub is initially configured to use the underlying Debian installations network settings. To configure the interface settings navigate to System -> Settings and click the Interface tab.

The Edgetsream Hub supports either one or two interfaces/bonds. The event and management interfaces can be separated where required to support the situation where event and log collection occurs on a production network and management and/or sending to a destination is over a management network.

To configure a static address for Event collection select the Device from the device drop down and enter a valid IP Address, Netmask and optionally a gateway. The network settings will prioritise the MAC address of the device for configuration.

If a separate interface is used for the Management untick the 'use .…' box and select the Device from the device drop down for the management interface and enter a valid IP Address, Netmask and optionally a gateway.

Click apply to update the settings. If you have changed the IP Address of the Edgestream Hub you will need to reauthenticate on the new IP Address.