#!/bin/sh

# TODO Temp solution required for validation of UCM certificates - date set to 01/02/2024 00:00
# TODO This will be replaced with a PTP message when ready
date 020100002024 >/dev/null

## RouDi

#workaround related to starting Roudi TBD
#Typed memory workaround to carve out the iceoryx from normal user space RAM
POSIX_TYPED_MEMORY=/memory/ram/iceoryx /opt/app/bin/roudi_roudi1 -m off &

## Network
echo "Setting up packet filter ..."

/sbin/pfctl -e -f /etc/pf.conf
if [ $? -ne 0 ]; then
    echo "VRTE: failed to setup packet filter"
fi

echo "Setting up packet filter anchor vrte_pf"
/sbin/pfctl -a vrte_pf -f /etc/pf.conf.d/vrte_pf.conf
if [ $? -ne 0 ]; then
    echo "VRTE: failed to setup packet filter anchor vrte_pf"
fi

route add -net 224.0.0.0/4 192.168.2.33
route add -net 224.0.0.0/4 10.1.0.32
route add -net 225.5.23.1/24 10.1.0.32

# The ones below are all covered by the lines above
# Causing warnings in the console (File exists)
# route add -net 225.5.24.0/24 10.1.0.32
# route add -net 239.0.0.0/4 10.1.0.32

## (v)GETK

IS_GETK_CONNECTED="$( pci-tool -v | grep "PMC-Sierra Inc" )"
if [[ -n "$IS_GETK_CONNECTED" ]] ; then
    # memory area used by etas-socketmanager
    ETAS_USE_TYPED_MEMORY=/memory/ram/iceoryx /opt/bosch/bin/etas-socketmanager -b 67108864 & # size of ETAS buffer
    POSIX_TYPED_MEMORY=/memory/ram/iceoryx /opt/bosch/bin/mta_etas_getkp_gateway > /dev/shmem/GETK.log 2>&1 &
else
    #/opt/bosch/bin/processmanager &
    # Disable mta_etas_vgetk_gateway stderr temporarily
    #on -p 1f /opt/bosch/bin/mta_etas_vgetk_gateway 2>/dev/null &

## Compatibility

mkdir -p /dcp/ucm

## VRTE

export LOGTRACEDEFAULTLOGLEVEL=info
export LOGTRACELOGMODE=network,console
export LOGTRACEPROCESSDESC="VRTE:EXM: daemon logging"
export LOGTRACEPROCESSID=EXM
export PROCESSIDENTIFIER=rb_exmd
export ECUCFG_ENV_VAR_ROOTFOLDER="/opt/vrte//exm-aap-execution-manager/etc/ecu-cfg"

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/vrte/lib

#/opt/vrte/exm-aap-execution-manager/bin/rb-exmd -t 60000 >/dev/null 2>/dev/null
# /opt/vrte/exm-aap-execution-manager/bin/rb-exmd -t 60000 2> /tmp/exm-err.log > /tmp/exm.log &
