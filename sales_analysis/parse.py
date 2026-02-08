import pandas as pd
import matplotlib.pyplot as plt
import os

ARQUIVO_CSV = os.path.join(os.path.dirname(__file__), 'arquivo.csv')

def parse_data():
    # 1. Carregar dados CSV (colunas: data, produto, quantidade_vendida, preco)
    df = pd.read_csv(ARQUIVO_CSV, sep=",")

    # 2. Calcular o total de vendas por mês
    df['month'] = pd.to_datetime(df['data']).dt.month
    df['year'] = pd.to_datetime(df['data']).dt.year
    df['total_sales'] = df['quantidade_vendida'] * df['preco']

    # 3. Determinar o produto mais vendido (por quantidade) e o de maior receita
    product_sales = df.groupby('produto')['total_sales'].sum().reset_index()
    product_sales = product_sales.sort_values('total_sales', ascending=False)
    highest_revenue_product = product_sales.iloc[0]['produto']

    product_quantity = df.groupby('produto')['quantidade_vendida'].sum().reset_index()
    product_quantity = product_quantity.sort_values('quantidade_vendida', ascending=False)
    most_sold_product = product_quantity.iloc[0]['produto']
    # Totais por mês para o gráfico
    monthly_df = df.groupby(['month', 'year'])['total_sales'].sum().reset_index()

    # 4. Gráfico de vendas por mês
    plt.figure(figsize=(10, 5))
    plt.plot(monthly_df['month'], monthly_df['total_sales'], label='Total Sales')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.title('Total Sales by Month')
    plt.legend()
    plt.show()

    # 5. Gráfico dos 5 principais produtos por receita
    plt.figure(figsize=(10, 5))
    top5 = product_sales.head(5)
    plt.bar(top5['produto'], top5['total_sales'])
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.title('Top 5 Products by Revenue')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    return monthly_df, most_sold_product, highest_revenue_product

if __name__ == "__main__":
    df, most_sold_product, highest_revenue_product = parse_data()
    print('Total de vendas por mês:\n', df)
    print('\nO produto mais vendido é:', most_sold_product)
    print('\nO produto de maior receita é:', highest_revenue_product)