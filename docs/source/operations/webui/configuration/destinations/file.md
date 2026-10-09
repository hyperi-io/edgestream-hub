# File
Send events to **File**.

**Type:** `file`

## Sample YAML
```yaml
destinations:
  file_example:
    type: file
    path: /tmp/vector-%Y-%m-%d.log
    encoding.codec: json
  # optional:
  #   <key>: <value>
```

## Fields Reference
Below are tables for **Base**, **TLS**, and **Optional** sections. Columns: Key, Label, Type, Default, Required, Depends on, Enum / Notes.

### Base
| Key | Label | Type | Default | Required | Enum / Notes | Depends on |
|---|---|---|---|---|---|---|
| path | Path | string | /tmp/vector-%Y-%m-%d.log | ✅ | The path to write events to. | — |
| encoding.codec | Encoding Codec | enum | json | ✅ | The codec to use for encoding events. Enum: ["avro", "cef", "csv", "gelf", "json", "logfmt", "native", "native_json", "protobuf", "raw_message", "text"] | — |

### Optional
| Key | Label | Type | Default | Required | Enum / Notes | Depends on |
|---|---|---|---|---|---|---|
| description | Description | string | "" | — | The description of the entry. | — |
| acknowledgements.enabled | Acknowledgements Enabled | bool | false | — | Whether or not end-to-end acknowledgements are enabled. | — |
| buffer.type | Buffer Type | enum | memory | — | The type of buffer to use. Enum: ["disk", "memory"] | — |
| buffer.max_events | Buffer Max Events | int | 500 | — | The maximum number of events allowed in the buffer. | buffer.type = memory |
| buffer.max_size | Buffer Max Size | int | 268435488 | — | The maximum size of the buffer on disk. Must be at least ~256 megabytes (268435488 bytes). | buffer.type = disk |
| buffer.when_full | Buffer When Full | enum | block | — | Event handling behavior when a buffer is full. Enum: ["block", "drop_newest"] | — |
| compression | Compression | enum | none | — | The compression algorithm to use. Enum: ["gzip", "none", "zstd"] | — |
| encoding.avro.schema | Encoding Avro Schema | string | "" | — | The Avro schema. | encoding.codec = avro |
| encoding.cef.device_event_class_id | Device Event Class ID | string | "" | — | Unique identifier for each event type. Identifies the type of event reported. The value length must be less than or equal to 1023. | encoding.codec = cef |
| encoding.cef.device_product | Device Product | string | "" | — | Identifies the product of a vendor. The part of a unique device identifier. No two products can use the same combination of device vendor and device product. The value length must be less than or equal to 63. | encoding.codec = cef |
| encoding.cef.device_vendor | Device Vendor | string | "" | — | Identifies the vendor of the product. The part of a unique device identifier. No two products can use the same combination of device vendor and device product. The value length must be less than or equal to 63. | encoding.codec = cef |
| encoding.cef.device_version | Device Version | string | "" | — | Identifies the version of the problem. In combination with device product and vendor, it composes the unique id of the device that sends messages. The value length must be less than or equal to 31. | encoding.codec = cef |
| encoding.cef.name | CEF Name | string | "" | — | This is a path that points to the human-readable description of a log event. The value length must be less than or equal to 512. Equals 'cef.name' by default. | encoding.codec = cef |
| encoding.cef.severity | CEF Severity | string | "" | — | This is a path that points to the field of a log event that reflects importance of the event. Reflects importance of the event. It must point to a number from 0 to 10. 0 = Lowest, 10 = Highest. Equals to 'cef.severity' by default. | encoding.codec = cef |
| encoding.cef.version | CEF Version | enum | V0 | — | CEF Version. Can be either 0 or 1. Equals to '0' by default.. Enum: ["V0", "V1"] | encoding.codec = cef |
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
| idle_timeout_secs | Idle Timeout Secs | int | 30 | — | The amount of time that a file can be idle and stay open. After not receiving any events in this amount of time, the file is flushed and closed. | — |
| timezone | Timezone | string | "" | — | Timezone to use for any date specifiers in template strings. This can refer to any valid timezone as defined in the TZ database, or local which refers to the system local timezone. | — |

