# EdgeStream Hub — Quickstart

This guide gets you from a fresh **Debian 13 (Trixie)** VM to a running **EdgeStream Hub** in minutes.

>  **Supported base OS**
> 
> * Debian 13 “Trixie” (minimal install).

## 0) Provision a VM (VMware, Proxmox, or bare metal)

**Suggested VM sizing (starter):** 2 vCPU • 4–8 GB RAM • 40 GB disk • 1 vNIC (bridged)

Open **TCP 22** (SSH) and **TCP 443** (GUI) from your admin network.

### VMware vSphere

Create a VM and attach your Debian ISO (or use a Cloud-Init workflow if you have one).
Docs: https://docs.vmware.com/en/VMware-vSphere/index.html

### Proxmox VE

Create a VM and attach your Debian ISO (or use a Cloud-Init workflow if you have one).
Docs: https://pve.proxmox.com/pve-docs/ and https://pve.proxmox.com/pve-docs/cloud-init.html

### ISO Image

* Debian Trixie Installation Guide (official): https://www.debian.org/releases/trixie/installmanual
* Installer images / netinst: https://www.debian.org/CD/netinst/ and https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/
  
  >  **Tips**
  > * Enable **OpenSSH** during OS install.
  > * Set a **static IP** or DHCP reservation; note the VM’s IP.
  > * Proxmox:
  > * Use **virtio** (paravirtualized) disk/NIC types when available.

***

## 1) Install EdgeStream Hub

SSH to the server as a sudo-capable user, then run:

```bash
curl -sSf https://apt.repo.hyperi.io/edgestream_installer | sudo bash
```

This installs all required packages and configures the base system.

When it finishes, the **initial web admin credentials** are saved to:

```
/root/edgestream_credentials
```

***

## 2) Sign in to the GUI

Open a browser to:

```
https://<the server’s IP or DNS name>
```

Use the credentials from `/root/edgestream_credentials`.

> If your browser warns about the certificate, continue for now; you can replace it later in **System → Certificate Store**.

***

## 3) First things to do

1. **Change the default password** (Users → select your user → change password).
2. **Set the system hostname & timezone** (System → Settings).
3. **(Optional) Add a DNS server** (e.g., `1.1.1.1`).
4. **Add a Source** (Events → Sources) and verify in **Log Viewer**.
5. **Add a Destination** (Events → Destinations) and verify in **Log Viewer**.
6. **Back up config** (System → Configuration Backup).

***

## 4) Verify services (optional)

On the server:

```bash
# All EdgeStream services should be active:
systemctl --type=service --state=running | grep -E 'edgestream'
# Check reverse proxy (GUI):
sudo systemctl status edgestream-revproxy
```

***

## 5) Troubleshooting

* **GUI not reachable**
* Confirm the VM’s IP and that **TCP 443** is allowed in your hypervisor firewall / security group.
* On the VM: `sudo ss -tlnp | grep ':443'`.
* **Installer can’t fetch packages**
* Check DNS and outbound internet: `dig deb.debian.org` and `curl https://www.debian.org`.
* Retry the installer once network is fixed.
* **No credentials file** (`/root/edgestream_credentials`)
* Re-check the installer output; if missing, ensure secrets were created, then re-run the role/installer.

***

## What next?

* **Events → Filters**: create rules.
* **System → Updates**: schedule maintenance windows before applying updates.
* **System → VPN Client**: connect remote networks securely.