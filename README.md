# Visualização 3D de Indicadores 

Este script gera um gráfico de dispersão tridimensional interativo a partir de um arquivo CSV, permitindo a análise de três indicadores (ou respostas) para diferentes unidades organizacionais, categorizadas por eixos temáticos.

## 📋 Descrição

O código utiliza as bibliotecas **Pandas** (manipulação de dados) e **Plotly Express** (visualização) para:

1. Ler um arquivo `.csv` exportado de uma ferramenta de BI.
2. Mapear cada unidade/sigla para um eixo estratégico pré-definido.
3. Criar um gráfico 3D onde os pontos representam as unidades, posicionados de acordo com os valores de três colunas do CSV.
4. Colorir os pontos conforme o eixo estratégico e exibir uma legenda explicativa.
5. Salvar o gráfico como um arquivo HTML interativo.

## ⚙️ Requisitos

- Python 3.7 ou superior
- Bibliotecas listadas no arquivo (ou instale diretamente):

```bash
pip install pandas plotly
