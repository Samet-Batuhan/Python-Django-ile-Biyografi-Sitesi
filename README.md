# Diyetisyen ve Yemek Uygulaması

Bu proje, diyetisyenler ve sağlıklı beslenmek isteyen kullanıcılar için geliştirilmiş bir web uygulamasıdır. Kullanıcıların yemek tariflerini görüntülemesine, diyet programlarına erişmesine, diyetisyenlerden randevu almasına ve çeşitli sağlık hesaplamaları yapmasına olanak tanır.

## Özellikler

- **Kullanıcı ve Diyetisyen Rolleri:** Sistemde normal kullanıcılar ve diyetisyenler (admin/süper kullanıcı) için ayrı giriş mekanizmaları bulunmaktadır.
- **Yemek Tarifleri:** Kategorilere ayrılmış, detaylı yemek tarifleri ve görselleri. URL'den otomatik tarif bilgisi çekme özelliği.
- **Diyet Programları:** Kullanıcıların takip edebileceği çeşitli diyet programları.
- **Randevu Sistemi:** Kullanıcılar sistemdeki diyetisyenlerden randevu talep edebilir ve talepleri diyetisyenin e-posta adresine iletilir.
- **Sağlık Hesaplayıcıları:**
  - Vücut Kitle İndeksi (VKİ)
  - Bazal Metabolizma Hızı (BMH)
  - Vücut Yağ Oranı
  - İdeal Kilo
  - Günlük Kalori İhtiyacı
- **Yorum Sistemi:** Kullanıcılar uygulama hakkında yorum yapabilir.
- **İletişim Formu:** Kullanıcıların site yönetimi ile iletişime geçmesi için bir form.
- **Yönetim Paneli:** Diyetisyenlerin kullanıcıları, randevuları ve diyet programlarını yönetebileceği bir arayüz.

## Kullanılan Teknolojiler

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript (Django Template Engine ile)
- **Veritabanı:** SQLite 3
- **Kütüphaneler:**
  - `django-ckeditor`: Zengin metin editörü için.

## Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1.  **Projeyi Klonlayın:**
    ```bash
    git clone <repository-url>
    cd <proje-dizini>
    ```

2.  **Sanal Ortam Oluşturun ve Aktif Edin:**
    ```bash
    # Windows için
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux için
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Gerekli Paketleri Yükleyin:**
    Bir `requirements.txt` dosyası oluşturup aşağıdaki paketleri ekleyin:
    ```
    Django
    django-ckeditor
    ```
    Ardından paketleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Veritabanı Kurulumu:**
    ```bash
    python manage.py migrate
    ```

5.  **Süper Kullanıcı (Diyetisyen/Admin) Oluşturun:**
    ```bash
    python manage.py createsuperuser
    ```
    İstenecek olan kullanıcı adı, e-posta ve şifre bilgilerini girin.

6.  **Geliştirme Sunucusunu Başlatın:**
    ```bash
    python manage.py runserver
    ```

Uygulama artık `http://127.0.0.1:8000/` adresinde çalışıyor olacaktır.
- **Admin/Diyetisyen Girişi:** `http://127.0.0.1:8000/account/diyetisyen/login`
- **Normal Kullanıcı Girişi:** `http://127.0.0.1:8000/account/login/`
- **Django Admin Paneli:** `http://127.0.0.1:8000/admin/` 
