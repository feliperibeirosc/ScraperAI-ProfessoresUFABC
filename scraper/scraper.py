import aiohttp
import asyncio
from bs4 import BeautifulSoup
import aiofiles

input_file_path = 'C:/Users/Felipe Ribeiro/Desktop/CR/ScraperAI-ProfessoresUFABC/scraper/data/raw/links.txt'
output_file_path = 'C:/Users/Felipe Ribeiro/Desktop/CR/ScraperAI-ProfessoresUFABC/scraper/data/raw/teacherData.txt'

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        return f'Error fetching {url}: {e}'

async def process_domain(session, domain):
    try:
        content = await fetch(session, domain)
        soup = BeautifulSoup(content, 'html.parser')

        heading_tag = soup.find('h1', class_='documentFirstHeading')
        heading_content = heading_tag.get_text(strip=True) if heading_tag else 'Tag <h1 class="documentFirstHeading"> not found'

        box_autor_tag = soup.find('div', class_='boxAutor')
        if box_autor_tag:
            content_between = []
            for sibling in heading_tag.find_all_next():
                if sibling == box_autor_tag:
                    break
                if sibling.name not in ['script', 'style']:
                    content_between.append(sibling.get_text(strip=True))

            full_content = ' '.join(content_between).strip()
        else:
            full_content = 'Tag <div class="boxAutor"> not found'

        return f'{{{heading_content} {full_content}}}'
 
    except Exception as e:
        return f'Error processing {domain}: {e}\n'

async def main():
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open(input_file_path, 'r', encoding='utf-8') as input_file:
            lines = [line.strip() for line in await input_file.readlines() if line.strip()]
        
        tasks = [process_domain(session, line) for line in lines]
        results = await asyncio.gather(*tasks)
        
        async with aiofiles.open(output_file_path, 'w', encoding='utf-8') as output_file:
            await output_file.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    asyncio.run(main())