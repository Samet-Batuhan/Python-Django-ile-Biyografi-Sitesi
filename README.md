# Biyografi Sitesi

Bu proje, Django ile geliştirilmiş basit bir biyografi web sitesidir. Şairler, müzisyenler, sporcular gibi farklı kategorilerdeki ünlü kişilerin biyografilerini listeler ve detaylarını gösterir.

## Proje Yapısı

- `biyografiapp/`: Projenin ana yapılandırma dosyalarını (settings.py, urls.py) içerir.
- `biyografiler/`: Biyografileri yöneten ana Django uygulamasıdır. Modelleri, view'ları ve şablonları içerir.
- `templates/`: Proje seviyesindeki ana şablonları barındırır.
- `manage.py`: Django projelerini yönetmek için kullanılan komut satırı aracıdır.
- `db.sqlite3`: Geliştirme için kullanılan SQLite veritabanı dosyasıdır.

## Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1.  **Projeyi Klonlayın:**
    ```bash
    git clone <repository-url>
    cd <proje-klasoru>
    ```

2.  **Sanal Ortam Oluşturun ve Aktif Edin:**
    ```bash
    python -m venv venv
    # Windows için
    venv\Scripts\activate
    # macOS/Linux için
    source venv/bin/activate
    ```

3.  **Bağımlılıkları Yükleyin:**
    Proje `Django`, `requests`, `lxml` ve `beautifulsoup4` kütüphanelerini kullanmaktadır.
    ```bash
    pip install Django requests lxml beautifulsoup4
    ```

4.  **Veritabanı Geçişlerini (Migrations) Uygulayın:**
    ```bash
    python manage.py migrate
    ```

5.  **Geliştirme Sunucusunu Başlatın:**
    ```bash
    python manage.py runserver
    ```
    Sunucu varsayılan olarak `http://127.0.0.1:8000/` adresinde çalışacaktır.

## Geliştirme Önerileri

Mevcut proje işlevsel olsa da, kod tekrarını azaltmak ve bakımı kolaylaştırmak için aşağıdaki iyileştirmeler yapılabilir:

- **Modellerin Yeniden Düzenlenmesi:** `Sair`, `Muzisyen`, `Sporcu` gibi tekrar eden modelleri, kategori ile ilişkilendirilmiş tek bir `Kisi` modelinde birleştirmek.
- **View'ların Yeniden Düzenlenmesi:** Her kategori için ayrı olan listeleme ve detay view'larını, URL'den kategori veya kişi kimliği alarak çalışan genel (generic) view'lara dönüştürmek.
- **Kullanılmayan Kodun Temizlenmesi:** Projenin ana işlevselliğiyle ilgisiz görünen `Link` modeli ve ilgili `home_view`, form ve şablonların kaldırılması.
- **Hataların Giderilmesi:** `hakkinda` view'ındaki hatanın ve `kisidetay` view'ının tüm kişi türleri için doğru çalışmasının sağlanması. 
