# o365audit

Collect logs from **Office 365 Audit**

Type: `o365audit`

## Sample YAML

```yaml
sources:
  o365audit_example:
    type: o365audit
    client.id: ''
    tenant.id: ''
    secret.key: ''
    route_label: ''
  # optional:
  #   <key>: <value>
```

## Fields Reference

Below are tables for **Base** and **Optional** sections. Columns: Key, Label, Type, Default, Required, Depends on, Enum / Notes.

### Base

| Key          | Label               | Type   | Default | Required | Enum / Notes                                                                                     | Depends on |
| ------------ | ------------------- | ------ | ------- | -------- | ------------------------------------------------------------------------------------------------ | ---------- |
| client.id    | Client ID           | string | ""      | ✅        | The unique identifier assigned to your Azure AD application entry.                               | —          |
| tenant.id    | Tenant ID           | string | ""      | ✅        | The unique identifier for your Azure AD tenant.                                                  | —          |
| secret.key   | Secret Key          | string | ""      | ✅        | The credential created for your application entry. (Actual key is only shown once upon creation) | —          |
| route\_label | Event Routing Label | string | ""      | —        | The label to use in routing these events to a destination. Defaults to source name-type.         | —          |

### Optional

| Key                        | Label                      | Type   | Default | Required | Enum / Notes                                                                                                                                                               | Depends on |
| -------------------------- | -------------------------- | ------ | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| description                | Description                | string | ""      | —        | The description of the entry.                                                                                                                                              | —          |
| poll\_schedule             | Poll Schedule              | string | 10m     | —        | Poll for new audit logs every secs. The format can include a number appended with the unit, d (days), h (hours), m (minutes), s (seconds) or a combination, such as 1h30m. | —          |
| hourstocollect             | Hours to Collect           | int    | 24      | —        | Look back this many hours for audit logs (max supported by Office API is 168). This should be greater than the poll schedule                                               | —          |
| audit.general              | Audit General              | bool   | true    | —        | Collect Audit General logs.                                                                                                                                                | —          |
| audit.azureactivedirectory | Audit AzureActiveDirectory | bool   | true    | —        | Collect Audit AzureActiveDirectory logs.                                                                                                                                   | —          |
| audit.exchange             | Audit Exchange             | bool   | true    | —        | Collect Audit Exchange logs.                                                                                                                                               | —          |
| audit.sharepoint           | Audit SharePoint           | bool   | true    | —        | Collect Audit SharePoint logs.                                                                                                                                             | —          |
| dlp.all                    | DLP All                    | bool   | true    | —        | Collect DLP All logs.                                                                                                                                                      | —          |
| maxthreads                 | Max Threads                | int    | 10      | —        | Maximum number of simultaneous threads retrieving logs.                                                                                                                    | —          |
