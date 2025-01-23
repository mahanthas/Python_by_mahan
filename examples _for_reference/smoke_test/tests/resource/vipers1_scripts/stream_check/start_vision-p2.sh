# WARN: Calling shell scripts is a security risk and shall not be done
#       for series. This script is only intended for development, and
#       will be migrated to startup.xml in the future.
export RBP_PARAM_ROOT_FOLDER='/m3/bosch/prk/rt_param/'
export LD_LIBRARY_PATH=/lib:/usr/lib:/opt/vrte/lib:/opt/bosch/lib:/opt/bosch/prk/lib

cd /opt/bosch/prk/bin/

echo "Starting the adasvisuservice"
on -p 80f -C5 -C6 -C7 ./adasvisuservice USE_STDOUT >/dev/null 2>&1 &

sleep 1

echo "Starting the viper s1 gateway"
on -p 80f -C5 -C6 -C7 ./viper-s1-gateway --cfg /opt/bosch/prk/etc/adascomp.cfg USE_STDOUT >/dev/null 2>&1 &

echo "wait for 1s before start rvp-chmsl-tg"
sleep 1

echo "starting rvp-chmsl"
on -p 120f -C5 -C6 -C7 ./rvp-chmsl-tg --cfg /opt/bosch/prk/etc/rvp_chmsl_tg.cfg USE_STDOUT > /dev/null 2>&1 &
