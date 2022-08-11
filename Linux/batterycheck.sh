#! /bin/bash -
LOG_FILE="SYSLOGS.log"

main() {
	# your script here
	echo
	echo -n "Date Time: "
	date
	echo "Advanced Configuration and Power Interface:"
	acpi -V
}

# channel 2 - stderr, channel 1 - stdout
main "$@" 2>&1 | tee -a "$LOG_FILE"


