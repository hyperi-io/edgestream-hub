# splunk\_hec

Collect logs from **Splunk HEC**

**Type:** `splunk_hec`

## Sample YAML

{% code title="splunk_hec_example.yaml" %}
```yaml
sources:
  splunk_hec_example:
    type: splunk_hec
    address: 0.0.0.0:9000
    route_label: ''
    valid_tokens: ''
    store_hec_token: false
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

| Key               | Label               | Type   | Default      | Required | Enum / Notes                                                                                                               | Depends on |
| ----------------- | ------------------- | ------ | ------------ | -------- | -------------------------------------------------------------------------------------------------------------------------- | ---------- |
| address           | Address             | regex  | 0.0.0.0:9000 | ✅        | The socket address to listen for connections on, or systemd{#N} to use the Nth socket passed by systemd socket activation. | —          |
| route\_label      | Event Routing Label | string | ""           | —        | The label to use in routing these events to a destination. Defaults to source name-type.                                   | —          |
| valid\_tokens     | Valid Tokens        | string | ""           | —        | A CSV list of valid HEC tokens.                                                                                            | —          |
| store\_hec\_token | Store HEC Token     | bool   | false        | —        | Whether or not to forward the Splunk HEC authentication token with events.                                                 | —          |

### TLS

| Key                     | Label                      | Type            | Default | Required | Enum / Notes                                                                                                                                                                                                                                                                                | Depends on |
| ----------------------- | -------------------------- | --------------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| tls.enabled             | TLS Enabled                | bool            | false   | —        | Whether or not to require TLS for incoming or outgoing connections. When enabled and used for incoming connections, an identity certificate is also required. See tls.crt\_file for more information.                                                                                       | —          |
| tls.alpn\_protocols     | ALPN protocols             | string          | ""      | —        | Sets the list of supported ALPN protocols. Declare the supported ALPN protocols, which are used during negotiation with peer. They are prioritized in the order that they are defined.                                                                                                      | —          |
| tls.verify\_certificate | Verify Certificate         | bool            | true    | —        | Enables certificate verification. For components that create a server, this requires that the client connections have a valid client certificate. For components that initiate requests, this validates that the upstream has a valid certificate.                                          | —          |
| tls.verify\_hostname    | Verify Hostname            | bool            | true    | —        | Enables hostname verification. If enabled, the hostname used to connect to the remote host must be present in the TLS certificate presented by the remote host, either as the Common Name or as an entry in the Subject Alternative Name extension. Only relevant for outgoing connections. | —          |
| tls.ca\_file            | Certificate Authority File | file\_ca\_file  | ""      | —        | Absolute path to an additional CA certificate file.                                                                                                                                                                                                                                         | —          |
| tls.crt\_file           | Certificate File           | file\_crt\_file | ""      | —        | Absolute path to a certificate file used to identify this server.                                                                                                                                                                                                                           | —          |
| tls.key\_file           | Private Key                | file\_key\_file | ""      | —        | Absolute path to a private key file used to identify this server.                                                                                                                                                                                                                           | —          |
| tls.key\_pass           | Private Key Passphrase     | string          | ""      | —        | Passphrase used to unlock the encrypted key file.                                                                                                                                                                                                                                           | —          |

### Optional

| Key                                            | Label                                      | Type | Default | Required | Enum / Notes                                                                                                                                                                                          | Depends on |
| ---------------------------------------------- | ------------------------------------------ | ---- | ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| keepalive.max\_connection\_age\_jitter\_factor | Keepalive Max Connection Age Jitter Factor | int  | 0.1     | —        | The factor by which to jitter the max\_connection\_age\_secs value. A value of 0.1 means that the actual duration will be between 90% and 110% of the specified maximum duration.                     | —          |
| keepalive.max\_connection\_age\_secs           | Keepalive Max Connection Age Secs          | int  | 300     | —        | The maximum amount of time a connection may exist before it is closed by sending a Connection: close header on the HTTP response. Set this to a large value like 100000000 to “disable” this feature. | —          |
