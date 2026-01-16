# Git Hızlı Kılavuz (CheatSheet)

Bu rehber, en sık kullanılan ve temel Git komutlarından başlayarak, daha ileri seviye özelliklere doğru sıralanmıştır.

## 1. Başlangıç (Kurulum ve Ayarlar)
Git'i kurduktan sonra yapmanız gereken ilk ayarlar.

Git'i kurmak için (Kimlik Bilgileri):
```bash
git config --global user.name "Adınız"
git config --global user.email "E-posta adresiniz"
```
Örnek:
```bash
git config --global user.name "AhmetYıldız"
git config --global user.email "ahmet@gofth.com"
```

Git'in yapılandırmasını görüntülemek için:
```bash
git config --list
```

## 2. Projeye Başlama (Depo Oluşturma)
Yeni bir projeye başlarken veya mevcut bir projeyi indirirken.

Yeni bir yerel depo oluşturmak için:
```bash
git init
```
Örnek:
```bash
git init yeni-projem
```

Var olan bir depoyu klonlamak (indirmek) için:
```bash
git clone <url>
```
Örnek:
```bash
git clone https://github.com/gofth/gofth-blog.git
```

## 3. Günlük Çalışma Döngüsü (En Önemli Komutlar)
Kod yazarken sürekli kullanacağınız temel komutlar.

Çalışma dizinindeki dosyaların durumunu görmek için:
```bash
git status
```

Yeni veya değiştirilmiş dosyaları izlemeye almak (Stage) için:
```bash
git add <dosya>
# veya tüm dosyalar için:
git add .
```
Örnek:
```bash
git add style.css
# veya
git add .
```

Değişiklikleri kaydetmek (Commit) için:
```bash
git commit -m "Mesaj"
```
Örnek:
```bash
git commit -m "Stil dosyası eklendi"
```

Uzak depodaki değişiklikleri indirip birleştirmek için (Güncelleme):
```bash
git pull <uzak> <dal>
```
Örnek:
```bash
git pull origin master
```

Yerel değişiklikleri uzak depoya göndermek için (Yükleme):
```bash
git push <uzak> <dal>
```
Örnek:
```bash
git push origin master
```

İzlenen dosyalardaki değişiklikleri detaylı görmek için:
```bash
git diff
```

## 4. Geçmişi Görüntüleme
Nelerin değiştiğini ve kimin ne yaptığını görmek için.

Commit geçmişini görmek için:
```bash
git log
```

Commit geçmişini tek satırda (özet) görmek için:
```bash
git log --oneline
```

Bir dosyanın geçmişini görmek için:
```bash
git log -p <dosya>
```

Bir dosyada kimin ne zaman ne yaptığını görmek için:
```bash
git blame <dosya>
```

## 5. Değişiklikleri Geri Alma
Hata yaptığınızda geri dönmek için.

Bir dosyadaki (kaydedilmemiş) değişiklikleri geri almak için:
```bash
git checkout -- <dosya>
```

Son commiti geri almak ve değişiklikleri korumak için:
```bash
git reset --soft HEAD~1
```

Son commiti geri almak ve değişiklikleri silmek için (DİKKAT!):
```bash
git reset --hard HEAD~1
```

Son commiti değiştirmek için (mesajı veya unutulan dosyayı eklemek):
```bash
git commit --amend
```

## 6. Dal (Branch) Yönetimi
Farklı özellikler üzerinde aynı anda çalışmak için.

Mevcut dalları listelemek için:
```bash
git branch
```

Yeni bir dal oluşturmak için:
```bash
git branch <dal>
```

Başka bir dala geçmek için:
```bash
git checkout <dal>
```

Yeni bir dal oluşturup ona geçmek için:
```bash
git checkout -b <dal>
```
Örnek:
```bash
git checkout -b yeni-dal
```

Bir dalı silmek için:
```bash
git branch -d <dal>
```

## 7. Birleştirme (Merge) ve Çakışmalar
Farklı dallardaki çalışmaları birleştirmek için.

Bir dalı mevcut dala birleştirmek için:
```bash
git merge <dal>
```

Birleştirme çakışmalarını çözmek için:
> Çakışan dosyaları düzenleyin ve `git add <dosya>` ile işaretleyin. Sonra commit atın.

Bir dalın commitlerini mevcut dalın üzerine eklemek için (Rebase):
```bash
git rebase <dal>
```

## 8. İleri Seviye ve Diğer Komutlar

### Uzak (Remote) Depo Yönetimi
Uzak depoları listelemek için:
```bash
git remote -v
```

Yeni bir uzak depo eklemek için:
```bash
git remote add <isim> <url>
```
Örnek:
```bash
git remote add origin git@github.com:gofth/gofth-blog.git
```

Uzak depoyu kaldırmak için:
```bash
git remote rm <uzak>
```

### Stash (Geçici Saklama)
Çalışma dizinindeki değişiklikleri saklamak için:
```bash
git stash
```

Saklanan değişiklikleri geri yüklemek için:
```bash
git stash pop
```

### Etiket (Tag) Yönetimi
Sürümleri etiketlemek için.
```bash
git tag v1.0
git push origin --tags
```

### Diğer İpuçları
Bir dosyayı veya klasörü yoksaymak için:
> `.gitignore` dosyasına yoksayılacak dosya veya klasörün adını yazın.

Git komutlarının yardım sayfalarını görmek için:
```bash
git help <komut>
```

---
**Kaynak:** [https://github.com/theomgdev/GIT-CheatSheet-Turkce](https://github.com/theomgdev/GIT-CheatSheet-Turkce)