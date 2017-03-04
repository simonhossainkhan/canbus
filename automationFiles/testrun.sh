#!/usr/bin/env bash

echo "Starting script"

echo "Getting WiFi SSID"
WIFISSDin=$(iwgetid -r)
echo $WIFISSDin
connected=1

echo "Waiting for Bluetooth to boot..."
sleep 1

echo "Beginning bluetooth commands"
bluetoothctl << EOF
power on
pair 00:1D:A5:00:04:34
connect 00:1D:A5:00:04:34
trust 00:1D:A5:00:04:34
EOF
sleep 1
echo "Bluetooth commands finished"

echo "Check for bluetooth connection"
if hcitool dev | grep '00:1D:A5:00:04:34';then
  echo "Bluetooth OBDII Reader connected"
else
  echo "Bluetooth not connected. Exiting."
  exit 0
fi

echo "Starting RFCOMM"
rfcomm_connect.sh &
RFID=$!
echo "RFCOMM PID"
echo $RFID
sleep 1
echo "RFCOMM connected"

echo "Begin recording"
python /home/pi/pyobd-pi/obd_recorder.py &
RID=$!
echo "Recording PID"
echo $RID

echo "Beginning Run"
while [ $connected==1 ]
do
  echo "Connected"
  TESTCON=$(iwgetid -r)
  if [[ "$TESTCON" == "$WIFISSIDin" ]];then
    $connected=1
  else
    $connected=0
  fi
done
while [ $connected==0 ]
do
  echo "Running"
  if [[ "$(iwgetid -r)" == "" ]];then
    $connected=0
  elif [[ "$(iwgetid -r)" == "$WIFISSIDin" ]];then
    $connected=1
  fi
done
echo "Ending Run"

echo "Releasing RFCOMM"
rfcomm_disconnect.sh &
sleep 1
echo "Released RFCOMM"


echo "Ending child process"
for child in $(jobs -p); do
  echo kill "$child" && kill "$child"
done
wait $(jobs -p)
echo "Finished child process"

echo "List log file"
log=$(ls /home/pi/pyobd-pi/log)
echo $log

echo "Uploading file..."
python upload_log.py $log

echo "Deleting all log files"
rm /home/pi/pyobd-pi/log/*
echo "Deleted files"

echo "End of script"
exit 0