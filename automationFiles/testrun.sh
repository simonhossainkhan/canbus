#!/usr/bin/env bash

relativePath="/home/pi/Documents/Github/canbus/automationFiles/"
rfcommStart="rfcomm_connect.sh"
rfcommEnd="rfcomm_disconnect.sh"
uploadLog="upload_log.py"


echo "Starting script"
sleep 10
echo "Getting WiFi SSID"
WIFISSIDin=$(iwgetid -r)
echo $WIFISSDin
connected=1

sleep 1

echo "Starting RFCOMM"
$relativePath$rfcommStart &
RFID=$!
echo "RFCOMM PID"
echo $RFID
sleep 4
echo "RFCOMM connected"

echo "Waiting for Bluetooth to boot..."
sleep 1

echo "Beginning bluetooth commands..."
bluetoothctl << EOF
power on
pair 00:1D:A5:00:04:34
connect 00:1D:A5:00:04:34
trust 00:1D:A5:00:04:34
EOF
sleep 5
echo "Bluetooth commands finished"

echo "Check for bluetooth connection"
if hcitool con | grep '00:1D:A5:00:04:34';then
  echo "Bluetooth OBDII Reader connected"
else
  echo "Bluetooth not connected"
  echo "Releasing RFCOMM"
  $relativePath$rfcommEnd &
  sleep 1
  echo "Released RFCOMM"
  echo "Exiting"
  exit 0
fi

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
    connected=1
  elif [[ -z "$TESTCON" ]];then
    connected=0
    break
  fi
done
while [ $connected==0 ]
do
  echo "Running"
  TESTCON=$(iwgetid -r)
  if [[ -z "$TESTCON" ]];then
    connected=0
  elif [[ "$TESTCON" == "$WIFISSIDin" ]];then
    connected=1
    break
  fi
done
echo "Ending Run"

echo "Releasing RFCOMM"
$relativePath$rfcommEnd &
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
python $relativePath$uploadLog $log

echo "Deleting all log files"
rm /home/pi/pyobd-pi/log/*
echo "Deleted files"

echo "End of script"
exit 0