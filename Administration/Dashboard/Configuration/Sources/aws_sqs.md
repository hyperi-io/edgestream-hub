# aws\_sqs

Collect logs from **AWS SQS**

**Type:** `aws_sqs`

## Sample YAML

{% code title="aws_sqs_example.yaml" %}
```yaml
sources:
  aws_sqs_example:
    type: aws_sqs
    queue_url: ''
    delete_message: true
    decoding.codec: bytes
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

| Key             | Label               | Type   | Default | Required | Enum / Notes                                                                                                                                      | Depends on |
| --------------- | ------------------- | ------ | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| queue\_url      | Queue URL           | string | ""      | ✅        | The URL of the SQS queue to poll for messages.                                                                                                    | —          |
| delete\_message | Delete Message      | bool   | true    | ✅        | Whether to delete the message once it is processed.                                                                                               | —          |
| decoding.codec  | Decoding Codec      | enum   | bytes   | ✅        | The codec to use for decoding events. Enum: \["avro", "bytes", "gelf", "influxdb", "json", "native", "native\_json", "protobuf", "syslog", "vrl"] | —          |
| route\_label    | Event Routing Label | string | ""      | —        | The label to use in routing these events to a destination. Defaults to source name-type.                                                          | —          |

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

| Key                                 | Label                             | Type   | Default | Required | Enum / Notes                                                                                                                                                                                                                           | Depends on                    |
| ----------------------------------- | --------------------------------- | ------ | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| description                         | Description                       | string | ""      | —        | The description of the entry.                                                                                                                                                                                                          | —                             |
| auth.access\_key\_id                | Auth Access Key ID                | string | ""      | —        | The AWS access key ID.                                                                                                                                                                                                                 | —                             |
| auth.assume\_role                   | Auth Assume Role                  | string | ""      | —        | The ARN of an IAM role to assume.                                                                                                                                                                                                      | —                             |
| auth.credentials\_file              | Auth Credentials File             | string | ""      | —        | Path to the credentials file.                                                                                                                                                                                                          | —                             |
| auth.external\_id                   | Auth External ID                  | string | ""      | —        | The optional unique external ID in conjunction with role to assume.                                                                                                                                                                    | —                             |
| auth.imds.connect\_timeout\_seconds | Auth IMDS Connect Timeout Seconds | int    | 1       | —        | Connect timeout for IMDS.                                                                                                                                                                                                              | —                             |
| auth.imds.max\_attempts             | Auth IMDS Max Attempts            | int    | 4       | —        | Number of IMDS retries for fetching tokens and metadata.                                                                                                                                                                               | —                             |
| auth.load\_timeout\_secs            | Auth Load Timeout Secs            | int    | 30      | —        | Timeout for successfully loading any credentials, in seconds.                                                                                                                                                                          | —                             |
| auth.secret\_access\_key            | Auth Secret Access Key            | string | ""      | —        | The credentials profile to use.                                                                                                                                                                                                        | —                             |
| auth.region                         | Auth Region                       | string | ""      | —        | The AWS region.                                                                                                                                                                                                                        | —                             |
| auth.session\_name                  | Auth Session Name                 | string | ""      | —        | The optional RoleSessionName is a unique session identifier for your assumed role.                                                                                                                                                     | —                             |
| client\_concurrency                 | Client Concurrency                | int    | —       | —        | Number of concurrent tasks to create for polling the queue for messages.                                                                                                                                                               | —                             |
| decoding.avro.schema                | Decoding Avro Schema              | string | ""      | —        | The Avro schema definition.                                                                                                                                                                                                            | decoding.codec = avro         |
| decoding.gelf.lossy                 | Decoding Gelf Lossy               | bool   | true    | —        | Determines whether or not to replace invalid UTF-8 sequences instead of failing.                                                                                                                                                       | decoding.codec = gelf         |
| decoding.influxdb.lossy             | Decoding Influxdb Lossy           | bool   | true    | —        | Determines whether or not to replace invalid UTF-8 sequences instead of failing.                                                                                                                                                       | decoding.codec = influxdb     |
| decoding.json.lossy                 | Decoding Json Lossy               | bool   | true    | —        | Determines whether or not to replace invalid UTF-8 sequences instead of failing.                                                                                                                                                       | decoding.codec = json         |
| decoding.native\_json.lossy         | Decoding Native Json Lossy        | bool   | true    | —        | Determines whether or not to replace invalid UTF-8 sequences instead of failing.                                                                                                                                                       | decoding.codec = native\_json |
| decoding.protobuf.desc\_file        | Decoding Protobuf Desc File       | string | ""      | —        | Path to desc file.                                                                                                                                                                                                                     | decoding.codec = protobuf     |
| decoding.protobuf.message\_type     | Decoding Protobuf Message Type    | string | ""      | —        | Path to desc file.                                                                                                                                                                                                                     | decoding.codec = protobuf     |
| decoding.syslog.lossy               | Decoding Syslog Lossy             | bool   | true    | —        | Determines whether or not to replace invalid UTF-8 sequences instead of failing.                                                                                                                                                       | decoding.codec = syslog       |
| decoding.vrl.source                 | Decoding Vrl Source               | string | ""      | —        | The Vector Remap Language (VRL) program to execute for each event. Note that the final contents of the . target will be used as the decoding result. Compilation error or use of ‘abort’ in a program will result in a decoding error. | decoding.codec = vrl          |
| decoding.vrl.timezone               | Decoding Vrl Timezone             | string | local   | —        | The name of the timezone to apply to timestamp conversions that do not contain an explicit time zone. The time zone name may be any name in the TZ database, or local to indicate system local time.                                   | decoding.codec = vrl          |
| region                              | Region                            | string | ""      | —        | The AWS region of the target service.                                                                                                                                                                                                  | —                             |
| endpoint                            | Endpoint                          | string | ""      | —        | Custom endpoint for use with AWS-compatible services.                                                                                                                                                                                  | —                             |
| poll\_secs                          | Poll Secs                         | int    | 15      | ✅        | How long to wait while polling the queue for new messages, in seconds.                                                                                                                                                                 | —                             |
| proxy.enabled                       | Proxy Enabled                     | bool   | false   | —        | Enables proxying support.                                                                                                                                                                                                              | —                             |
| proxy.http                          | Proxy HTTP                        | regex  | —       | —        | Proxy endpoint to use when proxying HTTP traffic.                                                                                                                                                                                      | —                             |
| proxy.https                         | Proxy HTTPS                       | regex  | —       | —        | Proxy endpoint to use when proxying HTTPS traffic.                                                                                                                                                                                     | —                             |
| proxy.no\_proxy                     | Proxy No Proxy                    | string | ""      | —        | A list of hosts to avoid proxying.                                                                                                                                                                                                     | —                             |
| visibility\_timeout\_secs           | Visibility Timeout Secs           | int    | 300     | —        | The visibility timeout to use for messages, in seconds                                                                                                                                                                                 | —                             |
