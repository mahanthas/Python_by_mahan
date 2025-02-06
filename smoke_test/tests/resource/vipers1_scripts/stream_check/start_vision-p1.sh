# WARN: Calling shell scripts is a security risk and shall not be done
#       for series. This script is only intended for development, and
#       will be migrated to startup.xml in the future.
export RBP_PARAM_ROOT_FOLDER='/m3/bosch/prk/rt_param/'
export LD_LIBRARY_PATH=/lib:/usr/lib:/opt/vrte/lib

cd /opt/bosch/prk/bin/

echo "Starting the root view publisher"
on -p 100f ./rvp-svc --cfg /opt/bosch/prk/etc/rvp_svc.cfg USE_STDOUT >/dev/null 2>&1 &
