import openpyxl
import csv
from pathlib import Path

# 1. Define your output path and raw data rows
output_file = Path("../../Project1_Top 50 Stocks Performance") / "FirstSemesterTop50.csv"

Number_tracker = 1

# Start cell, 6B (2nd Column)
# End column G (7th Column)
# End row 55
# Ordered column: No, Code, Stock Name, Amount of shares, Market Cap IDR (2 Decimal), Percentage (Due to rounding, this serves as approximation)

def content_loop(active_worksheet, months, w):
    global Number_tracker
    for r in range(6,56):
        row_content = []
        for c in range(2,8):
            current_content = active_worksheet.cell(r,c).value
            if c == 2:
                current_content = Number_tracker
                Number_tracker += 1

            if c == 7:
                current_content = float(round(current_content,2))

            if c == 6:
                current_content = float(round(current_content,2))

            if c == 5:
                current_content = int(current_content)

            row_content.append(current_content)

        row_content.append(months)

        w.writerow(row_content)


if __name__ == '__main__':
    with open("../Processed/FirstSemesterTop50.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(["No. ","Code","Stock Company Name","Amount of Shares","Market Cap IDR","Weight","Months"])

        for i in range(1,6):
            data = openpyxl.load_workbook(f"../Raw Files/top50_2026_0{i}.xlsx")
            curr = data.worksheets[0]
            content_loop(curr,i,writer)