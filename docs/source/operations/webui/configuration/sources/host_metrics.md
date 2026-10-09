# host\_metrics

Collect logs from **Host Metrics**

**Type:** `host_metrics`

{% code title="sample.yaml" %}
```yaml
sources:
  host_metrics_example:
    type: host_metrics
    route_label: ''
    metric_to_log: false
  # optional:
  #   <key>: <value>
```
{% endcode %}

## Fields Reference

Below are tables for **Base** and **Optional** sections. Columns: Key, Label, Type, Default, Required, Depends on, Enum / Notes.

### Base

| Key             | Label               | Type   | Default | Required | Enum / Notes                                                                                                           | Depends on |
| --------------- | ------------------- | ------ | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------- | ---------- |
| route\_label    | Event Routing Label | string | ""      | —        | The label to use in routing these events to a destination. Defaults to source name-type.                               | —          |
| metric\_to\_log | Metric to Log       | bool   | false   | —        | Convert a metric event into a log event, which can be useful for sending metrics to log-support downstream components. | —          |

### Optional

| Key                             | Label                           | Type       | Default                                                                                          | Required | Enum / Notes                                                                                                                                                                          | Depends on |
| ------------------------------- | ------------------------------- | ---------- | ------------------------------------------------------------------------------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| description                     | Description                     | string     | ""                                                                                               | —        | The description of the entry.                                                                                                                                                         | —          |
| collectors                      | Collectors                      | enum-multi | \["cpu", "disk", "filesystem", "load", "host", "memory", "network", "process", "cgroups", "tcp"] | —        | The list of host metric collector services to use. Defaults to all collectors. Enum: \["cpu", "disk", "filesystem", "load", "host", "memory", "network", "process", "cgroups", "tcp"] | —          |
| namespace                       | Namespace                       | string     | host                                                                                             | —        | Overrides the default namespace for the metrics emitted by the source.                                                                                                                | —          |
| scrape\_interval\_secs          | Scrape Interval Secs            | int        | 15                                                                                               | —        | The interval between metric gathering, in seconds.                                                                                                                                    | —          |
| cgroups.base                    | Cgroups Base                    | string     | ""                                                                                               | —        | The base cgroup name to provide metrics for.                                                                                                                                          | —          |
| cgroups.groups.excludes         | Cgroups Groups Excludes         | string     | ""                                                                                               | —        | CSV list of cgroup name patterns to exclude in gathering usage metrics.                                                                                                               | —          |
| cgroups.groups.includes         | Cgroups Groups Includes         | string     | ""                                                                                               | —        | CSV list of cgroup name patterns to include in gathering usage metrics.                                                                                                               | —          |
| cgroups.levels                  | Cgroups Levels                  | int        | 100                                                                                              | —        | The number of levels of the cgroups hierarchy for which to report metrics. A value of 1 means the root or named cgroup.                                                               | —          |
| disk.devices.excludes           | Disk Devices Excludes           | string     | ""                                                                                               | —        | CSV list of device name patterns to exclude in gathering I/O utilization metrics.                                                                                                     | —          |
| disk.devices.includes           | Disk Devices Includes           | string     | ""                                                                                               | —        | CSV list of device name patterns to include in gathering I/O utilization metrics.                                                                                                     | —          |
| filesystem.devices.excludes     | Filesystem Devices Excludes     | string     | ""                                                                                               | —        | CSV list of device name patterns to exclude in gathering usage metrics.                                                                                                               | —          |
| filesystem.devices.includes     | Filesystem Devices Includes     | string     | ""                                                                                               | —        | CSV list of device name patterns to include in gathering usage metrics.                                                                                                               | —          |
| filesystem.filesystems.excludes | Filesystem Filesystems Excludes | string     | ""                                                                                               | —        | CSV list of filesystem name patterns to exclude in gathering usage metrics.                                                                                                           | —          |
| filesystem.filesystems.includes | Filesystem Filesystems Includes | string     | ""                                                                                               | —        | CSV list of filesystem name patterns to include in gathering usage metrics.                                                                                                           | —          |
| filesystem.mountpoints.excludes | Filesystem Mountpoints Excludes | string     | ""                                                                                               | —        | CSV list of mount point path patterns to exclude in gathering usage metrics.                                                                                                          | —          |
| filesystem.mountpoints.includes | Filesystem Mountpoints Includes | string     | ""                                                                                               | —        | CSV list of mount point path patterns to include in gathering usage metrics.                                                                                                          | —          |
| network.devices.excludes        | Network Devices Excludes        | string     | ""                                                                                               | —        | CSV list of device name patterns to exclude in gathering network utilization metrics.                                                                                                 | —          |
| network.devices.includes        | Network Devices Includes        | string     | ""                                                                                               | —        | CSV list of device name patterns to include in gathering network utilization metrics.                                                                                                 | —          |
| process.processes.excludes      | Process Processes Excludes      | string     | ""                                                                                               | —        | CSV list of process name patterns to exclude.                                                                                                                                         | —          |
| process.processes.includes      | Process Processes Includes      | string     | ""                                                                                               | —        | CSV list of process name patterns to include.                                                                                                                                         | —          |
