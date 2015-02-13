#Erich Chu
import datetime
import time
import csv

allnames = []
alltimes = []

def takeAttendance():
    fullname = raw_input('What is your name? ')
    seconds = time.time()
    currenttime = datetime.datetime.fromtimestamp(seconds).strftime('%Y-%m-%d %H:%M:%S')
    allnames.append(fullname)
    alltimes.append(currenttime)
    goagain = raw_input('Are there any more signins? (Y/N)')
    if goagain == "N" or goagain == "n":
        return False
    else: return True
def main():
    cont = True
    while cont == True:
        cont = takeAttendance()
    with open('attendance.csv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['Timestamp', 'Name'])
        for t, val in enumerate(allnames):
            csvwriter.writerow([alltimes[t], allnames[t]])
main()
