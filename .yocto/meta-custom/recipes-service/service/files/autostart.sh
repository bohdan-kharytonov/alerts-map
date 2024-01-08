SCRIPT="/usr/bin/script.sh"

USER="root"

case "$1" in
  start)
    echo "Starting Alerts map script"
    DISPLAY=":0" /bin/bash -c "$SCRIPT" $USER
    ;;
  stop)
    echo "Stopping Alerts map script"
    ;;
  restart)
    echo "Restarting Alerts map script"
    $0 stop
    sleep 2
    $0 start
    ;;
  *)
    echo "Usage: $0 {start|stop|restart}"
    exit 1
    ;;
esac

exit 0