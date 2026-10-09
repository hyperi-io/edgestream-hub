# Http
Send events to **Http**.

**Type:** `http`

## Sample YAML
```yaml
destinations:
  http_example:
    type: http
    uri: https://127.0.0.1:9000/endpoint
    decoding.codec: json
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
| uri | URI | regex | https://127.0.0.1:9000/endpoint | ✅ | The full URI to make HTTP requests to. | — |
| decoding.codec | Decoding Codec | enum | json | ✅ | The codec to use for decoding events. Enum: ["avro", "csv", "gelf", "json", "logfmt", "native", "native_json", "protobuf", "raw_message", "text"] | — |

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
| auth.strategy | Auth Strategy | enum | none | — | The authentication strategy to use. Enum: ["none", "basic", "bearer"] | — |
| auth.token | Auth Token | string | "" | — | The bearer authentication token. | auth.strategy = bearer |
| auth.user | Auth User | string | "" | — | The basic authentication username. | auth.strategy = basic |
| auth.password | Auth Password | string | "" | — | The basic authentication password. | auth.strategy = basic |
| batch.max_bytes | Batch Max Bytes | int | 10000000 | — | The maximum size of a batch that is processed by a sink. | — |
| batch.max_events | Batch Max Events | int | 500 | — | The maximum size of a batch before it is flushed. | — |
| batch.timeout_secs | Batch Timeout Secs | int | 300 | — | The maximum age of a batch before it is flushed. | — |
| buffer.type | Buffer Type | enum | memory | — | The type of buffer to use. Enum: ["disk", "memory"] | — |
| buffer.max_events | Buffer Max Events | int | 500 | — | The maximum number of events allowed in the buffer. | buffer.type = memory |
| buffer.max_size | Buffer Max Size | int | 268435488 | — | The maximum size of the buffer on disk. Must be at least ~256 megabytes (268435488 bytes). | buffer.type = disk |
| buffer.when_full | Buffer When Full | enum | block | — | Event handling behavior when a buffer is full. Enum: ["block", "drop_newest"] | — |
| compression | Compression | enum | gzip | — | The compression algorithm to use. Enum: ["gzip", "none", "snappy", "zlib", "zstd"] | — |
| encoding.avro.schema | Encoding Avro Schema | string | "" | — | The Avro schema. | encoding.codec = avro |
| encoding.csv.capacity | Encoding CSV Capacity | int | 8192 | — | Set the capacity (in bytes) of the internal buffer used in the CSV writer. This defaults to a reasonable setting. | encoding.codec = csv |
| encoding.csv.delimiter | Encoding CSV Delimiter | string | , | — | The field delimiter to use when writing CSV. | encoding.codec = csv |
| encoding.csv.double_quote | Encoding CSV Double Quote | bool | true | — | Enable double quote escapes. This is enabled by default, but it may be disabled. When disabled, quotes in field data are escaped instead of doubled. | encoding.codec = csv |
| encoding.csv.escape | Encoding CSV Escape | string | " | — | The escape character to use when writing CSV. | encoding.codec = csv |
| encoding.csv.fields | Encoding CSV Fields | string | "" | — | Configures the fields that will be encoded, as well as the order in which they appear in the output. | encoding.codec = csv |
| encoding.csv.quote | Encoding CSV Quote | string | " | — | The quote character to use when writing CSV. | encoding.codec = csv |
| encoding.csv.quote_style | Encoding CSV Quote Style | enum | necessary | — | The quoting style to use when writing CSV data. Enum: ["always", "necessary", "never", "non_numeric"] | encoding.codec = csv |
| encoding.except_fields | Encoding Except Fields | string | "" | — | List of fields that are excluded from the encoded event. | — |
| encoding.json.pretty | Encoding Json Pretty | bool | true | — | Whether to use pretty JSON formatting. | encoding.codec = json |
| encoding.json.metric_tag_values | Encoding Metric Tag Values | enum | necessary | — | Controls how metric tag values are encoded. Enum: ["full", "single"] | encoding.codec = json |
| encoding.text.metric_tag_values | Encoding Metric Tag Values | enum | necessary | — | Controls how metric tag values are encoded. Enum: ["full", "single"] | encoding.codec = text |
| encoding.only_fields | Encoding Only Fields | string | "" | — | List of fields that are included in the encoded event. | — |
| encoding.protobuf.desc_file | Encoding Protobuf Desc File | string | "" | — | The path to the protobuf descriptor set file. | encoding.codec = protobuf |
| encoding.protobuf.message_type | Encoding Protobuf Message Type | string | "" | — | The name of the message type to use for serializing. | encoding.codec = protobuf |
| encoding.timestamp | Encoding Timestamp | enum | rfc3339 | — | Format used for timestamp fields. Enum: ["rfc3339", "unix", "unix_float", "unix_ms", "unix_ns", "unix_us"] | — |
| framing.method | Framing Method | enum | none | — | The framing method. Enum: ["none", "bytes", "character_delimited", "length_delimited", "newline_delimited"] | — |
| framing.character_delimited.delimiter | Framing Character Delimited Delimiter | string | "" | — | The character that delimits byte sequences. | framing.method = character_delimited |
| framing.character_delimited.max_length | Framing Character Delimited Max Length | int | — | — | The maximum length of the byte buffer. This length does not include the trailing delimiter. | framing.method = character_delimited |
| framing.length_delimited.length_field_is_big_endian | Framing Length Delimited Length Field is Big Endian | bool | true | — | Length field byte order (little or big endian). | framing.method = length_delimited |
| framing.length_delimited.length_field_length | Framing Length Delimited Length Field Length | int | 4 | — | Number of bytes representing the field length. | framing.method = length_delimited |
| framing.length_delimited.length_field_offset | Framing Length Delimited Length Field Offset | int | — | — | Number of bytes in the header before the length field. | framing.method = length_delimited |
| framing.length_delimited.max_frame_length | Framing Length Delimited Frame Length | int | — | — | Maximum frame length. | framing.method = length_delimited |
| framing.newline_delimited.max_length | Framing Newline Delimited Max Length | int | — | — | The maximum length of the byte buffer. | framing.method = newline_delimited |
| method | Method | enum | post | — | Specifies the method of the HTTP request. Enum: ["delete", "get", "head", "patch", "post", "put"] | — |
| payload_prefix | Payload Prefix | string | "" | — | A string to prefix the payload with. | — |
| payload_suffix | Payload Suffix | string | "" | — | A string to suffix the payload with. | — |
| proxy.enabled | Proxy Enabled | bool | false | — | Enables proxying support. | — |
| proxy.http | Proxy HTTP | regex | — | — | Proxy endpoint to use when proxying HTTP traffic. | — |
| proxy.https | Proxy HTTPS | regex | — | — | Proxy endpoint to use when proxying HTTPS traffic. | — |
| proxy.no_proxy | Proxy No Proxy | string | "" | — | A list of hosts to avoid proxying. | — |

