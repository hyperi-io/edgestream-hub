# 🎛️ Filters

Filters (also referred to as Transforms) intercept events ingested from a source and evaluate conditional logic before the events continue downstream to destination sinks. Events that evaluate to true pass through the pipeline; non-matching events are dropped.

## Overview

Navigate to Administration → Configuration → Filters to view and manage existing filter rules.

From the filter management dashboard, you can:
- Search & Filter: Perform real-time text searches across filter names, parent sources, types, and descriptions.
- Inspect & Sort: View status badges (Enabled / Disabled), bound upstream sources, and sort columns alphabetically or by status.
- Lifecycle Actions: Create, edit existing filter logic, toggle operational status, or delete filters with confirmation prompts.

## Configuration Fields
When creating or modifying a filter in the drawer interface, configure the following fields:

| Field    | Type     | Default  | Required | Validation / Description
| -------- | -------- | -------- | -------- | -------- |
| Enabled | Boolean | true | No | Toggles whether this filter actively evaluates traffic. When disabled, no events pass through this stage. | 
| Name | String | "" | Yes | Unique identifier for the filter. Allowed characters: A-Z, a-z, 0-9, _, -. (Immutable after creation). |
| Description | String| ""| Yes| Human-readable explanation of what traffic this filter isolates or processes. | 
| Source (parent) | Select| "" | Yes | The upstream data input (e.g., syslog_example, netflow_inbound) feeding into this filter. |
| Filter Logic | Mode | Query Builder | Yes | Selects the rule evaluation method: Query Builder or Advanced Mode (VRL). | 

## Filter Logic Modes

EdgeStream Hub provides two methods for writing filter conditions: a visual Query Builder for standard conditional operations, and an Advanced Mode (VRL) for direct Vector Remap Language programming.

1. ### Query Builder (Visual Editor)
    
    The Query Builder allows you to construct compound Boolean expressions without writing code. Rules can be grouped using AND or OR combinators.

    Each rule consists of a target Field, a comparison Operator, and an optional Value:

    | UI Operator | Backend Operator | Requires Value | Description | 
    | -------- | -------- | -------- | -------- |
    | = | equals | Yes | Exact equality match. | 
    | != | notEquals | Yes| Value does not equal the target. | 
    | > / >= | greaterThan / greaterThanOrEqual | Yes | Numeric or timestamp greater than (or equal). |
    | < / <= | lessThan / lessThanOrEqual | Yes | Numeric or timestamp less than (or equal). | 
    | contains | contains | Yes | Target string contains the substring. | 
    | begins with | startsWith | Yes | Target string begins with prefix. | 
    | ends with | endsWith | Yes | Target string terminates with suffix. | 
    | in / not in | in / notIn | Yes | Checks membership within a delimited set. | 
    | between / not between | between / notBetween | Yes | Checks bounded numeric or date range. | 
    | is null / is not null | null / notNull | No | Evaluates whether field key exists and is non-null. | 
    | is empty / is not empty | empty / notEmpty | No | Evaluates if string or array is zero-length. | 

    ```{note}
    When using the Query Builder, all rules requiring a value must be filled before submission, or validation will fail.
    ```

2. ### Advanced Mode (VRL)

    Selecting Advanced Mode switches the logic editor to a code editor for Vector Remap Language (VRL).
    
    VRL mode allows complex conditional logic, regex pattern matching, type checking, and arithmetic comparisons directly against event payloads.
    
    **Requirements for Filter VRL**

    For a filter component, your VRL expression must evaluate to a boolean (true or false) representing whether the event should be retained:
    
    **Example 1: Basic string and numeric condition**
    ```bash
    .service == "auth_service" && .status_code >= 400
    ```

    **Example 2: Regex matching on raw syslog messages**
    ```bash
    match(.message, r'^(ERROR|FATAL|CRITICAL):')
    ```

    **Example 3: CIDR allowlist / IP subnet validation**
    ```bash
    is_ipv4(.client_ip) && cidr_contains("192.168.1.0/24", .client_ip)
    ```

    **Example 4: Nested field existence and array containment**
    ```bash
    exists(.user.roles) && includes(array!(.user.roles), "admin")
    ```

## Step-by-Step: Creating a Filter
1. Open Administration → Configuration → Filters.
2. Click Create in the upper-right corner.
3. In the Create Transform drawer:
    - Keep Enabled checked.
    - Provide a unique Name (e.g., drop_healthchecks).
    - Add a concise Description (e.g., Drops internal HTTP probe events).
    - Select the target Source from the dropdown menu.
4. Choose the logic mode:
    - Select Query Builder to assemble visual rules (e.g., path != /healthz).
    - Select Advanced Mode to input custom VRL logic directly.
5. Click Create to compile and apply the filter pipeline.

## Best Practices
- Pipeline Placement: Connect filters directly to high-volume sources (syslog, netflow, cef) to drop unwanted noise as early as possible before events hit expensive destinations like S3 or ClickHouse.
- Name Immutability: Filter names cannot be modified after initial creation. Use consistent naming conventions such as \<source>_\<purpose>_filter (e.g., syslog_drop_debug).
- Safe VRL Testing: When writing custom VRL in Advanced Mode, account for nullable fields using the exists() function or VRL error-coalescing operators (??) to prevent runtime evaluation aborts on malformed records.