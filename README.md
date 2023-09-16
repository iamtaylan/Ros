# ROS UYGULAMALARI
- Eşkenar üçgen çizmek
- Lidar ile veri almak
- Kamera ile nesne tespiti yapıp ağırlık merkezi bulmak

## Eşkenar üçgen çizdirme uygulaması
### Proje Tanımı
ROS kullanarak turtlebot3 ile bir eşkenar üçgen çizdirmek ve kendimize özel msg dosyaları oluşturmak
### Msg Dosyaları
- Angle.msg
```python
float64 angle

```
- Length.msg
```python
float64 kenaruzunluk
```
### Arayüz
-PyQt5
![arayüz çıktısı][master/interface.png]

### Çalıştırma
- publisher.py dosyasını çalıştırarak eşkaner üçgenimizin uzunluğunu giriyoruz.
- ucgen_cizdirme_ui_3.py dosyasını çalıştırıyoruz.
- karşımıza çıkan arayüzde başlat butonuna basıyoruz ve turtlebot3 eşkenar üçgen çizmeye başlıyor

## Lidar Uygulaması
### Proje Tanımı
Lidar sensörü kullanarak engelleri tespit etmek bulunan engellere çarpmadan durabilmek ve kendimize özel msg dosyaları oluşturmak
### Eklenenler
- Geçen projede eksik olan hız mesaj dosyaları bu projede eklendi
### Msg Dosyaları
- Laser.msg
```python
std_msgs/Header header
float32 angle_min
float32 angle_max
float32 angle_increment
float32 time_increment
float32 scan_time
float32 range_min
float32 range_max
float32[] ranges
float32[] intensities
```
- Vector3.msg
```python
float64 x
float64 y
float64 z
```
- Rotate.msg
```python
Vector3 linear
Vector3 angular
```

###  Çalıştırma
- İlk olarak publisher_lidar.py dosyamızı çalıştırıyoruz ve robotumuzun ilerlemek istediği hızı belirliyoruz
- İkinci olarak lidar_scan.py dosyamızı çalıştırıyoruz ve robot karşısına belirli bir engel çıkana kadar belirlediğimiz hızda ilerliyor.

### Eksikler
- Planlanan Arayüz karşılaşılan hatalar yüzünden tamamlanamadı(güncellicek..) 








