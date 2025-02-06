echo "start_vision-p2.sh script called..."

export RBP_PARAM_ROOT_FOLDER='/m3/bosch/prk/rt_param/'
export LD_LIBRARY_PATH=/lib:/usr/lib:/opt/vrte/lib

cd /opt/bosch/prk/bin/

echo "Starting the visu app"
on -p 100f ./adasvisuservice VERBOSE USE_STDOUT > /opt/bosch/prk/bin/log_adasvisuservice.txt 2>&1 &

echo "wait for 1s to start viper-s1-gateway"
sleep 1

echo "Starting the viper s1 gateway"
on -p 100f ./viper-s1-gateway --cfg /opt/bosch/prk/etc/adascomp.cfg VERBOSE USE_STDOUT > /opt/bosch/prk/bin/log_adascomp.txt 2>&1 &

echo "Waiting for binaries to execute"

echo "completing the Vipers1 process ...."
