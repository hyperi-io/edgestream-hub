# postgresql\_metrics

Collect logs from **Postgresql Metrics**

{% hint style="info" %}
Type: `postgresql_metrics`
{% endhint %}

## Sample YAML

{% code title="sources.yaml" %}
```yaml
sources:
  postgresql_metrics_example:
    type: postgresql_metrics
    endpoints: ''
    route_label: ''
    tls:
      tls.ca_file: ''
  # optional:
  #   <key>: <value>
```
{% endcode %}

## Fields Reference

Below are tables for **Base**, **TLS**, and **Optional** sections. Columns: Key, Label, Type, Default, Required, Depends on, Enum / Notes.

### Base

| Key          | Label               | Type   | Default | Required | Enum / Notes                                                                                      | Depends on |
| ------------ | ------------------- | ------ | ------- | -------- | ------------------------------------------------------------------------------------------------- | ---------- |
| endpoints    | Endpoints           | string | ""      | ✅        | A CSV list of PostgreSQL instances to scrape. Each endpoint must be in the Connection URI format. | —          |
| route\_label | Event Routing Label | string | ""      | —        | The label to use in routing these events to a destination. Defaults to source name-type.          | —          |

### TLS

| Key          | Label                      | Type           | Default | Required | Enum / Notes                                        | Depends on |
| ------------ | -------------------------- | -------------- | ------- | -------- | --------------------------------------------------- | ---------- |
| tls.ca\_file | Certificate Authority File | file\_ca\_file | ""      | —        | Absolute path to an additional CA certificate file. | —          |

### Optional

| Key                    | Label                | Type   | Default    | Required | Enum / Notes                                                                                                                                       | Depends on |
| ---------------------- | -------------------- | ------ | ---------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| description            | Description          | string | ""         | —        | The description of the entry.                                                                                                                      | —          |
| exclude\_databases     | Exclude Databases    | string | ""         | —        | A CSV list of databases to match (by using POSIX Regular Expressions) against the datname column for which you don’t want to collect metrics from. | —          |
| include\_databases     | Include Databases    | string | ""         | —        | A CSV list of databases to match (by using POSIX Regular Expressions) against the datname column for which you want to collect metrics from.       | —          |
| namespace              | Namespace            | string | postgresql | —        | Overrides the default namespace for the metrics emitted by the source.                                                                             | —          |
| scrape\_interval\_secs | Scrape Interval Secs | int    | 15         | —        | The interval between scrapes, in seconds.                                                                                                          | —          |
