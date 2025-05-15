# 🏠 Previsão de Preços de Imóveis com Machine Learning

Este projeto utiliza algoritmos de Machine Learning para prever o preço de casas com base em características como área, número de quartos, localização, status de mobília, entre outros.

---

## 🎯 Objetivo

Construir um modelo preditivo capaz de estimar o preço de imóveis residenciais com base em atributos estruturais e localização.

---

## 📊 Dataset

**Fonte:** ([Housing Price Prediction - Kaggle](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction))

**Atributos disponíveis:**

* `price`: Preço da casa (variável alvo)
* `area`: Área da casa (em pés²)
* `bedrooms`: Número de quartos
* `bathrooms`: Número de banheiros
* `stories`: Número de andares
* `mainroad`: Acesso à estrada principal (Sim/Não)
* `guestroom`: Possui quarto de hóspedes? (Sim/Não)
* `basement`: Possui porão? (Sim/Não)
* `hotwaterheating`: Possui aquecimento de água? (Sim/Não)
* `airconditioning`: Possui ar-condicionado? (Sim/Não)
* `parking`: Número de vagas de garagem
* `prefarea`: Está em uma área preferida? (Sim/Não)
* `furnishingstatus`: Status da mobília (Sem mobília, Semi-mobiliado, Totalmente mobiliado)

---

## 🔧 Pré-processamento

* Remoção de Outliers
* Transformação de variáveis categóricas em numéricas
* Transformação da variavel `price` em milhões para melhor visualização
* Separar o dados em dados de treino e dados de teste com `train_test_split`
---

## 🧠 Scores dos Modelos Testados

| Modelo                 | MAE  | MSE  | RMSE | R²   |
|------------------------|------|------|------|------|
| Linear Regression      | 0.74 | 0.98 | 0.99 | 0.67 |
| Lasso                  | 0.85 | 1.22 | 1.10 | 0.59 |
| Lasso (com tuning)     | 0.75 | 0.98 | 0.99 | 0.67 |
| Decision Tree          | 1.02 | 1.82 | 1.35 | 0.38 |
| Random Forest          | 0.76 | 1.06 | 1.03 | 0.64 |
| Random Forest (tuned)  | 0.75 | 0.98 | 0.99 | 0.67 |

---

## 🌐 Aplicação Web

Desenvolvido um app interativo com [**Streamlit**](https://streamlit.io) para inserção dos dados e visualização da predição.

### Rodar localmente:

```bash
streamlit run app.py
```

---

## 📦 Dependências

```bash
pip install -r requirements.txt
```

### Pacotes utilizados:

* `pandas`
* `scikit-learn`
* `streamlit`
* `joblib`

---

## ✅ Conclusão

O presente projeto teve como objetivo desenvolver um modelo preditivo capaz de estimar o preço de imóveis residenciais com base em características como área construída, número de quartos, banheiros, presença de comodidades adicionais e localização em rua principal. Para isso, realizamos uma série de etapas fundamentais no fluxo de um projeto de ciência de dados, incluindo análise exploratória, tratamento de dados, engenharia de variáveis, escolha e avaliação de modelos, além da construção de um aplicativo interativo com Streamlit.

Após testarmos diversos algoritmos, como Regressão Linear, Lasso, Decision Tree, Random Forest e Gradient Boosting, o modelo de Random Forest Regressor com tuning de hiperparâmetros via GridSearchCV se destacou. Ele apresentou bom desempenho em termos de erro absoluto médio (MAE = 0.75) e coeficiente de determinação (R² = 0.67), equilibrando precisão e robustez, além de lidar bem com variáveis não lineares e possíveis interações entre os atributos.

Além disso, adotamos práticas de boas práticas como remoção de outliers com o método do intervalo interquartil (IQR), normalização dos dados e transformação de variáveis categóricas. O modelo final foi versionado e salvo com a biblioteca joblib, e sua aplicação foi disponibilizada em formato de aplicativo web utilizando Streamlit, permitindo que usuários finais façam previsões de preços de forma simples e rápida.

Este projeto demonstra como é possível aplicar técnicas de ciência de dados para resolver problemas reais de mercado imobiliário, e pode ser expandido futuramente com mais variáveis (como localização geográfica ou tempo de construção) ou com o uso de modelos ainda mais avançados. Ele está pronto para ser utilizado em produção e oferece um excelente ponto de partida para análises mais aprofundadas no setor.

---

## 💻 Como Executar Localmente

1. **Clone este repositório**
```bash
git clone https://github.com/jandeilsonxavier/analise-regras-associacao.git
cd restaurants-service-repository
```
2. **Crie o ambiente virtual**
```bash
python -m venv venv
```
3. **Ative o ambiente virtual**
```bash
No Windows:
venv\Scripts\activate

No Mac/Linux:
source venv/bin/activate
```
4. **Instale as dependências**
```bash
pip install -r requirements.txt
```
5. **Execute o script principal**
```bash
streamlit run app.py
```