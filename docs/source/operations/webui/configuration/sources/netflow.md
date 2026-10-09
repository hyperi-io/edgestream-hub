# netflow

Collect logs from **NetFlow**

**Type:** `netflow`

## Sample YAML

{% code title="config.yaml" %}
```yaml
sources:
  netflow_example:
    type: netflow
    address: 0.0.0.0:9000
    ports: 2055, 2056, 4739
    route_label: ''
  # optional:
  #   <key>: <value>
```
{% endcode %}

## Fields Reference

Below are tables for **Base** and **Optional** sections. Columns: Key, Label, Type, Default, Required, Depends on, Enum / Notes.

### Base

| Key          | Label               | Type   | Default          | Required | Enum / Notes                                                                                                               | Depends on |
| ------------ | ------------------- | ------ | ---------------- | -------- | -------------------------------------------------------------------------------------------------------------------------- | ---------- |
| address      | Address             | regex  | 0.0.0.0:9000     | ✅        | The socket address to listen for connections on, or systemd{#N} to use the Nth socket passed by systemd socket activation. | —          |
| ports        | Ports               | string | 2055, 2056, 4739 | —        | A csv list of ports to listen on for netflow traffic.                                                                      | —          |
| route\_label | Event Routing Label | string | ""               | —        | The label to use in routing these events to a destination. Defaults to source name-type.                                   | —          |

### Optional

| Key         | Label       | Type   | Default | Required | Enum / Notes                     | Depends on |
| ----------- | ----------- | ------ | ------- | -------- | -------------------------------- | ---------- |
| description | Description | string | ""      | —        | The description of the entry.    | —          |
| workers     | Workers     | int    | 50      | —        | NetFlow concurrent decoders.     | —          |
| udp-size    | UDP Size    | int    | 1500    | —        | Maximum netflow UDP packet size. | —          |
