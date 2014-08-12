nagios-plugin-citrix-xml
========================
A simple Nagios plugin to check Citrix XML Service response for a published application.

Example usage:
```
check_citrix-xml -H citrixxml1.local -a "Internet Explorer"
```

Tested on XenApp 6.5. Might be very incomplete as test is based on a simple tcpdump.
