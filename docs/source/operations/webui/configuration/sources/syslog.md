# syslog

Collect logs from **Syslog**

**Type:** `syslog`

{% code title="sample.yaml" %}
```yaml
sources:
  syslog_example:
    type: syslog
    address: 0.0.0.0:9000
    mode: udp
    path: ''
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

| Key          | Label               | Type   | Default      | Required | Enum / Notes                                                                                                               | Depends on  |
| ------------ | ------------------- | ------ | ------------ | -------- | -------------------------------------------------------------------------------------------------------------------------- | ----------- |
| address      | Address             | regex  | 0.0.0.0:9000 | ✅        | The socket address to listen for connections on, or systemd{#N} to use the Nth socket passed by systemd socket activation. | —           |
| mode         | Mode                | enum   | udp          | ✅        | The type of socket to use. Enum: \["tcp", "udp", "unix"]                                                                   | —           |
| path         | Path                | string | ""           | —        | The Unix socket path.                                                                                                      | mode = unix |
| route\_label | Event Routing Label | string | ""           | —        | The label to use in routing these events to a destination. Defaults to source name-type.                                   | —           |

### TLS

| Key                     | Label                      | Type            | Default | Required | Enum / Notes                                                                                                                                                                                                                                                                                | Depends on |
| ----------------------- | -------------------------- | --------------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| tls.enabled             | TLS Enabled                | bool            | false   | —        | Whether or not to require TLS for incoming or outgoing connections. When enabled and used for incoming connections, an identity certificate is also required. See tls.crt\_file for more information.                                                                                       | mode = tcp |
| tls.alpn\_protocols     | ALPN protocols             | string          | ""      | —        | Sets the list of supported ALPN protocols. Declare the supported ALPN protocols, which are used during negotiation with peer. They are prioritized in the order that they are defined.                                                                                                      | mode = tcp |
| tls.verify\_certificate | Verify Certificate         | bool            | true    | —        | Enables certificate verification. For components that create a server, this requires that the client connections have a valid client certificate. For components that initiate requests, this validates that the upstream has a valid certificate.                                          | mode = tcp |
| tls.verify\_hostname    | Verify Hostname            | bool            | true    | —        | Enables hostname verification. If enabled, the hostname used to connect to the remote host must be present in the TLS certificate presented by the remote host, either as the Common Name or as an entry in the Subject Alternative Name extension. Only relevant for outgoing connections. | mode = tcp |
| tls.ca\_file            | Certificate Authority File | file\_ca\_file  | ""      | —        | Absolute path to an additional CA certificate file.                                                                                                                                                                                                                                         | —          |
| tls.crt\_file           | Certificate File           | file\_crt\_file | ""      | —        | Absolute path to a certificate file used to identify this server.                                                                                                                                                                                                                           | mode = tcp |
| tls.key\_file           | Private Key                | file\_key\_file | ""      | —        | Absolute path to a private key file used to identify this server.                                                                                                                                                                                                                           | mode = tcp |
| tls.key\_pass           | Private Key Passphrase     | string          | ""      | —        | Passphrase used to unlock the encrypted key file.                                                                                                                                                                                                                                           | mode = tcp |

### Optional

| Key                    | Label               | Type   | Default | Required | Enum / Notes                                                                                         | Depends on  |
| ---------------------- | ------------------- | ------ | ------- | -------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| description            | Description         | string | ""      | —        | The description of the entry.                                                                        | —           |
| connection\_limit      | Connection Limit    | int    | 1024    | —        | The maximum number of TCP connections that are allowed at any given time.                            | mode = tcp  |
| keepalive.time\_secs   | Keepalive Time Secs | int    | 7200    | —        | The time to wait before starting to send TCP keepalive probes on an idle connection.                 | —           |
| max\_length            | Max Length          | int    | —       | —        | The maximum buffer size of incoming messages.                                                        | mode = udp  |
| receive\_buffer\_bytes | Receive Buffer      | int    | —       | —        | The size of the receive buffer used for each connection. Relevant when: mode = 'tcp' or mode = 'udp' | —           |
| permit\_origin         | Permit Origin       | string | —       | —        | List of allowed origin IP networks. IP addresses must be in CIDR notation.                           | mode = tcp  |
| socket\_file\_mode     | Socket File Mode    | int    | ""      | —        | Unix file mode bits to be applied to the unix socket file as its designated file permissions.        | mode = unix |
