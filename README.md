# Biyografi Sitesi 📖

Bu proje, Django ile geliştirilmiş basit bir biyografi web sitesidir. Şairler, müzisyenler, sporcular gibi farklı kategorilerdeki ünlü kişilerin biyografilerini listeler ve detaylarını gösterir.

## Proje Yapısı 🏗️

- `biyografiapp/`: Projenin ana yapılandırma dosyalarını (settings.py, urls.py) içerir.
- `biyografiler/`: Biyografileri yöneten ana Django uygulamasıdır. Modelleri, view'ları ve şablonları içerir.
- `templates/`: Proje seviyesindeki ana şablonları barındırır.
- `manage.py`: Django projelerini yönetmek için kullanılan komut satırı aracıdır.
- `db.sqlite3`: Geliştirme için kullanılan SQLite veritabanı dosyasıdır.

## Kurulum ve Çalıştırma 🚀

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
