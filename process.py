log_file = open("um-server-01.txt")


def sales_reports(log_file):
    #looping through the um-server-01.txt file
    for line in log_file:
        #getting rid of white spaces at end of string
        line = line.rstrip()
        #slicing from position 0 to 3 not included
        day = line[0:3]
        #print('day is', day)
        #finding day that's equal to tuesday and if so print line
        if day == "Mon":
            print('line is what', line)


sales_reports(log_file)
