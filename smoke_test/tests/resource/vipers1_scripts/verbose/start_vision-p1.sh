echo "start_vision-p1.sh script called..."

export RBP_PARAM_ROOT_FOLDER='/m3/bosch/prk/rt_param/'
export LD_LIBRARY_PATH=/lib:/usr/lib:/opt/vrte/lib

cd /opt/bosch/prk/bin/

echo "Starting rootviewpublishers"
on -p 100f ./rvp-svc --cfg /opt/bosch/prk/etc/rvp_svc.cfg VERBOSE USE_STDOUT > /opt/bosch/prk/bin/log_rvpsvc.txt 2>&1 &
