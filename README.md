# Análise e Enriquecimento de Dados de Clientes

### Objetivo
**Analisar e enriquecer dados de clientes** de um arquivo `.csv` fazendo o tratamento e complementação dos dados obedecendo regras próprias do projeto e acesso a APIs externas. E finalizar com a geração de arquivo `.json` e **relatórios estatísticos** sobre os dados.
> Desenvolvido como indicação de projeto final do módulo de **Programação orientada a Objetos** do programa **NExT - CESAR School**.

---

### 🔶 Funcionalidades Principais

- Leitura de um arquivo `.csv` com dados brutos de clientes

- Tratamento dos dados:

    - Nome (iniciais maiúsculas e separação de nomes considerando preposição na composição)
    - Celular (formatação com DDD e dígito 9 - adicionar se necessário)
    - CPF (formatação e validação seguindo regras da Receita Federal)
    - CEP (formatação e e busca de endereço com API ViaCEP)

- Enriquecimento de dados usando as APIs:

    - **ViaCEP** para buscar bairro, cidade, estado e DDD do cliente
    - **Genderize.io**, **GenderAPI.io** e **Gender-API.com** para inferência de gênero pelo primeiro nome do cliente

- Geração de arquivo de saída `users.json` com os dados processados

- Relatórios de análise usando `pandas` exibidos no console:
    - Distribuição de gênero (%)
    - Distribuição geográfica (% por região)
    - Qualidade dos dados (erros em nome, CEP, CPF e celular)
    - Interesses gerais e principais por gênero (%)

---

### 📂 Estrutura de Diretórios

```
analise_dados/
│
├── data/                       # Arquivos de entrada
│   └── lista_clientes.csv      
|
├── output/                     # Arquivos de saída
│   └── users.json      
|
├── src/                        # Código-fonte
│   ├── models/                 # Classes base (Pessoa, CPF, Endereço)
│   ├── repo/                   # Leitura/gravação de arquivos (csv e json)
│   ├── services/               # Requisições a APIs externas (CEP, Gênero)
│   ├── controllers/            # Lógica de controle e fluxo
│   ├── reports/                # Geração de relatórios com Pandas
│   └── main.py                 
│
├── .env                        # Variáveis de ambiente (não versionado)
|
└── tests/                      # Testes unitários (em andamento...)
```
---


### ⚙️ Requisitos
- Python 3.10+
- Conexão com internet
- Bibliotecas requests, pandas e python-dotenv

**Instale as dependências do projeto com:**
```bash
pip install -r requirements.txt
```

---

## ▶️ Como executar o projeto?

### 1. **Configure as chaves de APIs**

O sistema usa 2 APIs externas que necessitam de uma chave de usuário, então elas devem estar configuradas para o programa garantir todas as funcionalidades.

- Crie um arquivo `.env` na pasta raiz (veja na estrutura do projeto), e escreva o seguinte:

```env
# Chave de GenderAPI.io
API_KEY_IO = 'SuaChaveAqui'

# Chave Gender-API.com
API_KEY_COM = 'SuaChaveAqui'
```

- Coloque sua chave de cada API no lugar de SuaChaveAqui
- Dá para obter as chaves gratuitamente nos sites:
    - [https://genderapi.io](https://genderapi.io)
    - [https://gender-api.com](https://gender-api.com)

> ⚠️ ATENÇÃO:
> - Se as chaves não forem configuradas, a única API de gênero que funcionará corretamente é a **Genderize.io** (opção 1 do programa)

### 2. **Execute o projeto a partir da raiz:**

Como o projeto possui uma estrutura com várias camadas, utiliza muitos imports. A recomendação é chamar a execução principal pelo terminal:

```bash
python -m src.main
```
---

### ⚠️ Limitações

- As APIs de inferência de gênero possuem limite de requisições gratuitas.

- Caso atinja o limite, as requisições podem falhar ou retornar dados incompletos (análises sem gênero)

### ✅ Melhorias futuras

- Implementar testes unitários (cobertura mínima de 80%)
- Definir e lançar erros personalizados para as validações de CPF, celular, etc.
- Salvar os relatórios em arquivos de saída
- Aumentar a variedade de relatórios gerados
- ...



### 📌 Observações e Aprendizados
- O projeto foi desenvolvido com foco em boas práticas de POO e separação de responsabilidades de cada camada, **mesmo sendo um projeto para aprendizado**
- As decisões de estrutura foram feitas pensando em **escalabilidade futura**
- Até então me proporcionou a prática de **consumo de APIs**, **tratamento de dados com pandas** e **organização de um projeto Python em múltiplas camadas**.






