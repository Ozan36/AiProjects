**CNN Mimarisi**

CNN(Evrişimsel sinir ağları) , makine öğreniminin bir alt kümesidir ve derin öğrenme algoritmalarının kalbinde yer alırlar. Bir giriş katmanı, bir veya daha fazla gizli katman ve bir çıktı katmanı içeren düğüm katmanlarından oluşurlar. Her düğüm diğerine bağlanır ve ilişkili bir ağırlığa ve eşiğe sahiptir. Herhangi bir düğümün çıktısı belirtilen eşik değerinin üzerindeyse, o düğüm etkinleştirilir ve ağın bir sonraki katmanına veri gönderilir. Aksi takdirde, ağın bir sonraki katmanına hiçbir veri iletilmez.

**Katmanlar:**

- Evrişimsel katman
- Havuzlama katmanı(Pooling)
- Tam bağlantılı (FC) katman

**Evrişimsel katman**

Evrişimsel katman (Convolutional Layer), CNN’in temel yapı taşıdır ve görüntülerdeki özellikleri (kenarlar, dokular vb.) çıkarır. Renkli bir görüntü, yükseklik, genişlik ve derinlik (RGB) boyutlarına sahiptir. Evrişim işlemi sırasında filtre (çekirdek) adı verilen küçük bir matris görüntü üzerinde kaydırılarak noktasal çarpımlar hesaplanır ve sonuçlar özellik haritası (feature map) oluşturur.

Bu işlemler sırasında filtre ağırlıkları görüntü boyunca aynı kalır (parametre paylaşımı) ve eğitim sırasında öğrenilir. Ayrıca, CNN’in çıktısının boyutunu etkileyen ve eğitim öncesinde belirlenen üç hiperparametre bulunur:

1 Filtre boyutu (ör: 3x3)

2 Adım (stride)

3 Doldurma (padding)

Bu sayede CNN, görüntülerdeki önemli özellikleri öğrenerek sınıflandırma veya nesne tespiti gibi görevleri gerçekleştirebilir.

**Havuzlama(Pooling) Katmanı:**

Havuzlama katmanı, CNN’de evrişim katmanından sonra gelen bir katmandır ve giriş verisinin boyutunu küçültürken önemli bilgileri korumayı amaçlar. Bu sayede hem hesaplama yükü azalır hem de modelin genelleme yeteneği artar.

Maksimum Havuzlama (Max Pooling):

-   Pencere içindeki en büyük değeri alır.
-   En yaygın kullanılan yöntemdir.
-   Kenar ve belirgin özellikleri korur.

Ortalama Havuzlama (Average Pooling):

-   Pencere içindeki ortalama değeri alır.
-   Verileri daha yumuşak hale getirir.
-   Gürültüyü azaltabilir, ancak belirgin kenar bilgisi kaybolabilir.

Global Ortalama Havuzlama (Global Average Pooling):

- Tüm özellik haritasının ortalamasını alır, tek değer üretir.
- Genellikle tam bağlantılı katman yerine kullanılır.
- Parametre sayısını azaltarak aşırı öğrenmeyi engeller.

**Fully Connected Layer:**

Tam bağlantılı katman (Fully Connected Layer), CNN’in son aşamasında yer alır ve sınıflandırmadan sorumludur.

Bir katmandaki her nöron, sonraki katmandaki tüm nöronlara bağlıdır.

Önceki evrişim ve havuzlama katmanlarından çıkarılan özellikleri birleştirir ve sınıflara ayırır.

Tüm katmanlar tamamen bağlı değildir çünkü çok fazla parametre kullanmak hesaplama yükünü artırır ve aşırı öğrenmeye neden olabilir.

Bu nedenle, tam bağlantılı katmanlar sadece son katmanlarda kullanılır ve modelin genelleme yeteneği ile öğrenme gücü dengelenir.


**Ek katmanlar:**

Evrişimsel, havuzlama ve tam bağlı katmanların tümü bir CNN'in çekirdek katmanları olarak kabul edilir. Ancak bir CNN'in sahip olabileceği ek katmanlar da vardır:

**Aktivasyon katmanı,** bir CNN'de yaygın olarak eklenen ve eşit derecede önemli bir katmandır. Aktivasyon katmanı doğrusal olmama özelliğini etkinleştirir -- yani ağ daha karmaşık (doğrusal olmayan) desenler öğrenebilir. Bu, karmaşık görevleri çözmek için çok önemlidir. Bu katman genellikle evrişimli veya tam bağlı katmanlardan sonra gelir. Yaygın aktivasyon işlevleri arasında ReLU, Sigmoid, Softmax ve Tanh işlevleri bulunur.

**Dropout katmanı** , eklenen bir diğer katmandır. Dropout katmanının amacı, eğitim sırasında nöronları sinir ağından düşürerek aşırı uyumu azaltmaktır. Bu, modelin boyutunu küçültür ve aşırı uyumu önlemeye yardımcı olur.


**Evrişimsel Sinir Ağları Uygulamaları:**

- **Sağlık:** Tıbbi görüntüleri (X-ışınları, patoloji slaytları) analiz ederek hastalık teşhisi ve tedavi planlamasına yardımcı olur.
- **Otomotiv:** Otonom araçlarda çevreyi algılamak ve otomatik sürüş özelliklerini (park yardımı, hız sabitleme) desteklemek için kullanılır.
- **Sosyal Medya:** Fotoğraf etiketleme önerileri ve uygunsuz içerik denetimi gibi görsel analiz görevlerini gerçekleştirir.
- **Perakende:** Görsel arama sistemleri ve ürün öneri algoritmalarını geliştirerek kullanıcı deneyimini artırır.
- **Sanal Asistanlar:** Sesli komutları tanıma ve yorumlama yeteneğiyle sanal asistanların performansını iyileştirir.

**Ozan Yılmaz**
