import gspread
import os
from datetime import date


## google sheets implementation ##

def update_spreadsheet(tests):
   
   # log into google
   gc = gspread.service_account(filename=os.path.join(os.path.dirname(__file__), '../googlesecret.json'))

   # get the desired spreadsheet
   worksheet = gc.open('McGregor Testing').sheet1

   # get today's date
   today = date.today()
   day = today.strftime("%B %d, %Y")

   # loop through the tests array
   for test in tests:

      # append the new object information to the very last row in the sheet
      worksheet.append_row([ test[0], test[1], test[2], day ])