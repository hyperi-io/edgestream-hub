# 🔐 Web Interface Authentication

Web interface credentials authenticate operators to the EdgeStream Hub management dashboard.

```{note}
Web UI user accounts are strictly decoupled from host-level operating system authentication. A dashboard account does **not** grant SSH or local console shell privileges.
```

## Initial Bootstrap Access
During initial appliance provisioning, the installer generates a unique administrative access credential and saves it to the root filesystem:

```bash
/root/edgestream_credentials
```
To complete first-time sign-in:

1. Retrieve the bootstrap credentials from the host shell via SSH:

    ```bash
    sudo cat /root/edgestream_credentials
    ```

2. Navigate to https://<appliance-ip-or-fqdn> in your web browser.

3. Sign in using the default username (edgestream@local.com) and the generated access secret.

## Onboarding & Account Hardening
For security hygiene, transition away from the bootstrap account immediately after initial deployment:

1. Navigate to System → Users in the dashboard.

2. Select Create User and provision a dedicated administrative account for your operator or team identity.

3. Log out of the management dashboard.

4. Log back in using the newly created administrator credentials.

5. Return to System → Users, select the bootstrap account (edgestream@local.com), and either Disable or Delete it.

    ```{note}
    The management interface prevents self-deletion. You cannot delete or disable the account currently authenticated to the active dashboard session.
    ```

#Managing User Accounts
User lifecycles are administered under System → Users.

### Administrative Provisioning
Administrators can directly add, update, suspend, or remove users:

- Status Toggling: Deactivate active sessions immediately by toggling an account to Disabled without removing historical records.

- Deletion: Permanently removes the operator identity and revokes all active session tokens.

### Self-Registration Workflow
Self-registration can be toggled to accommodate enterprise onboarding workflows:

- Navigate to System → Settings → Advanced Settings.

- Locate the account_self_registration parameter and set it to enabled or disabled.

    ```{note}
    Enabling self-registration permits prospective users to register an identity, but **does not grant immediate dashboard access**. All self-registered accounts are created in a pending state and require explicit review and activation by an existing administrator under **System → Users**.
    ```

## Multi-Factor Authentication (MFA / TOTP)
EdgeStream Hub supports RFC 6238 Time-based One-Time Passwords (TOTP) compatible with authenticator applications such as Google Authenticator, 1Password, or Authy.

### Enabling TOTP
1. Navigate to System → Users and select the account to secure.

2. Open the MFA tab.

3. Scan the displayed QR code with your authenticator mobile app or password manager.

4. Enter the active 6-digit rolling verification code into the prompt.

5. The appliance validates the rolling token against its internal clock and enforces MFA for all subsequent login challenges upon successful verification.

## Emergency Recovery (CLI Break-Glass)
If administrative dashboard access or an authenticator device is lost, access can be recovered from the host terminal via the administrative recovery utility.

1. List Managed Dashboard Accounts
Run the command without arguments to enumerate all existing Web UI users:

    ```bash
    sudo /opt/edgestream-api/bin/reset_admin
    ```

2. Reset an Account Password
To override an account password:

    ```bash
    sudo /opt/edgestream-api/bin/reset_admin <username> '<new_password>'
    ```

3. Clear Multi-Factor Authentication
If an administrator is locked out due to a lost TOTP device, remove MFA enforcement while leaving the underlying password intact:

    ```bash
    sudo /opt/edgestream-api/bin/reset_admin --remove-mfa <username>
    ```

Once executed, the operator can sign in using their standard credentials and re-enroll their TOTP device under System → Users.