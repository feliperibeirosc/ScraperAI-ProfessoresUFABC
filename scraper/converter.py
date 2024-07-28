import csv

txt_file_path = 'C:/Users/Felipe Ribeiro/Desktop/CR/ScraperAI-ProfessoresUFABC/scraper/data/processed/teacherData.txt'
csv_file_path = 'C:/Users/Felipe Ribeiro/Desktop/CR/ScraperAI-ProfessoresUFABC/scraper/data/processed/teacherData.csv'

def process_txt_file(txt_file_path):
    data = []
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            if i + 2 < len(lines):
                name = lines[i].strip()
                university = lines[i + 1].strip()
                areas_of_interest = lines[i + 2].strip()
                data.append([name, university, areas_of_interest])
            else:
                print(f"Incomplete block detected starting at line {i}. Ignoring.")
    return data

def write_csv(data, csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Nome', 'Universidade', 'Areas de interesse'])
        writer.writerows(data)

data = process_txt_file(txt_file_path)
write_csv(data, csv_file_path)

print(f"CSV file '{csv_file_path}' created successfully!")
