# Sources

Sources are where events originate — either ingested from network sockets, cloud log brokers, agents (`nxlog`, `winlogbeat`, `vector`), or gathered locally via system metrics and log scrapers into `edgestream-hub`.

## Available Sources

| Source | Label | Base (required) fields | TLS | Common fields (high-level groups) |
| :--- | :--- | :--- | :--- | :--- |
| `aws_s3` | AWS S3 | `sqs.queue_url`, `region`, `auth.strategy`, `decoding.codec` | ✅ (HTTPS / client) | `description`, `auth.*`, `decoding.*`, `compression`, `multiline.*`, `proxy.*`, `sqs.*` |
| `aws_sqs` | AWS SQS | `queue_url`, `region`, `auth.strategy`, `decoding.codec` | ✅ (HTTPS / client) | `description`, `auth.*`, `decoding.*`, `proxy.*`, `poll_secs`, `visibility_timeout_secs` |
| `cef` | Common Event Format | `address`, `mode` (`tcp\|udp`) | ✅ (server, TCP only) | `description`, `route_label`, `translate_custom_fields`, `max_length`, `receive_buffer_bytes`, `permit_origin`, `timezone` |
| `fluent` | Fluent | `address` | ✅ (server) | `description`, `route_label`, `keepalive.*`, `receive_buffer_bytes`, `permit_origin` |
| `host_metrics` | Host Metrics | _none (defaults apply)_ | ❌ (internal scraper) | `description`, `route_label`, `collectors.*`, `scrape_interval_secs`, `namespace` |
| `http_client` | HTTP Client | `endpoint`, `decoding.codec`, `scrape_interval_secs` | ✅ (HTTPS / client) | `description`, `route_label`, `auth.*`, `decoding.*`, `headers`, `method`, `proxy.*`, `query.*` |
| `http_server` | HTTP Server | `address`, `decoding.codec` | ✅ (server) | `description`, `route_label`, `auth.*`, `decoding.*`, `headers`, `path`, `permit_origin`, `strict_path` |
| `internal_metrics`| Internal Metrics | _none (defaults apply)_ | ❌ (internal collector) | `description`, `route_label`, `scrape_interval_secs`, `namespace` |
| `logstash` | Logstash | `address` | ✅ (server) | `description`, `route_label`, `keepalive.*`, `receive_buffer_bytes`, `permit_origin` |
| `netflow` | NetFlow / IPFIX | `address` | ❌ (UDP datagrams) | `description`, `route_label`, `ports`, `workers`, `udp-size` |
| `o365audit` | Office 365 Audit | `tenant_id`, `client_id`, `client_secret` | ✅ (HTTPS / client) | `description`, `route_label`, `content_types`, `poll_interval_secs`, `proxy.*` |
| `opentelemetry` | OpenTelemetry | `address`, `grpc.address` | ✅ (server) | `description`, `route_label`, `grpc.*`, `http.*`, `permit_origin` |
| `postgresql_metrics`| PostgreSQL Metrics | `endpoints`, `namespace` | ✅ (client) | `description`, `route_label`, `databases`, `scrape_interval_secs`, `tls.*` |
| `socket` | Raw Socket | `address`, `mode` (`tcp\|udp\|unix`), `decoding.codec` | ✅ (server, TCP only) | `description`, `route_label`, `decoding.*`, `framing.*`, `multiline.*`, `max_length`, `receive_buffer_bytes`, `permit_origin` |
| `splunk_hec` | Splunk HEC | `address` | ✅ (server) | `description`, `route_label`, `token`, `query_parameters`, `permit_origin` |
| `syslog` | Syslog | `address`, `mode` (`tcp\|udp\|unix`) | ✅ (server, TCP only) | `description`, `route_label`, `max_length`, `receive_buffer_bytes`, `permit_origin`, `timezone` |
| `vector` | Vector (edgestream-hub) | `address` | ✅ (server) | `description`, `route_label`, `keepalive.*`, `receive_buffer_bytes`, `permit_origin`, `version` |

***

## TLS & Security (Quick Reference)

Network-listening and outbound client sources support TLS encryption via the standard **`tls.*`** block:

- `tls.enabled` *(bool, default: false)* – Enforce TLS for incoming or outgoing traffic.
- `tls.alpn_protocols` *(string)* – Priority-ordered ALPN negotiation protocols.
- `tls.ca_file` *(file)* – Additional Certificate Authority bundle (PEM).
- `tls.crt_file` *(file)* – Server certificate (for listeners) or client certificate (for outbound scrapers).
- `tls.key_file` *(file)* – Matching private key (PEM).
- `tls.key_pass` *(string)* – Passphrase used to decrypt the private key.
- `tls.verify_certificate` *(bool, default: true)* – Validate peer certificates (requires client certs when hosting a server; validates remote CA when pulling).
- `tls.verify_hostname` *(bool, default: true)* – Check server SAN/CN identity (client/pull sources only).

**Auth & proxy mechanisms (where supported):**

- **AWS Authentication:** `auth.strategy` (`access_key_id|credentials_file|imds`), `auth.assume_role`, `auth.external_id`, `auth.session_name`.
- **HTTP Listener Auth:** `auth.strategy` (`none|basic|bearer`), credentials validation tokens.
- **Outbound HTTP / S3 Proxying:** `proxy.enabled`, `proxy.http`, `proxy.https`, `proxy.no_proxy`.

***

## Common Fields Reference

These settings repeat across multiple source configurations:

- **Routing & Identification**
  - `description` – Freeform operational label for the UI and configuration pipeline.
  - `route_label` *(string)* – Target tag used to direct ingested events into specific filter pipelines or destination sinks (defaults to `<source_name>-<type>`).
- **Decoding (Ingestion Codec)**
  - `decoding.codec` – Parser used to unpack payloads (`avro`, `bytes`, `cef`, `gelf`, `influxdb`, `json`, `logfmt`, `native`, `native_json`, `protobuf`, `syslog`, `vrl`).
  - `decoding.lossy` *(bool, default: true)* – Replace invalid UTF-8 bytes with the Unicode replacement character instead of discarding the message.
- **Network & Socket Controls**
  - `address` – Interface socket binding (`0.0.0.0:<port>`) or `systemd{#N}` activation reference.
  - `permit_origin` *(string array)* – CIDR allowlist defining remote networks permitted to connect.
  - `receive_buffer_bytes` *(int)* – OS TCP/UDP socket receive buffer override (`SO_RCVBUF`).
- **Multiline Framing**
  - `multiline.start_pattern` – Regex defining the first line of a multi-row log entry.
  - `multiline.condition_pattern` – Continuation regex determining whether subsequent lines belong to the existing event.
  - `multiline.mode` (`continue_past|continue_through|halt_before|halt_with`).
  - `multiline.timeout_ms` *(int, default: 600000)* – Wait window before flushing pending buffer chunks.

***

## Source Settings

```{toctree}
:maxdepth: 1

aws_s3
aws_sqs
cef
fluent
host_metrics
http_client
http_server
internal_metrics
logstash
netflow
o365audit
opentelemetry
postgresql_metrics
socket
splunk_hec
syslog
vector
```
