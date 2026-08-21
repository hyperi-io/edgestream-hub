# Destinations (sinks)

### EdgeStream Destinations (Sinks)

***

Destinations (aka _sinks_) are where events are delivered — either to `hyperi dfe`, another `edgestream-hub` or to external systems such as S3, ClickHouse, Kafka, files, or HTTP endpoints.

***

#### Available Destinations

| Destination  | Label                   | Base (required) fields                         | TLS                | Common fields (high-level groups)                                                                                                                                                                                                          |
| ------------ | ----------------------- | ---------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `aws_s3`     | AWS S3                  | `bucket`, `region`, `encoding.codec`           | ✅ (client)         | `description`, `acknowledgements.enabled`, `batch.*`, `buffer.*`, `compression`, `encoding.*`, `framing.*`, `filename_*`, `server_side_encryption`, `ssekms_key_id*`, `storage_class`, `endpoint`, `timezone`, `proxy.*`, `acl`, `grant_*` |
| `clickhouse` | Clickhouse              | `endpoint`, `table`                            | ✅ (client)         | `description`, `acknowledgements.enabled`, `batch.*`, `buffer.*`, `compression`, `encoding.*`, `framing.*`, `endpoint`, `timezone`                                                                                                         |
| `file`       | File                    | `path`, `encoding.codec`                       | ❌ (not applicable) | `description`, `acknowledgements.enabled`, `buffer.*`, `compression`, `encoding.*`, `framing.*`, `idle_timeout_secs`, `timezone`                                                                                                           |
| `http`       | Http                    | `uri`, `decoding.codec`                        | ✅ (HTTPS)          | `description`, `acknowledgements.enabled`, `auth.*`, `batch.*`, `buffer.*`, `compression`, `encoding.*`, `framing.*`, `method`, `payload_prefix/suffix`, `proxy.*`                                                                         |
| `kafka`      | Kafka                   | `bootstrap_servers`, `topic`, `encoding.codec` | ✅ (client)         | `description`, `acknowledgements.enabled`, `batch.*`, `buffer.*`, `compression`, `encoding.*`, `headers_key`, `key_field`, `message_timeout_ms`, `sasl.*`, `socket_timeout_ms`, `librdkafka_options`                                       |
| `vector`     | Vector (edgestream-hub) | `address`                                      | ✅ (client/server)  | `description`, `acknowledgements.enabled`, `batch.*`, `buffer.*`, `compression`                                                                                                                                                            |

> `*` Fields marked with an asterisk are conditionally required (see details below).

***

#### TLS & Security (Quick Reference)

All sinks that communicate over the network can enable TLS via the shared **`tls.*`** block:

* `tls.enabled` _(bool, default: false)_ – Turn TLS on.
* `tls.alpn_protocols` _(string)_ – ALPN protocol list (ordered).
* `tls.ca_file` _(file)_ – Additional CA to trust (PEM).
* `tls.crt_file` _(file)_ – Client/server certificate (PEM).
* `tls.key_file` _(file)_ – Private key for certificate (PEM).
* `tls.key_pass` _(string)_ – Passphrase for encrypted key.
* `tls.server_name` _(string)_ – SNI override for outbound TLS.
* `tls.verify_certificate` _(bool, default: true)_ – Validate peer certificates (set **false** only for testing).
* `tls.verify_hostname` _(bool, default: true)_ – Verify hostname against cert (outbound only).

**Auth & proxy helpers (where supported):**

* HTTP sink: `auth.strategy` (`none|basic|bearer`), `auth.user`, `auth.password`, `auth.token`.
* Proxying (HTTP/HTTPS): `proxy.enabled`, `proxy.http`, `proxy.https`, `proxy.no_proxy`.
* Kafka: `sasl.enabled`, `sasl.mechanism`, `sasl.username`, `sasl.password`.

***

#### Common Fields Reference

These groups repeat across sinks; each sink may support a subset.

* **Description & Acks**
  * `description` – freeform text for the entry.
  * `acknowledgements.enabled` _(bool, default: false)_ – end-to-end acknowledgements.
* **Batching**
  * `batch.max_bytes` _(default: 10\_000\_000)_, `batch.max_events` _(default: 500)_, `batch.timeout_secs` _(default: 300)_.
* **Buffering**
  * `buffer.type` (`memory|disk`, default: `memory`)
  * `buffer.max_events` _(memory)_, `buffer.max_size` _(disk, default: 268,435,488 bytes)_
  * `buffer.when_full` (`block|drop_newest`, default: `block`)
* **Compression**
  * Typical values: `gzip|zstd|snappy|zlib|none` (varies by sink).
* **Encoding** (output format)
  * `encoding.codec` (e.g., `json`, `text`, `csv`, `protobuf`, `avro`, `gelf`, `logfmt`, `raw_message`, `native`, `native_json`)
  * Per-codec extras, e.g. `encoding.csv.*`, `encoding.avro.schema`, `encoding.protobuf.*`
  * Field filters: `encoding.only_fields`, `encoding.except_fields`
  * `encoding.json.pretty` _(bool)_
  * `encoding.timestamp` (`rfc3339|unix|unix_ms|unix_us|unix_ns|unix_float`)
