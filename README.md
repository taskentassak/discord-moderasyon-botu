# Discord Moderasyon Botu

Bu bot, Discord sunucuları için kapsamlı moderasyon, mesajlaşma ve sunucu yönetimi araçları sunar.

## Özellikler

### 🛡️ Moderasyon Komutları
- **Ban**: Kullanıcıları sunucudan yasaklar
- **Unban**: Kullanıcıların yasağını kaldırır
- **Kick**: Kullanıcıları sunucudan atar
- **Mute**: Kullanıcıları geçici veya kalıcı olarak susturur
- **Unmute**: Kullanıcıların susturmasını kaldırır

### 💬 Mesajlaşma Komutları
- **Yaz**: Belirtilen kanala mesaj gönderir
- **Herkeseyaz**: Sunucudaki tüm kullanıcılara DM gönderir (çekilişler için)

### ⚙️ Sunucu Yönetimi (Sadece Kurucu)
- **İmha**: Sunucuyu tamamen imha eder (kanalları siler, davetleri iptal eder)
- **Gerigetir**: Sunucuyu son yedekten geri yükler

## Kurulum

### Gereksinimler
```bash
pip install discord.py python-dotenv
```

### Kurulum Adımları

1. **Botunuzu Discord Developer Portal'da oluşturun**
   - https://discord.com/developers/applications adresine gidin
   - Yeni aplikasyon oluşturun
   - Bot sekmesinden token alın

2. **Token'ı ayarlayın**
   - `.env` dosyasını oluşturun
   - Token'ınızı ekleyin:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```

3. **Botu çalıştırın**
   ```bash
   python main.py
   ```

## Komutlar

### Moderasyon (Prefix: .)
- `.ban @kullanıcı [sebep]` - Kullanıcıyı yasaklar
- `.unban kullanıcı_id` - Yasağı kaldırır
- `.kick @kullanıcı [sebep]` - Kullanıcıyı atar
- `.mute @kullanıcı [süre] [sebep]` - Kullanıcıyı susturur
- `.unmute @kullanıcı` - Susturmayı kaldırır

### Mesajlaşma
- `.yaz #kanal mesaj` - Belirtilen kanala mesaj gönderir
- `.herkeseyaz mesaj` - Herkese DM gönderir

### Sunucu Yönetimi (Sadece Kurucu)
- `.imha` - Sunucuyu imha eder
- `.gerigetir` - Sunucuyu geri yükler
- `.yedekle` - Manuel yedek oluşturur

### Yardım
- `.yardım` - Tüm komutları gösterir

## Dosya Yapısı

```
/
├── main.py                 # Ana bot dosyası
├── .env                    # Token ve ayarlar
├── requirements.txt        # Python gereksinimleri
├── commands/
│   ├── moderation.py       # Moderasyon komutları
│   ├── messaging.py        # Mesajlaşma komutları
│   └── server_management.py # Sunucu yönetimi
├── utils/
│   ├── backup.py           # Yedekleme sistemi
│   └── permissions.py      # Yetki kontrolü
├── config/
│   └── settings.py         # Bot ayarları
└── data/
    ├── muted_users.json    # Susturulan kullanıcılar
    └── backups/            # Sunucu yedekleri
```

## Güvenlik

- Tüm komutlar uygun yetki kontrolü ile korunur
- Sunucu imha işlemi sadece kurucu tarafından yapılabilir
- Yedekleme sistemi otomatik olarak çalışır
- Rol hiyerarşisi kontrol edilir

## Destek

Bot tamamen Türkçe arayüze sahiptir ve Discord.py 2.5.2 ile uyumludur.