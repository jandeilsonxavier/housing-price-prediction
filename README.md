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
* `area`: Área da casa (em sq ft)
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

* Conversão de variáveis categóricas em numéricas com `.map()`.
* Treinamento/teste dividido com `train_test_split`.
* Padronização opcional com `StandardScaler`.

---

## 🧠 Scores dos Modelos Testados

| Modelo                | MAE    | MSE    | RMSE   | R²     |
| --------------------- | ------ | ------ | ------ | ------ |
| Regressão Linear      | 0.98   | 1.77   | 1.77   | 0.65   |
| Árvore de Decisão     | 1.24   | 2.76   | 1.66   | 0.45   |
| Random Forest (tuned) | 1.02   | 1.93   | 1.39   | 0.62   |
| Gradient Boosting     | 1.00   | 1.90   | 1.38   | 0.63   |

---

## 💽 Aplicação Web

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
* `numpy`

---

## 📌 Conclusão

Este projeto demonstrou que modelos baseados em árvores (como Random Forest e Gradient Boosting) apresentam melhor desempenho do que Regressão Linear para prever preços de imóveis. O app oferece uma interface prática para usuários finais.

---

## 👨‍💼 Autor

* **Jose Jandeilson Xavier dos Santos**
* [LinkedIn](https://www.linkedin.com/) | [GitHub](https://github.com/)

---

## 💻 Como Executar

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