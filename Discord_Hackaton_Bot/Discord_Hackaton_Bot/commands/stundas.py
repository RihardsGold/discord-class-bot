import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pathlib import Path

def get_schedule(day):
    current_dir = Path(__file__).parent
    
    credentials_file = current_dir / 'Google_Api_Json_File_Name.json' # <- Google API json file. (Stored in the same directory because I had problems if I tried to move it. Not sure why and gave up. If it works, why fix it, right?)


    scope = ['https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(creds)


    sheet_url = 'https://docs.google.com/spreadsheets/d/1wyQulaigwo3-MqHwZYtB7Tk8UvLe6el8rCP0J_sv2VA/edit?usp=sharing'  # Your Google Sheets URL.
    sheet = client.open_by_url(sheet_url)

    the_day = []
    lessons = []

    # Fetch data based on the chosen day
    if day.lower() == "pirmdiena":
        worksheet = sheet.worksheet('pirmdiena') #sheet.worksheet names are not uniform because they aren't in the google docs file. (┬┬﹏┬┬)
        cell_data = worksheet.acell('A2').value
        the_day.append(cell_data)

        cell_range = worksheet.range('N44:N51')
        for cell in cell_range:
            lessons.append(cell.value)
    elif day.lower() == "otrdiena":
        worksheet = sheet.worksheet('Otrdiena')
        cell_data = worksheet.acell('A2').value
        the_day.append(cell_data)

        cell_range = worksheet.range('N44:N51')
        for cell in cell_range:
            lessons.append(cell.value)
    elif day.lower() == "trešdiena":
        worksheet = sheet.worksheet('Trešdiena')
        cell_data = worksheet.acell('A2').value
        the_day.append(cell_data)

        cell_range = worksheet.range('N44:N51')
        for cell in cell_range:
            lessons.append(cell.value)
    elif day.lower() == "ceturtdiena":
        worksheet = sheet.worksheet('ceturtdiena')
        cell_data = worksheet.acell('A2').value
        the_day.append(cell_data)

        cell_range = worksheet.range('N44:N51')
        for cell in cell_range:
            lessons.append(cell.value)
    elif day.lower() == "piektdiena":
        worksheet = sheet.worksheet('Piektdiena')
        cell_data = worksheet.acell('A2').value
        the_day.append(cell_data)

        cell_range = worksheet.range('N44:N51')
        for cell in cell_range:
            lessons.append(cell.value)

    return the_day, lessons 
