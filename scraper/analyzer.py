import google.generativeai as genai
import asyncio
import aiofiles

input_file_path = 'C:/Users/Felipe Ribeiro/Desktop/CR/ScraperAI-ProfessoresUFABC/scraper/data/raw/teacherData.txt'
output_file_path = 'C:/Users/Felipe Ribeiro/Desktop/CR/ScraperAI-ProfessoresUFABC/scraper/data/processed/teacherData.txt'

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 500,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

model = genai.GenerativeModel(
    model_name="tunedModels/scraper-v1",
    generation_config=generation_config,
    safety_settings=safety_settings
)

async def process_teacher(line):
    response = model.generate_content(line)
    return response.text

async def process_lines(input_lines, output_file_path):
    async with aiofiles.open(output_file_path, 'w', encoding='utf-8') as output_file:
        for i, line in enumerate(input_lines):
            output = await process_teacher(line)
            await output_file.write(output + "\n")
            print(output)
            if (i + 1) % 15 == 0:
                await asyncio.sleep(60)  

async def read_and_process_file(input_file_path, output_file_path, encoding='utf-8'):
    try:
        async with aiofiles.open(input_file_path, 'r', encoding=encoding) as input_file:
            input_lines = [line.strip() for line in await input_file.readlines()]
        await process_lines(input_lines, output_file_path)
    except UnicodeDecodeError as e:
        print(f"Error reading the file: {e}")
        print("Try a different encoding or check the file for encoding issues.")

if __name__ == "__main__":
    asyncio.run(read_and_process_file(input_file_path, output_file_path))