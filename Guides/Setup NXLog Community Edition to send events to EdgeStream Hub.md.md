# Setup NxLog to send events to Edgestream Hub

## Edgestream Hub Configuration

Edit the system nxlog source in Configuration -> Sources or to create a new source select create and use Socket as the Type.

Set the toggle to Enabled.

Set the address to listen on. By default this is any address on the Edgestream Hub (0.0.0.0) and port 1514. Choose the default or select an available port.

Set the mode to TCP and Decoding.Codec to json.

Select a route\_label to identify this source for routing, such as **nxlog**.

Select **Update** or **Create** to save the settings. Next we will generate a self-signed certificate to encrypt the connection between the NxLog client and Edgestream Hub server.

### Generating TLS Certificates

The following commands will generate a certificate authority and self-signed certificates for this test scenario. For production systems use your organisations PKI infrastructure for certificates or a public authority.

#### Create Certificate Authority

Generate a private key file:
```
 openssl genrsa -out ca.key 4096
```
Generate a request and sign the key created in the previous step, provide values suitable for your environment:
```
openssl req -x509 -new -nodes -key ca.key -sha256 -days 1024 -out ca.pem
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:AU
State or Province Name (full name) [Some-State]:ACT
Locality Name (eg, city) []:Canberra
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Hypersec
Organizational Unit Name (eg, section) []:Infrastructure
Common Name (e.g. server FQDN or YOUR name) []:scenario.edestream-hub.local
Email Address []:support@hypersec.io
```

#### Create Edgestream-Hub NxLog Server Certificate

Run the following command to generate a certificate for your Edgestream-Hub NxLog receiver:
```
 openssl genrsa -out edgestream-hub-nxlog.key 4096
```
##### Generate a request:
```
openssl req -new -key edgestream-hub-nxlog.key -out edgestream-hub-nxlog.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:ACT
Locality Name (eg, city) []:Canberra
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Hypersec
Organizational Unit Name (eg, section) []:Infrastructure
Common Name (e.g. server FQDN or YOUR name) []:hub.edgestream-hub.local
Email Address []:support@hypersec.io

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```
In this example I did not provide a password which is optional.

Now we will sign the key using our certificate authority created above:
```

 openssl x509 -req -in edgestream-hub-nxlog.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out edgestream-hub-nxlog.crt -days 500 -sha256
```
##### Upload the Certificates

In the Web UI navigate to System -> Certificate Store and select Upload new file.

We will upload the following 3 files:
| File                     | Type                  |
| ------------------------ | --------------------- |
| ca.pem                   | Certificate Authority |
| edgestream-hub-nxlog.crt | Certificate           |
| edgestream-hub-nxlog.key | Private key           |

When completed, the keys will be listed in the Certificate Store:

![Certificate Store](..\images\nxlog_scenario_certificate_store.png "Certificate Store")

#### Configuring Certificates in NxLog Source

Go back into the NxLog source, Configuration -> Sources and click edit next to nxlog or the source you configured.

Under TLS set the following options:

![NxLog TLS Options](..\images\nxlog_scenario_nxlog_tls_options_1.png "NxLog TLS Options")

Select **Update** to save settings.

Note: In production Verify Hostname should be True.

#### Create Windows NxLog Client Certificates

Execute the following command to create client certificates for the windows hosts:
```
 openssl genrsa -out client-nxlog.key 4096
```
Generate a client request certificate:
```
openssl req -new -key client-nxlog.key -out client-nxlog.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:AU
State or Province Name (full name) [Some-State]:ACT
Locality Name (eg, city) []:Canberra
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Hypersec
Organizational Unit Name (eg, section) []:Infrastructure
Common Name (e.g. server FQDN or YOUR name) []:client.windows.local
Email Address []:support@hypersec.io

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```
Again in this scenario I haven't used a challenge password as it is optional.

Sign the client certificate using the certificate authority generated above:

```openssl x509 -req -in client-nxlog.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out client-nxlog.crt -days 500 -sha256```

### Installing NxLog

[Download NxLog community edition from the NxLog website](https://nxlog.co/products/nxlog-community-edition).

In this example I am downloading nxlog-ce-3.2.2329.msi for windows x86-64.

I am using C:\Program Files\nxlog as the installation location, adjust accordingly if you installed to a different directory.

Copy the client certificates and the certificate authority certificate to the C:\Program Files\nxlog\cert directory.

![File Manager](..\images\nxlog_scenario_nxlog_tls_windows_cert_dir.png "File Manager")

Edit the NxLog configuration file C:\Program Files\nxlog\conf\nxlog.conf

An example config that sends all events to the Edgestream-Hub running on IP Address 192.168.22.100:
```
Panic Soft
#NoFreeOnExit TRUE

define ROOT     C:\Program Files\nxlog
define CERTDIR  %ROOT%\cert
define CONFDIR  %ROOT%\conf\nxlog.d
define LOGDIR   %ROOT%\data

include %CONFDIR%\\*.conf
define LOGFILE  %LOGDIR%\nxlog.log
LogFile %LOGFILE%

Moduledir %ROOT%\modules
CacheDir  %ROOT%\data
Pidfile   %ROOT%\data\nxlog.pid
SpoolDir  %ROOT%\data

<Extension json>
    Module    xm_json
</Extension>

<Input windows_event_collect>
    Module      im_msvistalog
	Exec      to_json();
</Input>

<Output output_collector>
    Module om_ssl
    Host 192.168.22.100
    Port 1514
	CAFile         %CERTDIR%\ca.pem
	CertFile       %CERTDIR%\client-nxlog.crt
        CertKeyFile    %CERTDIR%\client-nxlog.key
	AllowUntrusted TRUE
    <Exec>
        $EventTime = integer($EventTime) / 1000000;
        to_json();
    </Exec>
</Output>

<Route 1>
    Path        windows_event_collect => output_collector
</Route>


```
In this example I'm allowing untrusted, do not use this in production unless you are aware of the security implications.

You can then restart the nxlog service and events will start flowing, check the nxlog log file if nothing is coming through.

## Edgestream-Hub Verification

You can view the statistics for the nxlog source in the Edgestream-Hub Event Flow monitor.

Navigate to Monitoring -> Event flow:

![Event Flow](..\images\nxlog_scenario_nxlog_event_monitor.png "Event Flow")

You can also run the command **vector top** on the Edgestream-Hub to see the event flow on the command line, or **vector tap to see** the raw events:

![Vector Tap](..\images\nxlog_scenario_nxlog_vector_top.png "Vector Tap")


