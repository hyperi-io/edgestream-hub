# Install EdgeStream Hub on Debian Linux

This guide walks through configuring a fresh **Debian 13 (Trixie)** VM and completing a standard installation of **EdgeStream Hub**.

```{note}
**Supported Base OS:** Debian 13 "Trixie" (minimal server install).
```

---

## Prerequisites & Sizing

### Recommended VM Sizing (Starter)

| Resource | Specification | Notes |
| :--- | :--- | :--- |
| **CPU** | 2 vCPU | Minimum baseline |
| **RAM** | 4–8 GB | 8 GB recommended if buffering locally |
| **Disk** | 40 GB | Thin-provisioned |
| **Network** | 1 vNIC (Bridged) | Static IP or DHCP reservation recommended |

### Firewall Requirements

Ensure the following inbound ports are open from your management network:

* **TCP 22**: SSH administration
* **TCP 443**: Web GUI access

---

## Step 1: Provision the VM

Deploy a clean installation using the official [Debian Trixie Netinst ISO](https://www.debian.org/CD/netinst/).

### Hypervisor Recommendations

* **VMware vSphere:** Create a VM (Debian 64-bit), attach the ISO, and assign bridged networking. Review the [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html) for specific cluster requirements.
* **Proxmox VE:** Create a VM using **VirtIO SCSI** disk controller and **VirtIO (paravirtualized)** network adapter. For automated deployments, refer to [Proxmox Cloud-Init Documentation](https://pve.proxmox.com/pve-docs/cloud-init.html).

### OS Installation Checklist

* Select **minimal install** (disable desktop environments).
* Check **OpenSSH server** and standard system utilities during package selection.
* Configure a static IPv4/IPv6 address or assign a static DHCP lease. Note the allocated IP address.

---

## Step 2: Run the EdgeStream Hub Installer

1. SSH into the server as a user with `sudo` privileges.
2. Execute the bootstrap script:

   ```bash
   curl -sSf https://apt.repo.hyperi.io/edgestream_installer | sudo bash
   ```

   The script configures the package repositories, installs prerequisites, and deploys EdgeStream Hub services.

3. When the installer completes, view the generated admin credentials:

   ```bash
   sudo cat /root/edgestream_credentials
   ```
