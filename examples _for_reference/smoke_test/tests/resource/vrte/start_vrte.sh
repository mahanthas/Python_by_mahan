#!/bin/sh

# TODO Temp solution required for validation of UCM certificates - date set to 01/02/2024 00:00
# TODO This will be replaced with a PTP message when ready
date 020100002024 >/dev/null

## RouDi

#workaround related to starting Roudi TBD
#Typed memory workaround to carve out the iceoryx from normal user space RAM
POSIX_TYPED_MEMORY=/memory/ram/iceoryx /opt/aos/bin/roudi_roudi1 -m off &

## Network
route add -net 224.0.0.0/4 10.15.253.32
route add -net 224.0.0.0/4 10.1.0.32

route add -host 239.255.0.240 10.1.2.32
route add -host 239.255.2.241 10.1.2.32

route add -host 239.255.5.1 10.1.5.32

route add -host 235.5.23.0 10.15.254.32
route add -host 235.5.22.0 10.15.254.32
route add -host 225.5.23.1 10.15.254.32
route add -host 235.5.24.0 10.15.254.32
route add -host 235.5.24.1 10.15.254.32

route add -host 239.255.250.1 10.15.250.32
route add -host 239.15.250.0 10.15.250.32

# The ones below are all covered by the lines above
# Causing warnings in the console (File exists)
# route add -net 225.5.24.0/24 10.1.0.32
# route add -net 239.0.0.0/4 10.1.0.32

# Enable bridge with multicast filter
ifconfig bridge0 create

# Results in "port unreachable" frames

# Works fine
ifconfig bridge0 addm veth0
ifconfig bridge0 addm vlan2
sysctl -w net.link.bridge.mcf=1
ifconfig bridge0 mcfadd vlan2 01:00:5E:7F:00:F0
ifconfig bridge0 mcfadd vlan2 01:00:5E:7F:02:F1
ifconfig bridge0 mcfadd veth0 01:00:5E:7F:02:F1
ifconfig bridge0 mcfadd veth0 01:00:5E:7F:00:F0
ifconfig bridge0 up

## (v)GETK

IS_GETK_CONNECTED="$( pci-tool -v | grep "PMC-Sierra Inc" )"
if [[ -n "$IS_GETK_CONNECTED" ]] ; then
    # memory area used by etas-socketmanager
    ETAS_USE_TYPED_MEMORY=/memory/ram/iceoryx /opt/bosch/bin/etas-socketmanager -b 67108864 & # size of ETAS buffer
    #POSIX_TYPED_MEMORY=/memory/ram/iceoryx /opt/bosch/bin/mta_etas_getkp_gateway > /dev/shmem/GETK.log 2>&1 &
# TODO: Uncomment the else section to enable processmanager and vgetk gw
# else
    # /opt/bosch/bin/processmanager &
    # Disable mta_etas_vgetk_gateway stderr temporarily
    # on -p 1f /opt/bosch/bin/mta_etas_vgetk_gateway 2>/dev/null &
fi

## Compatibility

mkdir -p /dcp/ucm
mkdir -p /ota/ucm/scratchdir
mkdir -p /ota/ucm/ucminitialmanifests
mkdir -p /var/log/dltlogs

## VRTE

export LOGTRACEDEFAULTLOGLEVEL=info
export LOGTRACELOGMODE=network,console
export LOGTRACEPROCESSDESC="VRTE:EXM: daemon logging"
export LOGTRACEPROCESSID=EXM
export PROCESSIDENTIFIER=rb_exmd
export ECUCFG_ENV_VAR_ROOTFOLDER="/opt/vrte//exm-aap-execution-manager/etc/ecu-cfg"

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/vrte/lib

# TODO can be remove after EXM -DLT logging fix
rm /var/log/dlt/*
# Workaround to bind the the socket using proceeses into different cores
#sh /opt/bosch/prk/bin/update_prio_core_binding.sh >/dev/null 2>&1 &

# Development only
if [ -f "/nvm/bosch/startup/vrte_verbose" ]; then
    rm /nvm/bosch/startup/vrte_verbose
    #/opt/vrte/exm-aap-execution-manager/bin/rb-exmd -t 60000 2> /tmp/exm-err.log > /tmp/exm.log
else
    #/opt/vrte/exm-aap-execution-manager/bin/rb-exmd -t 60000 >/dev/null 2>/dev/null
fi
