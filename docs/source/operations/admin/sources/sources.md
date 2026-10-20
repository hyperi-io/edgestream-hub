# 📥 Ingestion Sources

Sources define how data enters EdgeStream Hub. They either listen on local network ports to accept incoming logs, or connect out to external services, message queues, and cloud platforms to pull data in.

---

## Available Source Types

EdgeStream Hub supports multiple connectors designed for standard system, network, and cloud formats:

### Cloud & Messaging

* **Office 365 Audit (`o365audit`):** Connects to the Microsoft 365 Management Activity API to collect audit and security events from Microsoft 365, Entra ID (Azure AD), Exchange, SharePoint, and DLP.
* `Audit.General`: Microsoft Teams, Defender alerts, OneDrive actions, Sway, and Planner telemetry.
* `Audit.AzureActiveDirectory`: User logins, role assignments, directory modifications, and credential updates.
* `Audit.Exchange`: Mailbox activity, admin delegation changes, and mail policy events.
* `Audit.SharePoint`: Document library activities, file permissions, and site administration.
* `DLP.All`: Data Loss Prevention matches and policy incidents.


* **AWS SQS (`aws_sqs`):** Pulls messages directly from an Amazon Simple Queue Service standard or FIFO queue.
* **AWS S3 (`aws_s3`):** Downloads and processes log archives stored in an Amazon S3 bucket, triggered by SQS bucket notification messages.

### Network & Security Systems

* **Syslog (`syslog`):** Listens for standard RFC 3164 and RFC 5424 syslog messages over UDP, TCP, or encrypted TLS.
* **NetFlow (`netflow`):** Receives and parses Cisco NetFlow (v5, v7, v9) and IPFIX network traffic flows over UDP.
* **CEF (`cef`):** Ingests Common Event Format security logs produced by firewalls, security appliances, and SIEM forwarders.
* **Raw Socket (`socket`):** A general-purpose network listener for raw TCP, UDP, or Unix socket streams.

### Agents & Log Shippers

* **Logstash / Beats (`logstash`):** Accepts connections from Elastic Beats agents (Winlogbeat, Filebeat, Metricbeat) using the Lumberjack protocol.
* **Fluent (`fluent`):** Accepts log streams sent from Fluentd or Fluent Bit forwarders.
* **OpenTelemetry (`opentelemetry`):** Listens for standard OpenTelemetry log and trace data over HTTP or gRPC.
* **Vector (`vector`):** High-speed direct streaming between EdgeStream Hub nodes or upstream forwarders.
* **Splunk HEC (`splunk_hec`):** Receives events sent to the Splunk HTTP Event Collector format without needing to modify forwarder configurations.
* **HTTP Server (`http_server`):** Hosts a web endpoint to receive logs and webhooks sent as HTTP `POST` requests.
* **HTTP Client (`http_client`):** Regularly queries a remote website or REST API to fetch new data records.
* **File (`file`):** Reads and monitors log files directly from the local server filesystem (such as `/var/log/**/*.log`).
* **Windows Event Collector (`wec`):** *(Coming Soon)* Ingests events directly from domain-joined Windows machines using native Windows Event Forwarding.

### System & Health Metrics

* **Host Metrics (`host_metrics`):** Collects hardware and operating system metrics from the EdgeStream Hub server itself (CPU, memory, disk usage, and network traffic).
* **Internal Metrics (`internal_metrics`):** Tracks the real-time operational health, processing rates, and error counters of EdgeStream Hub.
* **PostgreSQL Metrics (`postgresql_metrics`):** Connects to a PostgreSQL database instance to monitor database health, active connections, and query statistics.

---

## Automatic Event Tagging

Whenever data enters through any source, EdgeStream automatically adds identification labels to each record:

| Label | Example Value | Description |
| --- | --- | --- |
| `@edgestream.event.name` | `core_firewall_syslog` | The friendly name assigned to the source instance. Used for routing and filtering rules. |
| `@edgestream.event.src_type` | `syslog` | The connector type handling the data. |
| `timestamp` | `2026-10-21T09:40:00.000Z` | The event timestamp from the message header, or the time EdgeStream received the log if missing. |

---

## How to Create a Source

1. In the left navigation, go to **Administration → Configuration → Sources**.
2. Click **Create** in the upper-right corner.
3. Configure the general properties:
* **Enabled:** Check this box so the source starts running as soon as you save it. (Leave unchecked if you want to set it up now and enable it later).
* **Name:** A unique identifier using letters, numbers, hyphens, or underscores (for example, `prod_firewall_syslog`).
```{warning}
**Source Names Are Permanent:** Once created, a source cannot be renamed because downstream filters and destinations refer directly to this name. If you need to rename a source, you must create a new one with the desired name and delete the old one.

```


* **Type:** Select the matching connector type from the dropdown.



### Completing the Settings Drawer

The settings drawer automatically updates based on the source type you choose:

* **Base Settings (Required):** The primary connection details—such as the listening port, server address, queue URL, or account credentials. If you enter a listening port, the system verifies that the port is free before saving.
* **TLS Settings (Optional / As Needed):** For encrypted streams, toggle TLS on and specify your certificate and key files.
* **Optional Settings:** Pre-configured defaults for line splitting, character sets, and connection limits. You can leave these at their default values unless your environment requires specific tuning.

4. Click **Create** to save and activate the source.

---

## Connecting Sources to Destinations

Creating a source only brings data into the appliance—it does not forward it automatically unless routed:

* **If a Default Destination Exists:** If your system has a default destination enabled under **Administration → Configuration → Destinations**, all new sources automatically send their data there.
* **To Route to a Specific Destination:**
1. Go to **Administration → Configuration → Destinations**.
2. Click **Edit** next to the target destination (such as an S3 bucket or ClickHouse database).
3. Under the **Inputs / Events and Metrics** list, select your new source.
4. Save the destination.



```{important}
If you do not have a default destination set and do not link your source to a specific destination, any events received by this source will be discarded immediately upon arrival (**blackholed**).

```

---

## Managing Existing Sources

* **Editing Settings:** Click **Edit** next to any listed source to update connection settings, renew certificates, or modify parsing options.
* **Pausing a Source:** Open the source edit menu, uncheck **Enabled**, and save. The source will stop listening or polling without deleting your configuration.
* **Deleting a Source:** Click **Delete** to remove the source and release any bound ports. Confirm that no active destinations or filters depend on this source before deleting it.