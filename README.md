# ZwiftLogRideOns
Python Script that reads active Zwift log counting RideOns and extracts who gave the Rideon

The Scrip needs python installed!

To use:
modify the three variable to match your setup

Variables

The actual zwift logfile
zwift_logfile = os.path.join(zwift_data, "Log.txt")

Where you want the rideon totals to be written to
rideontotalfile = os.path.join(output_path, "RideOnTotals.txt")

Where you want the name to be written to
notificationfile = os.path.join(output_path, "Notify.txt")



What I use this for ?
I use OBS studio and montior RidoOnTotals.txt and Notify.txt. The values are display on the live stream
you can see an example here https://youtu.be/YD8tGdh5S6E?t=1215
RideOn Total at the top
Notift at the bottom
