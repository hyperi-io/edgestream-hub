# 📦 Updates

The **Updates** page provides centralized package lifecycle management for EdgeStream Hub. It displays current package states, checks upstream configured repositories for new versions, and orchestrates on-demand package upgrades directly from the management interface.

---

## Overview

Navigate to **System → Updates** in the left-hand navigation to view the updates dashboard.

The interface polls upstream apt package repositories configured on the host system to identify:
* Currently installed packages and their versions.
* Upstream updates available for deployment.
* Repository origins and release channels.

---

## Repositories & Package Management

Under the **Repositories** tab, you can inspect available software packages and trigger updates.

### Checking for Updates

1. Open **System → Updates → Repositories**.
2. Review the list of installed EdgeStream services and system packages.
3. If an update is detected, select the target package to initiate an upgrade.

### Repository Configuration

EdgeStream Hub package sources are defined via upstream apt repositories. To customize, add, or alter the upstream repository endpoint (e.g., using an internal repository mirror or custom build channel):

1. Navigate to **System → Settings → Advanced Settings**.
2. Locate the **EdgeStream Hub Repository** configuration fields.
3. Update the repository URL or distribution release target and save changes.

---

## Operational Restrictions & Warnings

```{warning}
**Critical: `edgestream-api` Cannot Be Updated from the GUI**
```

The `edgestream-api` service provides the backend execution engine that powers the web interface and handles the update tasks themselves. Updating `edgestream-api` terminates the executing service mid-transaction, which breaks the running upgrade process and risks leaving package managers in an inconsistent state.

**Do not attempt to update `edgestream-api` via the web GUI.** It must be upgraded directly from the host command line over SSH.

## Upgrading edgestream-api via CLI
To update the core API daemon safely:

1. Connect to the EdgeStream Hub host via SSH:
```bash
ssh admin@<edgestream-host-ip>
```
2. Refresh repository metadata:
```bash
sudo apt-get update
```
3. Upgrade the API package directly:
```bash
sudo apt-get install --only-upgrade edgestream-api
```
4. Verify that the daemon restarted and is active:
```bash
sudo systemctl status edgestream-api
```

## Best Practices
- Scheduled Maintenance: Perform system package updates during designated maintenance windows, as underlying packet pipeline services (vector, netflow-collector) may briefly restart when upgraded.
- Configuration Snapshot: Before running major package upgrades, export a configuration backup via System → Backup.