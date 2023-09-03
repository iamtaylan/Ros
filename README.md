# Proje Tanımı

ROS kullanarak turtlebot3 ile bir eşkenar üçgen çizdirmek ve kendimize özel msg dosyaları oluşturmak

## Msg Dosyaları
- Angle.msg
```python
float64 angle

```
- Length.msg
```python
float64 kenaruzunluk
```
## Arayüz
-PyQt5
![arayüz çıktısı][master/interface.png]

## Çalıştırma
- publisher.py dosyasını çalıştırarak eşkaner üçgenimizin uzunluğunu giriyoruz.
- ucgen_cizdirme_ui_3.py dosyasını çalıştırıyoruz.
- karşımıza çıkan arayüzde başlat butonuna basıyoruz ve turtlebot3 eşkenar üçgen çizmeye başlıyor
