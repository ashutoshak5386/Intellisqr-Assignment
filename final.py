import tabula
import csv

# Specify the path to your PDF file
pdf_path = "yo.pdf"

# Extract tables 1, 2, and 3 from the PDF into a list of pandas DataFrames
tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)[0:3]

# Open a CSV file in write mode
with open("tables_1_2_3.csv", "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write each table to the CSV file
    for table in tables:
        # Extract the data from the table
        data = table.values.tolist()
        
        # Format each row and write it to the CSV file
        for row in data:
            csv_writer.writerow([f'{" "*2}{row[0]}{" "*5}{row[2]}{" "*5}{"pan of"}{" "*5}{row[1]}'])

        

        # Add an empty row between tables
        csv_writer.writerow([])

print("Tables 1, 2, and 3 saved as tables_1_2_3.csv with the desired formatting")
