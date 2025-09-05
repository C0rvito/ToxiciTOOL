# Usa a imagem oficial do Python como base
FROM python:3.10.12

# Define o autor do Dockerfile
LABEL maintainer="corvo"

# Define o diretório de trabalho dentro do contêiner
WORKDIR /usr/src/myapp

# Copia o arquivo de dependências para o diretório de trabalho
COPY ./python_req.txt .

# Atualiza o pip e instala as dependências do projeto
RUN pip install --upgrade pip && \
    pip install -r python_req.txt

# Instala as bibliotecas extras que você pediu para manter
RUN pip install jiwer gradio typing_extensions

# Instala dependências do sistema operacional (para gerar PDFs, etc.)
# O comando é unificado para criar uma única camada e limpar o cache depois, otimizando o tamanho da imagem
RUN apt-get update -y && \
    apt-get install -y pandoc texlive-xetex texlive-fonts-recommended texlive-plain-generic && \
    rm -rf /var/lib/apt/lists/*

# Copia todos os arquivos do seu projeto (do seu computador) para o diretório de trabalho (no contêiner)
COPY . .

# Copia as configurações personalizadas do JupyterLab (opcional)
COPY ./JupyterLab-configs/tracker.jupyterlab-settings /root/.jupyter/lab/user-settings/@jupyterlab/notebook-extension/tracker.jupyterlab-settings
COPY ./JupyterLab-configs/themes.jupyterlab-settings /root/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings
COPY ./JupyterLab-configs/plugin.jupyterlab-settings /root/.jupyter/lab/user-settings/@jupyterlab/docmanager-extension/plugin.jupyterlab-settings

# Expõe a porta que o JupyterLab usará
EXPOSE 8888

# Comando padrão que será executado quando o contêiner iniciar
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]