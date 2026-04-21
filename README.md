🐟 Fish Species Classification

Bu projede, balıkların fiziksel ölçümlerine (ağırlık, uzunluk, yükseklik vb.) dayanarak türlerinin makine öğrenmesi algoritmaları ile tahmin edilmesi amaçlanmıştır.

📌 Proje Hakkında

Balık türlerinin doğru şekilde sınıflandırılması; balıkçılık yönetimi, ekosistem takibi ve biyolojik çeşitliliğin korunması açısından önemlidir.

Bu çalışmada, biyometrik veriler kullanılarak farklı makine öğrenmesi modelleri uygulanmış ve performansları karşılaştırılmıştır.

📊 Veri Seti
Kaynak: Fish Market Dataset (Kaggle)
Toplam gözlem: 159
Tür sayısı: 6
Kullanılan Özellikler:
Weight
Length1
Length2
Length3
Height
Width

Hedef değişken:

Species (balık türü)
⚙️ Veri Ön İşleme
Eksik değer analizi yapıldı
Eksik veriler median yöntemi ile dolduruldu
Kategorik veriler sayısal forma dönüştürüldü (Label Encoding)
Veri seti %80 eğitim, %20 test olarak ayrıldı
Gerekli modeller için veri ölçekleme uygulandı

🤖 Kullanılan Modeller
Logistic Regression
Random Forest
K-Nearest Neighbors (KNN)
Support Vector Machine (SVM)

📈 Değerlendirme Metrikleri
Accuracy
Precision (weighted)
Recall (weighted)
F1 Score (weighted)

🏆 Sonuçlar
Tüm modeller genel olarak yüksek doğruluk oranı elde etmiştir
Logistic Regression modeli en dengeli ve başarılı sonuçları vermiştir
Bazı türler arasında (özellikle benzer fiziksel özelliklere sahip olanlar) karışmalar gözlemlenmiştir

📉 PCA Analizi
Veri setinin yapısını daha iyi anlamak için PCA uygulanmıştır:

Boyut indirgeme yapılmıştır (6 → 2)
Türlerin dağılımı görselleştirilmiştir
Bazı sınıfların örtüştüğü görülmüştür

🧪 Kullanılan Teknolojiler
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn

🚀 Kurulum ve Çalıştırma
git clone https://github.com/kullaniciadi/proje-adi.git
cd proje-adi
pip install -r requirements.txt
python main.py

📁 Proje Yapısı
├── fish.csv
├── main.py
├── README.md
└── rapor.pdf
📌 Not

Bu proje eğitim amaçlı geliştirilmiştir ve veri madenciliği / makine öğrenmesi yöntemlerinin karşılaştırılması üzerine odaklanmaktadır.
