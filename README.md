# ToxiciTOOL

## Descrição do Projeto

O **ToxiciTOOL** é uma ferramenta computacional desenvolvida para predição de toxicidade de compostos químicos utilizando técnicas de machine learning e deep learning. O sistema permite analisar estruturas moleculares e prever sua toxicidade em diferentes espécies e vias de administração, oferecendo uma alternativa eficiente aos testes in vivo tradicionais.

### Metodologia

O sistema funciona através das seguintes etapas:

1. **Entrada de dados**: O usuário fornece a estrutura química da substância no formato SMILES (Simplified Molecular-Input Line-Entry System)
2. **Processamento molecular**: O programa analisa a estrutura utilizando algoritmos de química computacional
3. **Predição de toxicidade**: Aplicação de modelos de redes neurais artificiais treinados com dados experimentais
4. **Geração de resultados**: Produção de relatórios quantitativos e visualizações dos resultados

### Aplicações

- **Pesquisa farmacêutica**: Avaliação pré-clínica de candidatos a fármacos
- **Indústria química**: Verificação de segurança de produtos químicos
- **Educação científica**: Ferramenta didática para química computacional e inteligência artificial
- **Desenvolvimento sustentável**: Redução de custos e tempo em testes de toxicidade

### Modelos Biológicos

O ToxiciTOOL realiza predições de toxicidade para:

- **Ratos** (via intravenosa e oral)
- **Camundongos** (via intravenosa e oral)

### Funcionalidades Principais

- **Pré-processamento de dados**: Sanitização e validação de estruturas moleculares
- **Representação molecular**: Geração de fingerprints moleculares utilizando RDKit
- **Classificação automatizada**: Implementação de redes neurais artificiais para predição
- **Análise estatística**: Cálculo de métricas de performance e validação dos modelos
- **Visualização de dados**: Geração de gráficos e matrizes de confusão

### Estrutura do Projeto

```
ToxiciTOOL-main/
├── docker/                    # Configurações do ambiente containerizado
│   ├── docker-compose-app.yml # Arquivo de configuração do Docker Compose
│   ├── python.Dockerfile      # Especificações da imagem Python personalizada
│   ├── python_req.txt         # Dependências Python do projeto
│   └── JupyterLab-configs/    # Configurações personalizadas do JupyterLab
├── script/                    # Códigos principais do projeto
│   ├── Limpeza.ipynb          # Notebook para pré-processamento de dados
│   ├── modelos_ANN_classificacao.ipynb # Notebook para treinamento de modelos
│   ├── representacao.py       # Módulo para representação molecular
│   ├── *.csv                  # Datasets de toxicidade
│   ├── Plots/                 # Gráficos e visualizações geradas
│   └── Resultados/            # Resultados quantitativos dos modelos
└── README.md                  # Documentação do projeto
```

## Pré-requisitos do Sistema

Para executar o ToxiciTOOL, é necessário ter instalado no sistema:

### Requisitos Técnicos

1. **Docker** - Plataforma de containerização para isolamento do ambiente
2. **Docker Compose** - Ferramenta para orquestração de containers
3. **Git** - Sistema de controle de versão para clonagem do repositório
4. **Navegador web** - Interface para acesso ao JupyterLab

### Conceito de Containerização

O Docker utiliza containerização para criar ambientes isolados e reproduzíveis. Esta abordagem oferece:

- **Isolamento**: O ambiente de execução é independente do sistema operacional host
- **Reprodutibilidade**: Garantia de que o software funcionará de forma idêntica em diferentes sistemas
- **Portabilidade**: Facilidade de distribuição e instalação
- **Gerenciamento de dependências**: Instalação automática de todas as bibliotecas necessárias

## Instalação e Configuração

### 1. Instalação do Docker

#### Linux (Ubuntu/Debian):

Execute os seguintes comandos no terminal:

```bash
# Instalação do Docker
curl -fsSL https://get.docker.com | sh

# Instalação do Docker Compose
sudo apt-get update && sudo apt-get install -y docker-compose

# Configuração de permissões de usuário
sudo usermod -aG docker ${USER}

# Aplicação das mudanças de grupo
newgrp docker
```

**Nota**: Será solicitada a senha do usuário durante a instalação.

#### Windows:

1. Acesse o site oficial: https://www.docker.com/products/docker-desktop
2. Baixe o instalador "Docker Desktop Installer.exe"
3. Execute o instalador e siga as instruções de instalação
4. Reinicie o sistema quando solicitado
5. Inicie o Docker Desktop através do ícone na área de trabalho

**Importante**: O Docker Desktop deve estar em execução (ícone visível na barra de tarefas) para funcionar.

#### macOS:

1. Acesse o site oficial: https://www.docker.com/products/docker-desktop
2. Baixe o arquivo Docker.dmg
3. Abra o arquivo baixado e arraste o Docker para a pasta Applications
4. Inicie o Docker Desktop através da pasta Applications
5. Siga as instruções de configuração inicial

### Verificação da Instalação

Para verificar se a instalação foi bem-sucedida, execute no terminal:

```bash
docker --version
```

A saída esperada deve mostrar a versão instalada do Docker (exemplo: "Docker version 20.10.x").

### 2. Clonagem do Repositório

Para obter o código-fonte do projeto:

1. Abra o terminal (Linux/macOS) ou Prompt de Comando (Windows)
2. Navegue até o diretório desejado para o projeto
3. Execute os seguintes comandos:

```bash
# Clonagem do repositório
git clone <URL_DO_REPOSITORIO>

# Navegação para o diretório do projeto
cd ToxiciTOOL-main
```

**Sobre o Git**: Git é um sistema de controle de versão distribuído que permite baixar e gerenciar códigos-fonte de repositórios remotos.

### 3. Especificações do Ambiente

O ambiente Docker configurado inclui as seguintes dependências:

- **Python 3.10.12** - Linguagem de programação principal
- **JupyterLab** - Ambiente de desenvolvimento interativo
- **RDKit** - Biblioteca para química computacional e análise molecular
- **TensorFlow 2.12.0** - Framework para deep learning e redes neurais
- **Scikit-learn** - Biblioteca para machine learning tradicional
- **Pandas, NumPy, Matplotlib** - Bibliotecas para manipulação e visualização de dados
- **SciPy, Seaborn** - Ferramentas adicionais para análise estatística e visualização

Este ambiente garante a reprodutibilidade dos resultados e facilita a distribuição do projeto.

## Execução do Projeto

### 1. Construção e Inicialização do Ambiente

Para construir e iniciar o ambiente Docker:

1. Navegue até o diretório do projeto no terminal
2. Acesse o diretório docker:
```bash
cd docker
```

3. Construa a imagem Docker (processo que pode levar 5-10 minutos na primeira execução):
```bash
docker-compose build
```

**Processo de construção**: O Docker baixa e instala todas as dependências necessárias, criando um ambiente isolado e configurado.

4. Inicie o container:
```bash
docker-compose up
```

**Indicador de sucesso**: Após a inicialização, será exibida uma mensagem similar a:

```
env-docker    | [I 2024-01-01 12:00:00.000 ServerApp] Jupyter Server 1.0.0 is running at:
env-docker    | [I 2024-01-01 12:00:00.000 ServerApp] http://0.0.0.0:8888/lab?token=abc123def456...
```

### 2. Acesso ao JupyterLab

O JupyterLab fornece uma interface web para desenvolvimento interativo:

1. **Extração do token**: Copie o token de autenticação exibido no terminal (parte após `token=`)
2. **Acesso via navegador**: Abra seu navegador web e acesse `http://localhost:8888`
3. **Autenticação**: Cole o token quando solicitado
4. **Login**: Clique em "Log in" para acessar o ambiente

Após o login, você terá acesso ao ambiente de desenvolvimento do ToxiciTOOL.

### 3. Execução dos Notebooks

#### Notebook 1: Pré-processamento de Dados (`Limpeza.ipynb`)

Este notebook implementa a classe `Limpeza` para processamento e validação de dados moleculares:

1. Abra o arquivo `Limpeza.ipynb` no JupyterLab
2. Leia as instruções e documentação no notebook
3. Execute as células sequencialmente (Shift+Enter)

**Funcionalidades**:
- Sanitização de estruturas moleculares SMILES
- Validação de dados de toxicidade
- Remoção de entradas inválidas ou inconsistentes
- Preparação de datasets para análise

**Exemplo de implementação**:
```python
# Carregamento dos dados de toxicidade
df = pd.read_csv('rat_vi.csv')

# Instanciação da classe de limpeza
limpeza = Limpeza(df)

# Processamento dos dados
dados_limpos = limpeza.dados_limpos(
    col_smiles='SMILES',    # Coluna contendo estruturas SMILES
    col_valor='LD50',       # Coluna com valores de toxicidade
    sanitize=True,          # Aplicar sanitização molecular
    fragmento=False,        # Excluir fragmentos moleculares
    cutoff=0.05            # Threshold para remoção de dados
)
```

#### Notebook 2: Modelos de Classificação (`modelos_ANN_classificacao.ipynb`)

Este notebook implementa e treina modelos de redes neurais artificiais para classificação de toxicidade:

1. Abra o arquivo `modelos_ANN_classificacao.ipynb`
2. Configure os parâmetros do modelo conforme necessário
3. Execute as células em sequência

**Processo de treinamento**:
1. **Configuração**: Definição dos hiperparâmetros do modelo
2. **Carregamento**: Importação dos dados pré-processados
3. **Treinamento**: Otimização dos pesos da rede neural
4. **Avaliação**: Validação e cálculo de métricas de performance

**Resultados**: O notebook gera matrizes de confusão, métricas de classificação e visualizações dos resultados.

### 4. Estrutura dos Dados

O ToxiciTOOL utiliza diferentes tipos de datasets de toxicidade:

#### Tipos de Arquivos:

- **`*_vi.csv`**: Dados de toxicidade intravenosa (administração direta na corrente sanguínea)
- **`*_vo.csv`**: Dados de toxicidade oral (administração via oral)
- **`*_classificado.csv`**: Dados pré-processados e classificados para treinamento dos modelos

#### Espécies Biológicas:

- **`rat_*`**: Dados experimentais de ratos (Rattus norvegicus)
- **`mouse_*`**: Dados experimentais de camundongos (Mus musculus)

**Exemplo de nomenclatura**: `rat_vi_classificado.csv` contém dados de toxicidade intravenosa em ratos, pré-processados e classificados.

### 5. Configurações dos Modelos

O sistema testa automaticamente diferentes configurações de hiperparâmetros para otimização:

```python
# Parâmetros testados automaticamente:
use_count_option = [False, True]      # Contagem de características moleculares
fpSize_option = [2048, 4096, 8192]   # Dimensionalidade do fingerprint molecular
radius_option = [2, 3, 5]            # Raio de exploração da estrutura molecular
```

**Interpretação dos parâmetros**:
- **fpSize**: Dimensionalidade do vetor de características (maior dimensionalidade = maior capacidade de representação, maior custo computacional)
- **radius**: Raio de exploração da estrutura molecular (maior raio = captura de mais informações estruturais)
- **use_count**: Método de contagem de características (binário vs. ponderado)

## Comandos Docker Avançados

### Gerenciamento de Containers

```bash
# Listar containers em execução
docker ps

# Parar o ambiente (encerra o JupyterLab)
docker-compose down

# Reiniciar o ambiente
docker-compose restart

# Visualizar logs do sistema (útil para diagnóstico)
docker-compose logs -f

# Acesso ao terminal do container (usuários avançados)
docker exec -it env-docker /bin/bash
```

### Limpeza do Sistema

```bash
# Remover containers inativos
docker container prune

# Remover imagens não utilizadas (libera espaço em disco)
docker image prune

# Limpeza completa do sistema Docker (use com cautela)
docker system prune -a
```

## Estrutura dos Resultados

Após a execução dos modelos, os resultados são organizados da seguinte forma:

### Visualizações:
- **`script/Plots/`**: Gráficos e matrizes de confusão gerados
  - `rat_vi/`: Resultados para toxicidade intravenosa em ratos
  - `rat_vo/`: Resultados para toxicidade oral em ratos
  - `mouse_vi/`: Resultados para toxicidade intravenosa em camundongos
  - `mouse_vo/`: Resultados para toxicidade oral em camundongos

### Dados Quantitativos:
- **`script/Resultados/`**: Arquivos CSV com métricas de performance
  - `rat_vi/resultados.csv`: Métricas para ratos intravenosos
  - `rat_vo/resultados.csv`: Métricas para ratos orais

**Tipos de resultados gerados**:
- **Matrizes de confusão**: Visualização da performance de classificação
- **Métricas de performance**: Precisão, recall, F1-score, acurácia
- **Comparações de modelos**: Análise comparativa entre diferentes configurações

## Solução de Problemas

### Problema 1: Falha na inicialização do container

**Sintomas**: O comando `docker-compose up` retorna erro ou não executa.

**Diagnóstico e soluções**:
```bash
# Verificar instalação do Docker
docker --version
docker-compose --version

# Verificar status dos containers
docker ps

# Analisar logs de erro
docker-compose logs
```

**Soluções específicas**:
- **Windows**: Verificar se o Docker Desktop está em execução
- **Linux**: Executar com privilégios administrativos se necessário (`sudo`)

### Problema 2: Conflito de porta

**Sintomas**: Erro indicando que a porta 8888 está em uso.

**Soluções**:
```bash
# Identificar e parar containers usando a porta 8888
docker stop $(docker ps -q --filter "publish=8888")

# Alternativa: modificar a porta no arquivo docker-compose-app.yml
# Alterar "8888:8888" para "8889:8888"
```

### Problema 3: Erros de permissão (Linux)

**Sintomas**: Mensagens de "permission denied" ou "access denied".

**Soluções**:
```bash
# Adicionar usuário ao grupo docker
sudo usermod -aG docker $USER

# Aplicar mudanças de grupo
newgrp docker

# Alternativa: logout/login do sistema
```

### Problema 4: Falha no acesso ao JupyterLab

**Sintomas**: Navegador não consegue acessar a interface ou retorna erro 404.

**Soluções**:
1. Verificar se o container está em execução: `docker ps`
2. Confirmar o token de autenticação correto
3. Utilizar a URL correta: `http://localhost:8888`
4. Limpar cache do navegador

### Problema 5: Tempo excessivo de construção

**Sintomas**: O processo `docker-compose build` demora mais de 15 minutos.

**Explicações**:
- **Primeira execução**: Normal devido ao download de dependências
- **Conexão lenta**: Aguardar conclusão do processo
- **Problemas de rede**: Verificar conectividade com a internet

### Diagnóstico avançado

Para problemas persistentes:

1. **Análise de logs**: `docker-compose logs -f`
2. **Reinicialização completa**: `docker-compose down` seguido de `docker-compose up`
3. **Reconstrução forçada**: `docker-compose down` → `docker-compose build --no-cache` → `docker-compose up`

## Contribuição

Este projeto está em desenvolvimento ativo e aceita contribuições da comunidade científica.

### Processo de Contribuição

1. **Fork do repositório**: Crie uma cópia do projeto em sua conta
2. **Criação de branch**: Desenvolva sua contribuição em uma branch separada
3. **Commit das mudanças**: Documente adequadamente suas modificações
4. **Pull Request**: Submeta sua contribuição para revisão

### Diretrizes

- Mantenha a documentação atualizada
- Siga as convenções de código existentes
- Inclua testes para novas funcionalidades
- Documente adequadamente as mudanças

## Licença

Este projeto está licenciado conforme especificado no arquivo `LICENSE`.

## Contato e Suporte

Para questões relacionadas ao projeto:

- **Reportar bugs**: Utilize a aba "Issues" do repositório
- **Sugestões de melhorias**: Abra uma issue com a tag "enhancement"
- **Discussões técnicas**: Utilize a aba "Discussions" do repositório

---

## Conclusão

Este guia fornece instruções completas para instalação, configuração e execução do ToxiciTOOL. O projeto representa uma ferramenta valiosa para a comunidade científica na área de predição de toxicidade molecular.

**Nota importante**: Este projeto está em fase de desenvolvimento e testes. A documentação será atualizada conforme o projeto evolui.

**Recomendação para iniciantes**: Execute os notebooks na ordem sequencial: primeiro `Limpeza.ipynb` para pré-processamento dos dados, seguido por `modelos_ANN_classificacao.ipynb` para treinamento e avaliação dos modelos.

**Aplicação**: Utilize esta ferramenta para análises de toxicidade molecular em suas pesquisas científicas.
