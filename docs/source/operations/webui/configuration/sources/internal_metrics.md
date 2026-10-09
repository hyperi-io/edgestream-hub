# internal\_metrics

Collect logs from **Internal Metrics**

**Type:** `internal_metrics`

## Sample YAML

{% code title="sources.yaml" %}
```yaml
sources:
  internal_metrics_example:
    type: internal_metrics
    route_label: ''
    metric_to_log: false
  # optional:
  #   <key>: <value>
```
{% endcode %}

## Fields Reference

Below are tables for **Base**, **TLS**, and **Optional** sections. Columns: Key, Label, Type, Default, Required, Depends on, Enum / Notes.

### Base

| Key             | Label               | Type   | Default | Required | Enum / Notes                                                                                                           | Depends on |
| --------------- | ------------------- | ------ | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------- | ---------- |
| route\_label    | Event Routing Label | string | ""      | —        | The label to use in routing these events to a destination. Defaults to source name-type.                               | —          |
| metric\_to\_log | Metric to Log       | bool   | false   | —        | Convert a metric event into a log event, which can be useful for sending metrics to log-support downstream components. | —          |

### Optional

| Key                    | Label                | Type   | Default | Required | Enum / Notes                                                           | Depends on |
| ---------------------- | -------------------- | ------ | ------- | -------- | ---------------------------------------------------------------------- | ---------- |
| description            | Description          | string | ""      | —        | The description of the entry.                                          | —          |
| namespace              | Namespace            | string | vector  | —        | Overrides the default namespace for the metrics emitted by the source. | —          |
| scrape\_interval\_secs | Scrape Interval Secs | int    | 1       | —        | The interval between metric gathering, in seconds.                     | —          |
