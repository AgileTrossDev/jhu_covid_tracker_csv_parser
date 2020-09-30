import csv
import sys

# Number of days that will be in the output
look_back_days = 30

# Column range where first date is recorded
start_col_to_remove = 11;

# Use command line parameters to set input/output files
input_file = sys.argv[1];
output_file = sys.argv[2];

# Open file to be written
outF = open(output_file, "w")

# Display what is about to happen
print "Parser started"
print "Parsing file: " + input_file
print "Creating file: " + output_file

# Open the csv file and then Iterate over each line 
with open(input_file, 'rb') as csvfile:
     jhu_covid_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
     for row in jhu_covid_reader:
  
         # Calculate what is the last col in range to be removed
         end_col_to_remove = len(row)-look_back_days

         # Remove range of columns
         del row[start_col_to_remove:end_col_to_remove]
         
         # Join the row back into a string delimeted by a comma and write to file
         outF.write(",".join(row))
  
         # Mark new line
         outF.write("\n")

# Close output file         
outF.close()

print "Parser exiting..."
