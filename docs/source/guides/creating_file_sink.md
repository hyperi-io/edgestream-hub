# File Sink

File sinks should be configured to write to an external storage device using a cifs or nfs share, and only write locally during testing.

Select create in the top right corner.

## Core settings

Use a suitable name for the sink, in this example we will use the sink **Name:** **local\_test\_sink**.

In the **Type** dropdown menu select **File**.

The essential fields are Path and Encoding Codec. The path determines the directory and filename used for writing events, and the encoding codec specifies the format the events will be written in. The vector user must have suitable permission to write to the destination location.

The path name can utilise vector's templating scheme to write files using attributes of the event.

## Events and Metrics

Under Events and Metrics select the sources you want written out to this sink. You can select this as a fallback sink, which means any event or metric sources without a sink configured will be written to this as a catch all.

Note: events and metrics can be delivered to any number of sinks configured, however only 1 sink can be a fallback. Setting this removes the fallback setting of any existing sink.
