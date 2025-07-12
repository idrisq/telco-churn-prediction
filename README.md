# Müşteri Kaybı (Churn) Tahmin Projesi

Bu proje, bir telekomünikasyon şirketi için müşteri kaybı (churn) olasılığını tahmin eden uçtan uca bir makine öğrenmesi çözümüdür. Proje, veri analizinden modelin bir API olarak sunulmasına kadar tüm adımları kapsamaktadır.

## Problem Tanımı

Müşteri kaybı, abonelik tabanlı iş modelleri için en büyük maliyet kalemlerinden biridir. Yeni müşteri kazanmak, mevcut bir müşteriyi elde tutmaktan çok daha maliyetlidir. Bu projenin amacı, hangi müşterilerin hizmeti terk etme olasılığının yüksek olduğunu proaktif olarak tespit ederek, şirketin bu müşterilere özel kampanyalarla ulaşıp onları elde tutmasını sağlayacak bir karar destek sistemi geliştirmektir.

## Kullanılan Teknolojiler ve Kütüphaneler

- **Python 3.9**
- **Veri Analizi ve Modelleme:** Pandas, NumPy, Scikit-learn, XGBoost
- **Veri Görselleştirme:** Matplotlib, Seaborn
- **API Sunucusu:** FastAPI, Uvicorn
- **Konteynerleştirme:** Docker
- **Model Kaydetme:** Joblib

## Veri Seti

Projede, Kaggle'da halka açık olarak yayınlanan "Telco Customer Churn" veri seti kullanılmıştır.
[Veri Seti Linki](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

## Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

```bash
# 1. Proje reposunu klonlayın
git clone [https://github.com/idrisq/telco-churn-prediction.git](https://github.com/senin-kullanici-adin/telco-churn-prediction.git)
cd telco-churn-prediction

# 2. Python sanal ortamı oluşturun ve aktive edin
# Windows:
python -m venv venv
venv\Scripts\activate
# MacOS/Linux:
# python3 -m venv venv
# source venv/bin/activate

# 3. Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt
```

## Kullanım

API sunucusunu başlatmak için aşağıdaki komutu çalıştırın:

```bash
uvicorn main:app --reload
```

Sunucu başlatıldıktan sonra, interaktif dokümantasyona ve test arayüzüne erişmek için tarayıcınızdan `http://127.0.0.1:8000/docs` adresine gidin.

## Proje Yapısı

```
telco-churn-prediction/
│
├── data/
│   └── raw/
├── models/
│   ├── churn_model_v1.joblib
│   └── model_columns.json
├── notebooks/
│   └── 1.0-EDA-ve-Analiz.ipynb
├── src/
│   ├── __init__.py
│   └── schema.py
├── .gitignore
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```

## Sonuçlar ve Değerlendirme

Farklı modeller eğitilmiş ve iş problemine en uygun metrik olan **Recall (Duyarlılık)** skoruna göre karşılaştırılmıştır. XGBoost modeli, giden müşterileri yakalama konusunda en başarılı model olmuştur.

| Model                        | Accuracy | Precision | Recall | F1 Score | AUC-ROC |
|------------------------------|----------|-----------|--------|----------|---------|
| Lojistik Regresyon (Baseline) | 0.8169   | 0.6724    | 0.5641 | 0.6135   | 0.8447  |
| **XGBoost (Gelişmiş)** | **0.8034** | **0.6037** | **0.7844** | **0.6822** | **0.8606** |



## Gelecek Geliştirmeler

- **Hyperparameter Tuning:** Optuna veya Hyperopt gibi kütüphanelerle XGBoost modelinin hiperparametreleri optimize edilebilir.
- **Alternatif Modeller:** LightGBM ve CatBoost gibi diğer Gradient Boosting modelleri denenebilir.
- **Bulut Dağıtımı:** Proje, AWS Elastic Beanstalk, Google Cloud Run veya Heroku gibi bir bulut platformuna dağıtılabilir.
- **CI/CD Pipeline:** GitHub Actions kullanılarak, koda her push yapıldığında otomatik test ve dağıtım süreçleri (CI/CD) eklenebilir.
