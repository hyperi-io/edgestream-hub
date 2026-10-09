# Vector
Send events to **Vector**.

**Type:** `vector`

## Sample YAML
```yaml
destinations:
  vector_example:
    type: vector
    address: 0.0.0.0:9000
    tls:
      tls.enabled: false
      tls.alpn_protocols: ''
      tls.ca_file: ''
      tls.crt_file: ''
      tls.key_file: ''
      tls.key_pass: ''
      tls.server_name: ''
      tls.verify_certificate: true
      tls.verify_hostname: true
  # optional:
  #   <key>: <value>
```

## Fields Reference
Below are tables for **Base**, **TLS**, and **Optional** sections. Columns: Key, Label, Type, Default, Required, Depends on, Enum / Notes.

### Base
| Key | Label | Type | Default | Required | Enum / Notes | Depends on |
|---|---|---|---|---|---|---|
| address | Address | regex | 0.0.0.0:9000 | ✅ | The socket address to listen for connections on, or systemd{#N} to use the Nth socket passed by systemd socket activation. | — |

### TLS
| Key | Label | Type | Default | Required | Enum / Notes | Depends on |
|---|---|---|---|---|---|---|
| tls.enabled | TLS Enabled | bool | false | — | Whether or not to require TLS for incoming or outgoing connections. When enabled and used for incoming connections, an identity certificate is also required. See tls.crt_file for more information. | — |
| tls.alpn_protocols | ALPN protocols | string | "" | — | Sets the list of supported ALPN protocols. Declare the supported ALPN protocols, which are used during negotiation with peer. They are prioritized in the order that they are defined. | — |
| tls.ca_file | Certificate Authority File | file_ca_file | "" | — | Absolute path to an additional CA certificate file. | — |
| tls.crt_file | Certificate File | file_crt_file | "" | — | Absolute path to a certificate file used to identify this server. | — |
| tls.key_file | Private Key | file_key_file | "" | — | Absolute path to a private key file used to identify this server. | — |
| tls.key_pass | Private Key Passphrase | string | "" | — | Passphrase used to unlock the encrypted key file. | — |
| tls.server_name | Server Name | string | "" | — | Server name to use when using Server Name Indication (SNI). | — |
| tls.verify_certificate | Verify Certificate | bool | true | — | Enables certificate verification. For components that create a server, this requires that the client connections have a valid client certificate. For components that initiate requests, this validates that the upstream has a valid certificate. | — |
| tls.verify_hostname | Verify Hostname | bool | true | — | Enables hostname verification. If enabled, the hostname used to connect to the remote host must be present in the TLS certificate presented by the remote host, either as the Common Name or as an entry in the Subject Alternative Name extension. Only relevant for outgoing connections. | — |

### Optional
| Key | Label | Type | Default | Required | Enum / Notes | Depends on |
|---|---|---|---|---|---|---|
| description | Description | string | "" | — | The description of the entry. | — |
| acknowledgements.enabled | Acknowledgements Enabled | bool | false | — | Whether or not end-to-end acknowledgements are enabled. | — |
| batch.max_bytes | Batch Max Bytes | int | 10000000 | — | The maximum size of a batch that is processed by a sink. | — |
| batch.max_events | Batch Max Events | int | 500 | — | The maximum size of a batch before it is flushed. | — |
| batch.timeout_secs | Batch Timeout Secs | int | 300 | — | The maximum age of a batch before it is flushed. | — |
| buffer.type | Buffer Type | enum | memory | — | The type of buffer to use. Enum: ["disk", "memory"] | — |
| buffer.max_events | Buffer Max Events | int | 500 | — | The maximum number of events allowed in the buffer. | buffer.type = memory |
| buffer.max_size | Buffer Max Size | int | 268435488 | — | The maximum size of the buffer on disk. Must be at least ~256 megabytes (268435488 bytes). | buffer.type = disk |
| buffer.when_full | Buffer When Full | enum | block | — | Event handling behavior when a buffer is full. Enum: ["block", "drop_newest"] | — |
| compression | Compression | bool | false | — | Whether or not to compress requests. | — |

