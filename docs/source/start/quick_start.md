# Quick start

The quick start section steps you through basic configuration of the Edgestream Hub including network settings, configuring sources and destinations.

---

## Step 1: Access the Management GUI
1. Open your browser and navigate to: https://< server-ip-or-hostname >

2. Accept the self-signed TLS certificate prompt (you can install custom certificates later under System → Certificate Store).

3. Log in using the admin credentials from /root/edgestream_credentials.

## Step 2: Initial Configuration Checklist
Complete these core onboarding tasks immediately after logging in:

1. Change Default Password: Navigate to Users, select your user account, and update the password.

2. System Identity: Open System → Settings and configure the system hostname and local timezone.

3. Upstream DNS: Set upstream resolvers (e.g., 1.1.1.1, 8.8.8.8) under System → Settings → Network.

4. Data Ingestion: Configure an input under Administration → Configuration → Sources and verify live receipt in the Log Viewer.

5. Egress Destination: Configure an output pipeline under Administration → Configuration → Destinations.

6. Configuration Backup: Export a snapshot of the base state via System → Backup.

## Verification & Health Checks
Verify that all daemon components and the reverse proxy are running:

### Check all active EdgeStream background services
systemctl --type=service --state=running | grep -E 'edgestream'

### Check reverse proxy status
sudo systemctl status edgestream-revproxy

## Troubleshooting

### GUI Not Reachable (Timeout / Refused)
- Confirm the host IP address and ensure TCP port 443 is permitted on external firewalls.
- Check if the local reverse proxy is listening:
  - sudo ss -tlnp | grep ':443'
- Check proxy logs:
  - sudo journalctl -u edgestream-revproxy -n 50 --no-pager

### Repository or Dependency Download Failures
- Verify outbound internet connectivity and DNS resolution:
  - dig deb.debian.org
  - curl -I https://deb.debian.org

Resolve network issues, then re-execute the installer script.

### Missing Credentials File (/root/edgestream_credentials)
- Ensure the installation script finished without exit errors.
- Review /var/log/edgestream-installer.log (if present) or re-run the installer.
