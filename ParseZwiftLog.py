#!/usr/bin/env python3
# 0.1  John McManus 21/05/2020 - initial version
# 0.2  John McManus 22/05/2020 - path variable added from code provided by David A Desrosiers



import os
import string
import time

printable = {"Lu", "Ll"}

home = os.path.expanduser("~")
zwift_data = os.path.join(home, "OneDrive","Documents2", "Zwift", "Logs")
zwift_logfile = os.path.join(zwift_data, "Log.txt")

# Tune this to your individual output path, OneDrive, local, Dropbox or other
output_path = os.path.join(home, "OneDrive", "Documents2", "ZwiftStreaming", "Overlays", "Dynamic")
rideontotalfile = os.path.join(output_path, "RideOnTotals.txt")
notificationfile = os.path.join(output_path, "Notify.txt")

# logfile = 'C:\\Users\\JohnMcManus\\OneDrive\\Documents2\\Zwift\\Logs\\Log.txt'
# rideontotalfile = 'C:\\Users\\JohnMcManus\\OneDrive\\Documents2\\ZwiftStreaming\\Overlays\\Dynamic\\RideOnTotals.txt'
# notificationfile = 'C:\\Users\\JohnMcManus\\OneDrive\\Documents2\\ZwiftStreaming\\Overlays\\Dynamic\\Notify.txt'
# HUD_Notify HUD_Notify: A.Loake U12 says Ride On!
# ;HUD_Notify: D.Saglia (Van Aert Fan) says Ride On!
# ;Chat: Sutts TBRðŸ§˜ðŸ»â€â™‚ï¸ðŸƒ 713849 (World): Thanks mark. Robin. Apologies for terrible lead out
# ;Chat: NEWLIN (VAMPIRE CYCLING) 598462 (World): hey
# print(logfile)
# Chat: costantino 1833617 (World): ciao Eric
# Chat: Kit 44328 (World): We always back here brother
# Chat: 931740 (Paddock): Anyone else gonna do the 2hr run?

notificationLists = []
nottotal = 0


def filter_non_printable(str):
    str = "".join([x for x in str if x in string.printable])
    return str


def parseline(line):
    if line.find("Ride On!") != -1 and line.find("HUD_Notify:") != -1:
        start_sub = line.find("HUD_Notify:")
        end_sub = line.find("says")
        start_sub = start_sub + 11
        end_sub = end_sub - 1
        rideonname = line[start_sub:end_sub]
        rideonname = filter_non_printable(rideonname)
        notificationLists.append("Thanks:" + rideonname)
        global nottotal
        nottotal = nottotal + 1
        updatetotalfile(str(nottotal))

    return 0


def process_notification():
    for n in notificationLists[::-1]:
        print(":")
        print(n)
        updatenotefile(n)
        time.sleep(2)

    return 0


def updatenotefile(note):
    print(note)
    try:
        with open(notificationfile, "w", encoding="latin-1") as outfile:
            outfile.write(note)

            outfile.close()
    except IOError:
        print(print("ERROR:NOTIFYFILE"))

    return 0


def updatetotalfile(tot):
    print(tot)

    try:
        with open(rideontotalfile, "w", encoding="latin-1") as outfile:
            outfile.write(tot)
            outfile.close()
    except IOError:
        print("ERROR:TOTALFILE")

    return 0


def process(new_data):
    line = ""
    for currentchar in new_data:
        if currentchar == "\n":
            parseline(line)
            line = ""
        line = line + currentchar
    return 0


last_position = 0
notificationLists.append("")
updatetotalfile("")
while True:  # loop forever
    with open(zwift_logfile, encoding="latin-1") as f:
        f.seek(last_position)
        new_data = f.read()
        last_position = f.tell()
    process(new_data)
    process_notification()
    time.sleep(10)  # sleep some amount of time
    print("." * 21)
