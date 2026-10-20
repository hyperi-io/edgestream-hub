# 🎛️ Event Filters

Event Filters—intercept ingested events from a designated source and evaluate conditional logic before the events proceed downstream.

Filters operate on a **pass/drop** model: an event evaluating to `true` continues along the ingestion pipeline to configured destinations, whereas an event evaluating to `false` is discarded. This reduces storage overhead, eliminates downstream ingestion noise, and enforces data quality standards at the network edge.

---

## Architectural Rules & Cardinality

* **1:1 Source Binding:** Exactly **one** filter can be attached to a given source.
* **Compound Logic:** While a source supports only a single filter attachment, that filter can evaluate arbitrarily complex logic containing multiple nested condition groups, combinators, and regular expressions.
* **Source Scope:** Any defined input—including standard sources, cloud connectors, and simple syslog listeners (regardless of whether they are currently enabled or disabled)—can be selected as an upstream parent.

---

## Filter Logic Engines

When configuring filter rules, EdgeStream Hub provides two evaluation modes: the visual **Query Builder** and direct **Vector Remap Language (VRL)** scripting.

### 1. Visual Query Builder

The Query Builder provides a structured interface powered by React Query Builder, allowing operators to construct boolean logic trees without hand-crafting code.

```text
[ Root Group: Match (AND) ]
  ├── [ Rule: status_code ] >= [ 400 ]
  └── [ Nested Group: Match (OR) ]
        ├── [ Rule: environment ] == [ "production" ]
        └── [ Rule: priority ] == [ "high" ]

```

#### Core Components

* **Rules:** An atomic condition consisting of three components:
* **Field:** The target key inside the event payload (e.g., `status_code`, `host`, `headers.user_agent`).
* **Operator:** The comparison operator (e.g., `=`, `!=`, `>`, `<`, `contains`, `starts with`, `ends with`, `in`, `is null`, `is empty`).
* **Value:** The literal scalar or list against which the extracted field is evaluated.


* **Combinators:** Determine how conditions evaluate within a group:
* **AND:** Every rule within the immediate group must evaluate to `true`.
* **OR:** At least one rule within the group must evaluate to `true`.


* **Nested Groups:** Sub-clauses that isolate logical precedence (identical to wrapping expressions in parentheses, such as `A AND (B OR C)`).

#### Usage Notes

* Operators such as `is null`, `is not null`, `is empty`, and `is not empty` evaluate field existence or string/array lengths and do not accept a value argument.
* All rules requiring a value must be completed before submission, or form validation will prevent saving.

---

### 2. Vector Remap Language (VRL)

For complex parsing, regex manipulation, CIDR subnet matching, and nested type validations, select **Advanced Mode (VRL)**.

VRL is an expression-oriented, type-safe language built specifically for high-throughput observability pipelines. In a filter component, the script must evaluate to a terminal **boolean expression** (`true` or `false`).

#### Syntax & Execution Model

* The incoming event is referenced using the path notation `.` (e.g., `.message`, `.http.status`, `.ip_address`).
* Statements execute sequentially, with the final unassigned expression determining whether the event passes (`true`) or drops (`false`).

#### Example VRL Filter Expressions

**Filter by HTTP Status Code and Path Exclusion:**

```vrl
# Retain client/server errors while dropping routine health probe traffic
.status_code >= 400 && !starts_with(string!(.path), "/healthz")

```

**Regex Matching Across Raw Syslog Payloads:**

```vrl
# Retain only explicit security authorization and privilege-escalation events
match(.message, r'sshd\[\d+\]: (Failed|Accepted) password')

```

**Network Subnet / CIDR Filtering:**

```vrl
# Drop internal lab subnet traffic; retain external boundary traffic
!cidr_contains("10.50.0.0/16", string!(.source_ip))

```

**Defensive Evaluation for Dynamic Schemas:**

```vrl
# Ensure the field exists and is non-empty before checking nested array values
exists(.user.roles) && includes(array!(.user.roles), "SecurityAdmin")

```

```{tip}
The management UI performs an automated syntax validation pass against your VRL script prior to saving, preventing invalid programs from reaching the runtime pipeline.

```

---

## Step-by-Step: Creating a Filter

1. Navigate to **Administration → Configuration → Filters** in the dashboard.
2. Click **Create** to launch the configuration drawer.
3. Configure the baseline metadata:
* **Enabled:** Toggle whether the filter actively processes traffic immediately upon creation.
* **Name:** A unique system identifier consisting of alphanumeric characters, hyphens, or underscores (`[A-Za-z0-9_-]`). This name is immutable once committed.
* **Description:** Operational notes clarifying the filtering criteria and business purpose.


4. Select the **Source** from the dropdown menu to bind the filter to an upstream data input.
5. Select the **Filter Logic** mode:
* Use **Query Builder** to assemble visual condition blocks.
* Use **Advanced Mode (VRL)** to input custom VRL scripts.


6. Click **Create**. The backend validates the logic, attaches the filter stage to the designated source pipeline, and begins processing live telemetry.

---

## Managing Existing Filters

All configured filters appear in the primary **Filters** data table, which displays the filter name, attached source, implementation type (`QUERY_BUILDER` or `VRL`), operational state, and descriptive notes.

* **Editing a Filter:** Select **Edit** adjacent to any filter entry. You can update the operational state (**Enabled** / **Disabled**), description, upstream source binding, and conditional logic. Filter names cannot be modified.
* **Deleting a Filter:** Click **Delete** to open a confirmation modal. Once confirmed, the filter stage is removed from the pipeline, and all subsequent events from the parent source flow directly to downstream destinations without restriction.