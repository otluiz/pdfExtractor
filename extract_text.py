import os
from PyPDF2 import PdfReader

# Função para encontrar o primeiro arquivo PDF correspondente
def find_first_pdf(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Função para extrair texto de um PDF
def extract_text_from_pdf(pdf_path, start_section=None):
    text = ""
    start_collecting = start_section is None
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        for page in range(num_pages):
            page_text = reader.pages[page].extract_text()
            if start_section and start_section in page_text:
                start_collecting = True
            if start_collecting:
                text += page_text
    return text

# Nome do arquivo PDF
filename = "cbic2023_artigo14.pdf"
# Caminho inicial para a busca
search_path = "/home"

# Procurar pelo primeiro arquivo PDF
pdf_path = find_first_pdf(filename, search_path)

# Perguntar ao usuário se deseja pular para uma seção específica
start_section = input("Deseja pular para uma seção específica? (Digite o nome da seção ou pressione Enter para começar do início): ")

if pdf_path:
    print(f"Arquivo encontrado em: {pdf_path}")
    pdf_text = extract_text_from_pdf(pdf_path, start_section)
    
    # Perguntar ao usuário se deseja exibir todo o texto ou salvar em um arquivo
    user_choice = input("Deseja exibir todo o arquivo, ecolha (E) ou salvar em um arquivo em formato texto plano (S)? (Digite 'E' para exibir ou 'S' para salvar um txt): ").strip().upper()
    
    if user_choice == 'E':
        print(pdf_text)
    elif user_choice == 'S':
        output_filename = pdf_path.split(os.sep)[-1].replace('.pdf', '.txt')
        with open(output_filename, 'w') as output_file:
            output_file.write(pdf_text)
        print(f"Texto extraído salvo em: {output_filename}")
    else:
        print("Opção inválida. Saindo do programa.")
else:
    print(f"Arquivo {filename} não encontrado no caminho {search_path}.")
