# Discord Bot Kurulum Rehberi

Bu rehber, Discord botunuzu kendi bilgisayarınızda çalıştırmak için gerekli adımları içerir.

## 1. Gereksinimler

- Python 3.8 veya üzeri
- Discord hesabı ve sunucusu

## 2. Kurulum Adımları

### Adım 1: Python Kurulumu
1. Python'u indirin: https://python.org/downloads/
2. Kurulum sırasında "Add to PATH" seçeneğini işaretleyin

### Adım 2: Dosyaları Hazırlama
1. Bot dosyalarını istediğiniz klasöre çıkarın
2. Komut satırında (CMD/Terminal) bot klasörüne gidin:
   ```
   cd discord_bot_export
   ```

### Adım 3: Gerekli Paketleri Yükleyin
```bash
pip install -r requirements.txt
```

### Adım 4: Bot Token'ını Ayarlayın
1. `.env` dosyasını metin editörüyle açın
2. `DISCORD_TOKEN=` kısmından sonra bot token'ınızı yapıştırın
3. Dosyayı kaydedin

### Adım 5: Botu Çalıştırın
```bash
python main.py
```

## 3. Bot Komutları

### Moderasyon Komutları (Prefix: .)
- `.ban @kullanıcı [sebep]` - Kullanıcıyı yasaklar
- `.unban kullanıcı_id` - Yasağı kaldırır
- `.kick @kullanıcı [sebep]` - Kullanıcıyı atar
- `.mute @kullanıcı [süre] [sebep]` - Kullanıcıyı susturur
- `.unmute @kullanıcı` - Susturmayı kaldırır

### Mesajlaşma Komutları
- `.yaz #kanal mesaj` - Belirtilen kanala mesaj gönderir
- `.herkeseyaz mesaj` - Herkese DM gönderir

### Sunucu Yönetimi (Sadece Kurucu)
- `.imha` - Sunucuyu imha eder
- `.gerigetir` - Sunucuyu geri yükler

### Yardım
- `.yardım` - Tüm komutları gösterir

## 4. Sorun Giderme

### Bot bağlanmıyor:
- Token'ın doğru olduğundan emin olun
- Bot'un sunucunuza eklendiğinden emin olun

### Komutlar çalışmıyor:
- Bot'un gerekli yetkilere sahip olduğundan emin olun
- Prefix'in doğru olduğundan emin olun (.)

### Yetkiler:
Bot için gerekli yetkiler:
- Mesajları Yönet
- Kullanıcıları Yasakla
- Kullanıcıları At
- Rolleri Yönet
- Kanalları Yönet

## 5. Önemli Notlar

- Bot çalışmaya devam etmesi için komut satırı açık kalmalı
- Sunucuyu kapatırsanız bot çalışmayı durduracak
- Yedekleme sistemi `data/backups/` klasöründe çalışır
- Susturulan kullanıcılar `data/muted_users.json` dosyasında saklanır

## 6. 24/7 Çalıştırma

Bot'u 24/7 çalıştırmak için:
1. VPS/Cloud sunucu kiralayın
2. Dosyaları sunucuya yükleyin
3. Screen veya tmux kullanarak arka planda çalıştırın:
   ```bash
   screen -S discord_bot
   python main.py
   # Ctrl+A, D tuşlarıyla çıkın
   ```

Bot artık Replit'e bağlı değil ve kendi sunucunuzda çalışacak!