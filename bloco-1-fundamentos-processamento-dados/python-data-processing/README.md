# TP1 – Python para Processamento de Dados

Performance Test 1. Covers advanced string operations: slicing, indexing, `split()`, `join()`, `find()`, `replace()`, `strip()`, f-string formatting, and ASCII manipulation.

---

## Exercises

### Ex01 – strip() (Email Sanitizer)

Remove leading and trailing whitespace from an email address collected via an online form to ensure valid delivery in marketing campaigns.

### Ex02 – String Formatting (Receipt Generator)

Generate a formatted purchase receipt combining a customer's name and a transaction value, displaying the amount with exactly two decimal places.

### Ex03 – split() (Record Parser)

Split a semicolon-delimited text record into individual fields and print the total field count followed by each field on a separate line.

### Ex04 – join() (Logistics ID Builder)

Assemble a unique package identifier by joining a distribution center code, product category code, and batch number with a hyphen separator.

### Ex05 – Slicing (Badge Code Interpreter)

Extract the employee ID, department code, and shift indicator from a fixed-format badge string using slicing, then map the shift character to its full name.

### Ex06 – split(), strip() and join() (Report Formatter)

Convert a semicolon-delimited data line into a slash-separated format by splitting fields, stripping each one, and rebuilding the string with a `for` loop.

### Ex07 – startswith() and endswith() (File Upload Validator)

Validate a filename for server upload by checking that it starts with the required department prefix and ends with an allowed extension (`.py` or `.txt`).

### Ex08 – Indexing and Slicing (Game Macro Interpreter)

Parse an 8-character game command macro using positional indexing and slicing to extract coordinates, action code, action type, and defense/delay indicator.

### Ex09 – replace() (Forum Text Sanitizer)

Iterate over a list of offensive terms and replace each one with a corresponding asterisk sequence in a student forum message, applying substitutions sequentially.

### Ex10 – f-string Formatting (Daily Cash Closing Report)

Calculate net revenue, total expenses, and final balance from three input values, then render a right-aligned tabular financial report using f-strings with field width specifiers.

### Ex11 – find() (DNA Codon Locator)

Locate the first occurrence of a target codon within a DNA sequence string using `find()` and print its index, or `-1` if not found.

### Ex12 – split() and join() (Participant List Reformatter)

Convert a comma-separated list of names into a slash-separated format using `split()` to parse and `join()` to reconstruct the string.

### Ex13 – .format() (IPv4 Address Standardizer)

Standardize a masked IPv4 address that may use hyphens or underscores as delimiters and include a subnet mask suffix, replacing invalid or out-of-range octets with zero.

### Ex14 – find(), rfind() and rindex() (Directory Path Analyzer)

Analyze a file path string to locate the first and last `/` separator and classify the final filename segment as an executable or a common file.

### Ex15 – strip() and lstrip() / rstrip() (Transcription Fragment Cleaner)

Apply a four-step cleaning pipeline to a raw transcription fragment: remove surrounding whitespace, strip leading/trailing punctuation, remove noise markers (`^`, `~`), and strip section delimiters (`[`, `]`).

### Ex16 – ord() and chr() (Caesar Cipher Decryptor)

Decrypt a Caesar-encrypted message where the shift key is encoded as the number of trailing dots, restoring only words longer than three characters using ASCII arithmetic.

---

# TP1 – Python para Processamento de Dados

Teste de Performance 1. Cobre operações avançadas com strings: fatiamento, indexação, `split()`, `join()`, `find()`, `replace()`, `strip()`, formatação com f-string e manipulação de ASCII.

---

## Exercícios

### Ex01 – strip() (Higienizador de E-mail)

Remover espaços em branco do início e do fim de um endereço de e-mail coletado via formulário online para garantir a entrega correta em campanhas de marketing.

### Ex02 – Formatação de Strings (Gerador de Recibo)

Gerar um recibo de compra formatado combinando o nome do cliente e o valor da transação, exibindo o montante com exatamente duas casas decimais.

### Ex03 – split() (Parser de Registro)

Dividir um registro textual delimitado por ponto e vírgula em campos individuais e imprimir a quantidade total de campos seguida de cada campo em uma linha separada.

### Ex04 – join() (Montador de ID Logístico)

Montar um identificador único de pacote unindo o código do centro de distribuição, o código da categoria do produto e o número do lote com hífen como separador.

### Ex05 – Fatiamento (Interpretador de Crachá)

Extrair o código interno do funcionário, o código do setor e o indicador de turno de uma string de crachá em formato fixo usando fatiamento, e mapear o caractere do turno para seu nome completo.

### Ex06 – split(), strip() e join() (Formatador de Relatório)

Converter uma linha de dados delimitada por ponto e vírgula para um formato separado por barras, dividindo os campos, limpando cada um e reconstruindo a string com um laço `for`.

### Ex07 – startswith() e endswith() (Validador de Upload de Arquivo)

Validar um nome de arquivo para upload no servidor verificando se ele começa com o prefixo obrigatório do departamento e termina com uma extensão permitida (`.py` ou `.txt`).

### Ex08 – Indexação e Fatiamento (Interpretador de Macro de Jogo)

Interpretar uma macro de comando de jogo com 8 caracteres usando indexação posicional e fatiamento para extrair coordenadas, código da ação, tipo da ação e indicador de defesa/atraso.

### Ex09 – replace() (Higienizador de Texto do Fórum)

Percorrer uma lista de termos ofensivos e substituir cada um pela sequência de asteriscos correspondente em uma mensagem do fórum estudantil, aplicando as substituições sequencialmente.

### Ex10 – Formatação com f-string (Demonstrativo de Fechamento de Caixa)

Calcular receita líquida, total de despesas e saldo final a partir de três valores de entrada e renderizar um relatório financeiro tabular com alinhamento à direita usando f-strings com especificadores de largura de campo.

### Ex11 – find() (Localizador de Códon de DNA)

Localizar a primeira ocorrência de um códon alvo em uma sequência de DNA usando `find()` e imprimir seu índice, ou `-1` caso não seja encontrado.

### Ex12 – split() e join() (Reformatador de Lista de Participantes)

Converter uma lista de nomes separados por vírgula para um formato separado por barras usando `split()` para separar e `join()` para reconstruir a string.

### Ex13 – .format() (Padronizador de Endereço IPv4)

Padronizar um endereço IPv4 mascarado que pode usar hífens ou sublinhados como delimitadores e incluir sufixo de máscara de sub-rede, substituindo octetos inválidos ou fora do intervalo por zero.

### Ex14 – find(), rfind() e rindex() (Analisador de Caminho de Diretório)

Analisar uma string de caminho de arquivo para localizar o primeiro e o último separador `/` e classificar o segmento final do nome do arquivo como executável ou arquivo comum.

### Ex15 – strip() e lstrip() / rstrip() (Limpador de Fragmento de Transcrição)

Aplicar um pipeline de limpeza em quatro etapas a um fragmento bruto de transcrição: remover espaços nas bordas, retirar pontuação inicial/final, remover marcadores de ruído (`^`, `~`) e retirar delimitadores de seção (`[`, `]`).

### Ex16 – ord() e chr() (Decriptador de Cifra de César)

Decriptar uma mensagem cifrada por César em que a chave de deslocamento é codificada como o número de pontos finais, restaurando apenas palavras com mais de três caracteres usando aritmética ASCII.
