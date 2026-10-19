# 🪵 Syslog Sources

The Syslog Sources interface provides streamlined provisioning and lifecycle management for basic network syslog listeners.

```{note}
This interface is tailored for standard UDP/TCP ingestion. To configure advanced syslog pipelines requiring **TLS/mTLS encryption**, custom certificates, or non-standard framing, refer to [Standard Sources](sources).
```

## Overview

Syslog listeners bind directly to network interfaces on the EdgeStream Hub to ingest syslog telemetry across standard network transport layers.

### Ingested Metadata Tagging

When an incoming event is processed by a configured listener, EdgeStream automatically enriches the event payload with standard internal metadata fields:

| Field | Injected Value | Description | 
| ----- | -------------- | ----------- |
| @edgestream.event.name | <listener_name> | The custom human-readable name defined for the listener. | 
| @edgestream.event.src_type | syslog | Identifies the originating pipeline mechanism. | 

## Creating a Syslog Source

1. Navigate to Administration → Configuration → Sources → Syslog (or Events → Syslog Sources).
2. Click Create in the upper-right corner.
3. In the drawer interface, configure the listener attributes:
    - Port: Specify a single network port (e.g., 514, 1514).
    
        ```{note}
        The target port must not conflict with active listeners or existing host services. EdgeStream Hub performs a pre-flight port availability check; provisioning will fail if the port is already bound.
        ```

    - Name: A descriptive, alphanumeric identifier (e.g., firewall_syslog). This string is stamped into @edgestream.event.name across all matching incoming records.
    
    - Protocol: Select the transport protocol:
      - UDP (Standard best-effort datagram delivery)
      - TCP (Connection-oriented stream delivery)
      - Both (TCP & UDP) (Listens across both protocols concurrently on the designated port)
      
4. Click Create. The listener initializes and begins accepting socket traffic immediately.

## Event Routing & Downstream Destinations

Once provisioned, events ingested by the syslog listener are routed based on your pipeline topology:

- Default Sink Routing: If an appliance-wide default destination sink is configured, events route to that egress pipeline automatically.
- Custom Sink Binding: To route events to specific egress endpoints (e.g., S3, ClickHouse, Kafka), navigate to Administration → Configuration → Destinations, edit the target sink, and add the new syslog listener name to its upstream input list.

## Modifying a Syslog Source

Existing listeners can be updated without recreating the pipeline entry, subject to specific parameter constraints.

1. Locate the target listener in the table and click Edit.

2. Update the editable properties:

   - Name: Modify the event enrichment identifier.

   - Protocol: Adjust transport mechanisms between UDP, TCP, or Both. At least one protocol must remain active.

3. Click Update to apply the configuration.

```{note}
Port Immutability: Network listening ports cannot be changed on an active source. To migrate syslog ingestion to a different network port, provision a new listener on the target port and decommission the old one.
```

## Deleting a Syslog Source

Decommissioning a source unbinds the port and stops socket ingestion.

1. Locate the listener in the list and click Delete.

2. A confirmation modal will appear. Review the resource name to ensure no downstream dashboards or storage pipelines depend on active traffic from this source.

3. Confirm the prompt to unbind the port and remove the listener.