# cef

Collect logs from **CEF**

**Type:** `cef`

{% code title="sample.yaml" %}
```yaml
sources:
  cef_example:
    type: cef
    address: 0.0.0.0:9000
    mode: tcp
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

| Key          | Label               | Type   | Default      | Required | Enum / Notes                                                                                                               | Depends on |
| ------------ | ------------------- | ------ | ------------ | -------- | -------------------------------------------------------------------------------------------------------------------------- | ---------- |
| address      | Address             | regex  | 0.0.0.0:9000 | ✅        | The socket address to listen for connections on, or systemd{#N} to use the Nth socket passed by systemd socket activation. | —          |
| mode         | Mode                | enum   | tcp          | ✅        | The type of socket to use. Enum: \["tcp", "udp"]                                                                           | —          |
| route\_label | Event Routing Label | string | ""           | —        | The label to use in routing these events to a destination. Defaults to source name-type.                                   | —          |

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

| Key                       | Label                   | Type   | Default | Required | Enum / Notes                                                                                                                                                                                         | Depends on |
| ------------------------- | ----------------------- | ------ | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| description               | Description             | string | ""      | —        | The description of the entry.                                                                                                                                                                        | —          |
| translate\_custom\_fields | Translate Custom Fields | bool   | false   | —        | Toggles translation of custom field pairs to key:value.                                                                                                                                              | —          |
| max\_length               | Max Length              | int    | —       | —        | The maximum buffer size of incoming messages.                                                                                                                                                        | mode = udp |
| receive\_buffer\_bytes    | Receive Buffer          | int    | —       | —        | The size of the receive buffer used for each connection. Relevant when: mode = 'tcp' or mode = 'udp'                                                                                                 | —          |
| permit\_origin            | Permit Origin           | string | —       | —        | List of allowed origin IP networks. IP addresses must be in CIDR notation.                                                                                                                           | mode = tcp |
| timezone                  | Timezone                | string | local   | —        | The name of the timezone to apply to timestamp conversions that do not contain an explicit time zone. The time zone name may be any name in the TZ database, or local to indicate system local time. | —          |
