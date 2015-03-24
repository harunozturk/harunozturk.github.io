#   Yapay Sinir Ağları  

.fx: first

Harun Öztürk `<harun.ozturk@bil.omu.edu.tr>`

Özcan Çamoğlu `<ozcan.camoglu@bil.omu.edu.tr>`

##  Konular

-   Danışmansız Öğrenme (Unsupervised Learning)

-   Yarışmacı Öğrenme (Competitive Learning)

-   Özörgütlemeli Harita Ağı (Self Organizing Map)

Özörgütlemeli harita ağı, yarışmacı öğrenme algoritmasını kullanır

Danışmansız öğrenme yöntemlerinden biridir

#   Danışmansız Öğrenme

##  Nedir?

-   Sisteme nasıl davranması gerektiğini söyleyen insan/makine yok

-   Sisteme çıkış bilgisi verilmez

-   Genelde çıkış hakkında bilgimizin olmadığı problemlerle boğuşur

-   Girişlere göre kendi kendini eğitir

-   Ağ, işlemleri yaparak **zamanla** öğrenir

##  Danışmansız Öğrenme

![unsupervised] (media/unsupervised.jpg)

-   Giriş verileri karmaşık

-   Bir algoritmadan geçir

-   Kümelenmiş veriler

#   Yarışmacı Öğrenme

##  Nedir?

-   Giriş verilerine göre proseslerin yarıştığı bir yaklaşımdır

-   Giriş verilerini kümelemek için kullanılır

-   Danışmansız öğrenme veya destekleyici öğrenme ile kullanılabilir

-   Giriş elemanları ağdaki bütün proseslere bağlıdır

-   Yarış sonunda bir proses kazanır

-   Kazanan prosesin ağırlıkları güncellenir

-   Yaklaşıma göre kazanan prosesin komşularının ağırlıkları da güncellenebilir

##  Yarışmacı Öğrenme

-   BMU: Best Match Unit

![competitive](media/competitive.jpg)

##  Yarışmacı Öğrenme

-   Bir prosesin bir giriş verisine yakın olması

-   Kazanan proses giriş verisine yaklaştırılır

![competitive2](media/competitive2.png)

##  Yarışmacı Öğrenme

-   Çıkışa göre veya öklid uzaklığına göre

![competitive3](media/competitive3.png)

-   Büyük olan veya yakın olan

![competitive4](media/competitive4.png)

-   Yarışı kazanır

![competitive5](media/competitive5.png)



##  Farklı Yaklaşımlar

-   Sadece kazanan proses değil komşuları da güncellensin

Özörgütlemeli harita ağı

-   Yarışı kazanan ve ikinci olan proses güncellensin

-   Kazananı yaklaştır, ikinci olanı uzaklaştır

-   Sınır değerlerini iyileştirmek için kullanılır

LVQ2: Linear Vector Quantization

-   Destekleyici öğrenmede yanlış sınıfa ait proses kazanırsa

-   O prosesi uzaklaştırırken doğru sınıfın yerel kazananını yakınlaştır

LVQ-X

-   Bir proses sürekli kazanıyorsa cezalandır

#   Özörgütlemeli Harita Ağı

##  Nedir?

-   Yarışmacı öğrenimle eğitilen ileri beslemeli ağ

-   Giriş katmanı ve yarışmacı katmanından oluşur

-   Yarışmacı katmanına Kohonen katmanı denir

-   Kohonen katmanında ki her bir prosese bütün girişler bağlanır

##  Özörgütlemeli Harita Ağı

-   Kazanan proses elemanı belirlenir

![competitive6](media/competitive6.png)

-   Kazanan prosesin ağırlıkları değiştirilir

![competitive7](media/competitive7.png)

##  Özörgütlemeli Harita Ağı

-   Değişim miktarı

![competitive8](media/competitive8.png)

-   Öğrenme katsayısı güncellenir

![competitive9](media/competitive9.png)

-   Topolojik çap azaltılır

![competitive10](media/competitive10.png)

##  Örnek

-   Öğrenme katsayısı α0 = 0.6

-   Ağırlıklar

![competitive11](media/competitive11.png)

-   Giriş değerleri

![competitive12](media/competitive12.png)

##  Ağ Yapısı

![competitive13](media/competitive13.png)

-   Sadece ilk değer için gerçekleştireceğiz

##  Öklid Uzaklıkları

-   P1 prosesinin [1, 1, 1, 0, 0, 0, 0] noktasına öklid uzaklığı

sqrt(

     (0.2-1)^^2 + (0.6-1)^^2 + (0.5-1)^^2 +

     (0.9-0)^^2 + (0.4-0)^^2 + (0.2-0)^^2 +

     (0.8-0)^^2 ) = 1.6431

P2 = 1.2328

P3 = 1.3564

P4 = 1.3928

**`P5 = 1.1532`**

![competitive6](media/competitive6.png)

##  Kazanan Proses

![competitive14](media/competitive14.png)

-   Kazanan proses belirlendi

-   Ağırlıklar değiştirilecek

##  Ağırlıkların Değişimi

![competitive7](media/competitive7.png)

![competitive8](media/competitive8.png)

![competitive15](media/competitive15.png)

-   Eski ağırlıklar **[0.8, 0.9, 0.7, 0.9, 0.3, 0.2, 0.5]**

-   Güncellenmiş ağırlıklar **`[0.92, 0.96, 0.88, 0.36, 0.12, 0.08, 0.2]`**

##  Diğer Girdi Değerleri

-   Diğer girdi değerleri için aynı adımları tekrarla

![competitive12](media/competitive12.png)

##  Öğrenme Katsayısını Güncelle

-   Bir epoch tamamlandıktan sonra α0 öğrenme katsayısını güncelle

![competitive9](media/competitive9.png)

t: İterasyon adımı

T: Toplam işlem sayısı

-   Zamanla sıfıra yakınsar



##  Özörgütlemeli Harita Ağı

.code: code/som.py

















