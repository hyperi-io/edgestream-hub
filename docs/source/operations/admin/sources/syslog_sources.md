# 🪵 Syslog Sources

The **Syslog Sources** screen provides an easy way to configure network syslog listeners on EdgeStream Hub without needing to set up complex low-level pipelines.

```{note}
This page is for standard, unencrypted **UDP** and **TCP** syslog traffic. If your devices require **TLS encryption**, custom security certificates, or client verification, set them up using the main [Sources](sources) screen instead.

```

---

## Overview

A syslog listener opens a network port directly on the EdgeStream Hub appliance to accept incoming log messages from firewalls, network switches, routers, and servers across your local network.

### Automatic Event Tags

When an event arrives through a syslog listener, EdgeStream automatically adds standard identification tags to help identify and route the traffic:

| Field | Example Value | Description |
| --- | --- | --- |
| `@edgestream.event.name` | `edge_firewall_syslog` | The friendly name you gave the listener. |
| `@edgestream.event.src_type` | `syslog` | Identifies that the message came in via a syslog listener. |
| `host` | `192.168.1.1` | The IP address or hostname of the device that sent the message. |
| `timestamp` | `2026-10-21T09:46:00.000Z` | The timestamp parsed from the syslog message (or arrival time if missing). |

---

## Adding a Syslog Source

1. In the left navigation, go to **Administration → Configuration → Sources → Syslog** (or **Events → Syslog Sources**).
2. Click **Create** in the upper-right corner.
3. Configure the listener settings in the drawer:
* **Port:** Enter the network port number you want the appliance to listen on (common examples include `514` or `1514`).
```{warning}
The selected port must be free and not in use by other services on the server. The system checks port availability automatically when you save and will alert you if the port is already taken.

```


* **Name:** A descriptive name for this listener (e.g., `edge_firewall_syslog`). Letters, numbers, hyphens, and underscores are allowed.
* **Protocol:** Choose how messages will be sent to this port:
* **UDP:** Standard syslog transport. Recommended for high-volume network devices like firewalls and switches.
* **TCP:** Connection-oriented delivery. Recommended when you need guaranteed delivery without lost packets over busy links.
* **Both (TCP & UDP):** Listens on both protocols at the same time using the same port number.




4. Click **Create**. The listener will start immediately and begin accepting incoming syslog messages.

---

## Connecting Syslog to Destinations

Once created, syslog events need to be pointed to a destination so they are stored or forwarded:

* **Using a Default Destination:** If you have already configured an appliance-wide default destination (under **Administration → Configuration → Destinations**), all incoming syslog events will automatically route there.
* **Routing to a Specific Destination:**
1. Go to **Administration → Configuration → Destinations**.
2. Click **Edit** next to the destination where you want these logs sent (e.g., an S3 bucket or ClickHouse database).
3. Under the **Inputs / Sources** checklist, find your syslog listener's name and check its box.
4. Save the destination.



```{important}
If no default destination is active and the listener has not been assigned to a specific destination, all received syslog messages will be discarded immediately upon arrival (**blackholed**).

```

---

## Modifying an Existing Syslog Source

To adjust an active listener:

1. Locate the source in the table and click **Edit**.
2. Update the permitted fields:
* **Name:** Update the friendly name stamped into incoming events.
* **Protocol:** Switch between **UDP**, **TCP**, or **Both**.


3. Click **Update** to apply your changes.

```{note}
**Changing the Port:** The listening port number cannot be modified on an existing listener. If you need to move traffic to a different port, create a new listener on the target port, redirect your network devices, and then delete the old listener.

```

---

## Deleting a Syslog Source

1. Find the listener in the list and click **Delete**.
2. A confirmation prompt will appear. Double-check that no important dashboards, alerts, or destinations still rely on this listener.
3. Confirm the deletion. The appliance will immediately close the network port and remove the listener.