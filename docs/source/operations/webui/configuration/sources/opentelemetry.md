# opentelemetry

Collect logs from **Opentelemetry**

**Type:** `opentelemetry`

## Sample YAML

{% code title="opentelemetry_source.yaml" %}
```yaml
sources:
  opentelemetry_example:
    type: opentelemetry
    grpc.address: localhost:4317
    http.address: localhost:4318
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

| Key          | Label               | Type   | Default        | Required | Enum / Notes                                                                             | Depends on |
| ------------ | ------------------- | ------ | -------------- | -------- | ---------------------------------------------------------------------------------------- | ---------- |
| grpc.address | GRPC Address        | string | localhost:4317 | ✅        | The socket address to listen for connections on.                                         | —          |
| http.address | HTTP Address        | string | localhost:4318 | ✅        | The socket address to listen for connections on.                                         | —          |
| route\_label | Event Routing Label | string | ""             | —        | The label to use in routing these events to a destination. Defaults to source name-type. | —          |

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

| Key                                                 | Label                                           | Type   | Default | Required | Enum / Notes                                                                                                                                                                                          | Depends on |
| --------------------------------------------------- | ----------------------------------------------- | ------ | ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| description                                         | Description                                     | string | ""      | —        | The description of the entry.                                                                                                                                                                         | —          |
| http.headers                                        | HTTP Headers                                    | string | ""      | —        | A csv list of HTTP headers to include in the log event.                                                                                                                                               | —          |
| http.keepalive.max\_connection\_age\_jitter\_factor | HTTP Keepalive Max Connection Age Jitter Factor | int    | 0.1     | —        | The factor by which to jitter the max\_connection\_age\_secs value. A value of 0.1 means that the actual duration will be between 90% and 110% of the specified maximum duration.                     | —          |
| keepalive.max\_connection\_age\_secs                | HTTP Keepalive Max Connection Age Secs          | int    | 300     | —        | The maximum amount of time a connection may exist before it is closed by sending a Connection: close header on the HTTP response. Set this to a large value like 100000000 to “disable” this feature. | —          |
