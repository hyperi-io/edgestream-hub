# EdgeStream Hub

### Enterprise-Grade Observability & Security Pipeline Appliance

**Collect, filter, and route telemetry at the edge—without the configuration headaches.**

EdgeStream Hub is a turn-key telemetry processing appliance built on Debian. Designed to run seamlessly on bare-metal hardware or as a lightweight virtual machine, EdgeStream Hub provides a centralized control plane to ingest, shape, and deliver high-volume logs, metrics, and security events to your upstream destinations.

---

```{toctree}
:maxdepth: 2

about_docs
intro/index
start/index
operations/index
guides/index
COMMERCIAL

```

[Get Started](https://www.google.com/search?q=docs/quickstart.md) · [Documentation](https://www.google.com/search?q=docs/index.md) · [Latest Releases](https://www.google.com/search?q=https://github.com/your-org/edgestream-hub/releases) · [Architecture Overview](https://www.google.com/search?q=docs/architecture.md)

---

## Why EdgeStream Hub?

Modern infrastructure produces massive volumes of operational and security telemetry. Forwarding raw, unfiltered data directly to cloud SIEMs and analytical sinks leads to ballooning storage costs, pipeline bottlenecks, and operational noise.

EdgeStream Hub sits between your event producers and storage backends, providing line-rate processing, precision filtering, and multi-destination fanout—all configured through an intuitive web management dashboard.

---

## Key Capabilities

### 📥 Comprehensive Ingestion (Push & Pull)

Ingest telemetry across standard protocols, cloud APIs, and agent formats out of the box:

* **Network & Security:** Multi-protocol Syslog (UDP/TCP/TLS), Cisco NetFlow (v5/v7/v9/IPFIX), Common Event Format (CEF), and raw sockets.
* **Cloud & SaaS:** Native Microsoft 365 / Entra ID audit log extraction, AWS SQS queues, and Amazon S3 buckets.
* **Modern Observability:** Native OpenTelemetry (OTLP) endpoints, Vector point-to-point streaming, Splunk HEC emulation, and Elastic Beats (Lumberjack).

### 🎛️ Precision Event Filtering & Transformation

Stop paying to store health-check noise, redundant debug messages, and malformed records:

* **Visual Query Builder:** Build nested boolean rule trees (AND/OR, regex matches, numeric comparisons, null checks) without writing code.
* **Vector Remap Language (VRL):** Harness the full power of high-throughput, type-safe VRL scripts for deep payload transformation, regex parsing, and CIDR-based subnet validation.

### 📤 Multi-Destination Fan-Out

Route normalized data wherever your team needs it:

* Stream real-time security events to your SIEM while simultaneously archiving raw compressed payloads into low-cost object storage (S3, MinIO) or ClickHouse for long-term compliance.
* Decouple sources from destinations with dynamic routing and default fail-safe sinks.

### 🖥️ Turn-Key Appliance Management

Say goodbye to complex configuration files and manual daemon reloads:

* **Intuitive Web UI:** Manage listeners, inspect live pipelines, and update transforms entirely from your browser.
* **Enterprise Access Control:** Built-in multi-factor authentication (TOTP/MFA), role-based administration, and CLI break-glass recovery utilities.
* **Native Debian Base:** Stable, reproducible, and minimal host footprint with automated system update tracking directly from the dashboard.

---

## How It Works

```text
[ Data Sources ]               [ EdgeStream Hub ]                 [ Destinations ]
  Firewalls / Syslog  ───┐                                   ┌──► Cloud SIEM (Splunk, Elastic)
  Cloud (M365, AWS)   ───┼──► [ Ingest ] ──► [ Filter ] ────┼──► ClickHouse / Long-Term DB
  OTLP / Beats Agents ───┘      (Tagging)      (Drop/Keep)   └──► Object Storage (S3 / Cold Archive)

```

1. **Ingest:** Listeners bind to host interfaces or actively poll remote APIs, automatically enriching every record with source metadata (`@edgestream.event.*`).
2. **Filter:** Pipeline transforms evaluate incoming records in memory at line rate, dropping unwanted traffic and standardizing schemas.
3. **Deliver:** Clean, formatted events stream reliably to one or more configured sinks.

---

## Deployment Options

EdgeStream Hub is distributed as a pre-packaged appliance image and native Debian packages:

| Deployment Type | Target Environments | Recommended Use Case |
| --- | --- | --- |
| **Virtual Appliance** | VMware ESXi, Proxmox, Hyper-V, KVM | Standard enterprise edge and branch office collector |
| **Bare Metal** | 1U/2U Rackmount Hardware | High-throughput aggregation nodes (10GbE+ NetFlow/Syslog) |
| **Cloud Instance** | AWS EC2, Azure VM, GCP Compute | Regional cloud-native aggregation and transit routing |

---

## Ready to Deploy?

Get your edge telemetry pipeline running in under 15 minutes:

* **[Debian Quickstart Guide](https://www.google.com/search?q=docs/quickstart.md)** — Step-by-step installation instructions for Debian hosts.
* **[Sources Configuration](https://www.google.com/search?q=docs/sources.md)** — Learn how to set up your first syslog listener or cloud collector.
* **[Transforms & Filters](https://www.google.com/search?q=docs/filters.md)** — Discover how to write efficient drop rules and reduce downstream ingestion costs.
* **[Download Latest Release](https://www.google.com/search?q=https://github.com/your-org/edgestream-hub/releases)** — Grab the latest ISO, OVA, or `.deb` packages.