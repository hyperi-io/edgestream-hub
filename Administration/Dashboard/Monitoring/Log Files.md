# 📜 Log Files

The Log Files viewer provides an interactive console to inspect system, authentication, and service-level logs in real time directly from the EdgeStream Hub Web UI.

![Log Viewer](..\..\..\images\Logfiles.png "Log Viewer")

## 🧭 Viewer Controls

The interface streams log output over an authenticated WebSocket connection, offering real-time tailing and diagnostic navigation.

Controls include:

* **Log File Selection** — A searchable dropdown menu used to switch between monitored system and application log streams.

* **Auto Scroll** — When enabled, the console automatically follows new incoming log lines in real time. Disabling Auto Scroll allows administrators to freeze the view and inspect historical messages without interruption.

* **In-Console Search** — Integrated text search within the log console to quickly locate specific error signatures, IP addresses, or timestamps.

## 📁 Preconfigured Log Files

The Log Viewer comes preconfigured to monitor core system and application event logs:

* `/var/log/syslog` — General operating system and daemon activity logs.

* `/var/log/auth.log` — System authentication, user login attempts, and privilege escalations.

* `/var/log/edgestream-api/access.log` — EdgeStream Web UI and REST API HTTP request access logs.

* `/var/log/edgestream-api/error.log` — EdgeStream API service exceptions, tracebacks, and operational failures.

* `/var/log/edgestream-api/queue-runner.log` — Background task execution, asynchronous jobs, and maintenance worker activity.

## ⚙️ Custom Log Configuration

Administrators can monitor custom file paths (such as third-party services or dedicated collector logs) by navigating to:

> **Settings** → **Advanced Settings** → **Log Viewer Configuration**

Once added, custom log paths will immediately appear in the **Log file** selection dropdown.
