# socket

Collect logs from **Socket**

**Type:** `socket`

## Sample YAML

{% code title="socket_example.yaml" %}
```yaml
sources:
  socket_example:
    type: socket
    address: 0.0.0.0:9000
    mode: tcp
    decoding.codec: json
    route_label: ''
    tls:
      tls.enabled: false
      tls.alpn_protocols: ''
      tls.verify_certificate: true
      tls.verify_hostname: true
      tls.ca_file: ''
      tls.crt_file: ''
      tls.key_file: ''
      tls.key_pass: ''
  # optional:
  #   <key>: <value>
```
{% endcode %}

## Fields Reference

Below are tables for **Base**, **TLS**, and **Optional** sections. Columns: Key, Label, Type, Default, Required, Depends on, Enum / Notes.

### Base

| Key            | Label               | Type   | Default      | Required | Enum / Notes                                                                                                                                      | Depends on |
| -------------- | ------------------- | ------ | ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| address        | Address             | regex  | 0.0.0.0:9000 | ✅        | The socket address to listen for connections on, or systemd{#N} to use the Nth socket passed by systemd socket activation.                        | —          |
| mode           | Mode                | enum   | tcp          | ✅        | The type of socket to use. Enum: \["tcp", "udp"]                                                                                                  | —          |
| decoding.codec | Decoding Codec      | enum   | json         | ✅        | The codec to use for decoding events. Enum: \["avro", "bytes", "gelf", "influxdb", "json", "native", "native\_json", "protobuf", "syslog", "vrl"] | —          |
| route\_label   | Event Routing Label | string | ""           | —        | The label to use in routing these events to a destination. Defaults to source name-type.                                                          | —          |

### TLS

| Key                     | Label                      | Type            | Default | Required | Enum / Notes                                                                                                                                                                                                                                                                                | Depends on |
| ----------------------- | -------------------------- | --------------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| tls.enabled             | TLS Enabled                | bool            | false   | —        | Whether or not to require TLS for incoming or outgoing connections. When enabled and used for incoming connections, an identity certificate is also required. See tls.crt\_file for more information.                                                                                       | mode = tcp |
| tls.alpn\_protocols     | ALPN protocols             | string          | ""      | —        | Sets the list of supported ALPN protocols. Declare the supported ALPN protocols, which are used during negotiation with peer. They are prioritized in the order that they are defined.                                                                                                      | —          |
| tls.verify\_certificate | Verify Certificate         | bool            | true    | —        | Enables certificate verification. For components that create a server, this requires that the client connections have a valid client certificate. For components that initiate requests, this validates that the upstream has a valid certificate.                                          | —          |
| tls.verify\_hostname    | Verify Hostname            | bool            | true    | —        | Enables hostname verification. If enabled, the hostname used to connect to the remote host must be present in the TLS certificate presented by the remote host, either as the Common Name or as an entry in the Subject Alternative Name extension. Only relevant for outgoing connections. | —          |
| tls.ca\_file            | Certificate Authority File | file\_ca\_file  | ""      | —        | Absolute path to an additional CA certificate file.                                                                                                                                                                                                                                         | —          |
| tls.crt\_file           | Certificate File           | file\_crt\_file | ""      | —        | Absolute path to a certificate file used to identify this server.                                                                                                                                                                                                                           | —          |
| tls.key\_file           | Private Key                | file\_key\_file | ""      | —        | Absolute path to a private key file used to identify this server.                                                                                                                                                                                                                           | —          |
| tls.key\_pass           | Private Key Passphrase     | string          | ""      | —        | Passphrase used to unlock the encrypted key file.                                                                                                                                                                                                                                           | —          |

### Optional

| Key                                     | Label                          | Type   | Default | Required | Enum / Notes                                                                                                                                                                                                                           | Depends on                    |
| --------------------------------------- | ------------------------------ | ------ | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| description                             | Description                    | string | ""      | —        | The description of the entry.                                                                                                                                                                                                          | —                             |
| max\_length                             | Max Length                     | int    | —       | —        | The maximum buffer size of incoming messages.                                                                                                                                                                                          | mode = udp                    |
| receive\_buffer\_bytes                  | Receive Buffer                 | int    | —       | —        | The size of the receive buffer used for each connection. Relevant when: mode = 'tcp' or mode = 'udp'                                                                                                                                   | —                             |
| permit\_origin                          | Permit Origin                  | string | —       | —        | List of allowed origin IP networks. IP addresses must be in CIDR notation.                                                                                                                                                             | mode = tcp                    |
| decoding.avro.schema                    | Decoding Avro Schema           | string | ""      | —        | The Avro schema definition.                                                                                                                                                                                                            | decoding.codec = avro         |
| decoding.avro.strip\_schema\_id\_prefix | Strip Avro Schema ID Prefix    | bool   | true    | —        | For Avro datum encoded in Kafka messages, the bytes are prefixed with the schema ID.                                                                                                                                                   | decoding.codec = avro         |
| decoding.gelf.lossy                     | Decoding Gelf Lossy            | bool   | true    | —        | Determines whether or not to replace invalid UTF-8 sequences instead of failing.                                                                                                                                                       | decoding.codec = gelf         |
| decoding.influxdb.lossy                 | Decoding Influxdb Lossy        | bool   | true    | —        | Determines whether or not to replace invalid UTF-8 sequences instead of failing.                                                                                                                                                       | decoding.codec = influxdb     |
| decoding.json.lossy                     | Decoding Json Lossy            | bool   | true    | —        | Determines whether or not to replace invalid UTF-8 sequences instead of failing.                                                                                                                                                       | decoding.codec = json         |
| decoding.native\_json.lossy             | Decoding Native Json Lossy     | bool   | true    | —        | Determines whether or not to replace invalid UTF-8 sequences instead of failing.                                                                                                                                                       | decoding.codec = native\_json |
| decoding.protobuf.desc\_file            | Decoding Protobuf Desc File    | string | ""      | —        | Path to desc file.                                                                                                                                                                                                                     | decoding.codec = protobuf     |
| decoding.protobuf.message\_type         | Decoding Protobuf Message Type | string | ""      | —        | Path to desc file.                                                                                                                                                                                                                     | decoding.codec = protobuf     |
| decoding.syslog.lossy                   | Decoding Syslog Lossy          | bool   | true    | —        | Determines whether or not to replace invalid UTF-8 sequences instead of failing.                                                                                                                                                       | decoding.codec = syslog       |
| decoding.vrl.source                     | Decoding Vrl Source            | string | ""      | —        | The Vector Remap Language (VRL) program to execute for each event. Note that the final contents of the . target will be used as the decoding result. Compilation error or use of ‘abort’ in a program will result in a decoding error. | decoding.codec = vrl          |
| decoding.vrl.timezone                   | Decoding Vrl Timezone          | string | local   | —        | The name of the timezone to apply to timestamp conversions that do not contain an explicit time zone. The time zone name may be any name in the TZ database, or local to indicate system local time.                                   | decoding.codec = vrl          |
