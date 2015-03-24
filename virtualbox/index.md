#   VirtualBox

.fx: first

Perihan Demirer `perihan.demirer@bil.omu.edu.tr`

Harun Öztürk `harun.ozturk@bil.omu.edu.tr`

##  Sanallaştırma

Bir fiziksel kaynağı birden fazla mantıksal işleme bölme

İki gruba ayrılabilir

-   System virtual machine

İşletim sistemi için sanallaştırma

-   Process virtual machine

Tek bir yazılım için sanallaştırma

##  VirtualBox

-   Innotek tarafından geliştirilmiştir

-   GPL ile lisanslanmış sürümü mevcuttur

-   Sanal makine yazılımıdır

-   Ana makine üzerinde çalışan ***`sanal`*** makineler oluşturur

##  Alternatifler

Yazılım      |  Geliştirici(ler)
-------------|------------------
KVM          | Qumranet
Xen          | Keir Fraser, Steven Hand, Ian Pratt
VMware       | VMware Inc.
Virtuozzo    | Parallels Inc.
Virtual Iron | Virtual Iron Software

##  Alternatifler
Yazılım      |  Geliştirici(ler)
-------------|------------------
QEMU         | Anthony Liguori, Paul Brook
OpenVZ       | Parallels Inc.
Hyper-V      | Microsoft
Virtual PC   | Microsoft

##  Kurulum

-   Ubuntu depolarından

	    !sh
	    $ sudo apt-get install virtualbox

Ubuntu depolarındaki hali güncel olmayabilir

-   Resmi sitesinden **.deb** uzantılı paket indirilerek

	    !sh
	    $ sudo dpkg -i /path/virtualbox.deb

##  Yeni Sanal Makine Oluşturma

Sanal makine oluşturma
:   	    !text
    	    1   Yeni
    	    2   Sanal makineye isim ver
    	    3   Bellek boyutunu seç
    	    4   Sabit disk seçimi yap
    	    5   Sabit disk dosya türü seç
    	    6   Sabit boyutlu disk - Değişken boyutlu disk seçimi yap
    	    7   Sabit disk kayıt yeri ve boyutunu seç

#   Bellek ve Disk Ayarlama

##  Bellek Ayarlama

Bellek boyutunu değiştirme
:   	    !text
    	    1   Değişiklik yapılacak sanal makineyi seç
    	    2   Ayarlar
    	    3   Sistem
    	    4   Anakart
    	    5   Ana bellek alanını değiştir

##  Disk Ayarlama

-   Başlangıçta ayırdığın alanı değiştirmek için

		!sh
		$ vboxmanage modifyhd name.vdi --resize MB_boyut

-   Değişiklikten sonra yeni açılan alanı formatlamak gerekebilir

##  Ekran Görüntüsü Alma

-   Grafik arayüzde bu iş için buton bulunmamakta

-   Bu komutu vererek mümkün

		!sh
		$ vboxmanage controlvm "VM_adi" screenshotpng /path/name.png

##  Anlık Görüntüler

-   Sanal makinenin durumunu kaydedebilme

-   İstenildiği zaman kaydedilmiş duruma dönüş

-   ***`.vdi`*** dosyası ile taşınabilme

##  Misafir Eklentileri

Sanal makinenin daha etkin kullanımı için

-   Host-Guest arası özgür fare hareketi

-   Paylaşılan klasör oluşturabilme

-   Guest ekranını yeniden boyutlandırabilme

##  Misafir Eklentileri

Kurulum
:   -   Sanal makineye eklentilere sahip CD tak
            
            !text
            1   Sanal makineyi aç
            2   Aygıtlar
            3   Misafir eklentileri CD kalıbını ekle

    -   CD den çalıştır ve kur


#   Dizin Paylaştırma

##  Paylaştırılacak Dizin Ekleme

-   Sanal makinede misafir eklentileri kurulu olmalı

Dizin paylaştırma
:           !text
            1   Değişiklik yapılacak sanal makineyi seç
            2   Ayarlar
            3   Paylaşılan klasörler
            4   Yeni paylaşılan klasör ekle
            5   Klasör yolu ve adını gir

##  Paylaşılan Dizini Görme

Windows
:   	    !text
    	    1   Bilgisayarım sağ tık
    	    2   Ağ sürücüsüne bağlan
    	    3   Sürücü harfini seç
    	    4   Klasör olarak `\\vboxsvr\klasor_adi` yolunu gir
    	    5   Artık Bilgisayarım'da görebilirsin

Ubuntu
:           !sh
            $ sudo mount -t vboxsf paylasilan ~/sanal
            $ sudo mount -t vboxsf -o uid=1000,gid=1000 paylasilan ~/sanal

-   Ubuntu için komutlar sanal makinede verilmeli

#   Ağ Yapılandırması

##  Host Only

-   Gerçek makinede **sanal** anahtar oluşturulur

-   Sanal anahtara bağlanan sanal makineler

-   Haberleşme sanal makineler ve host arasında

-   İnternet erişimi yok

##  NAT

-   Sanal makineler aynı ağda

-   Host üzerinden internet erişimi var

-   Sanal makineler internete çıkarken host un IP sini kullanır

##  Bridge

-   Doğrudan host un ethernetine erişim

-   Gerçek bir makine gibi IP alıp birbirleriyle haberleşirler

-   İnternet erişimi var

##  Extension Pack

-   USB cihazları bağlantısı

-   Webcam bağlantısı

-   PXE - Preboot Execution Environment

.notes: Sanal makinenin çeşitli ağ protokollerini kullanarak açılması için gerekli dosyaların çağrılması

-   VRDP - VirtualBox Remote Desktop Protocol

.notes: Sanal makinelere uzak masaüstü bağlantısı yaparak yönetmek

##  Extension Pack

-   Uygun paketi [buradan][extensionpack] indir

Kurulum
:           !text
            1   Dosya
            2   Tercihler
            3   Uzantılar
            4   Paket ekle

[extensionpack]: https://www.virtualbox.org/wiki/Downloads

-   Bir sefer kurmak yeterli

#   Ekstra

##  Tek Tık ile Açma

	!text
	1   Sanal makineyi seç
	2   Makine
	3   Masaüstüne kısayol oluştur

-   VirtualBox ı açmana gerek kalmadı

##  Video Çekme

	!text
	1   Sanal makineyi seç
	2   Ayarlar
	3   Ekran
	4   Görüntü yakalama
	5   Görüntü yakalamayı etkinleştir

