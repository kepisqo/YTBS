# YTBS
TEİAŞ yük tevzi bilgi sistemine saatlik olarak girilmesi gereken endex verilerini otomatik olarak giren uygulama

## Genel Bakış
Selenium kütüphanesi kullanılarak chrome üzerinden [YTBS](https://ytbs.teias.gov.tr/ytbs/frm_login.jsf) sistemine login olunur,
girilmesi gereken sıradaki saat bilgisi alınır. Uygulama sıradaki saatin gelmesini bekler, saat geldiğinde Wincc programının anlık
olarak excele yazdığı endex verilerini alarak önce kendi tuttuğu excele kaydeder, daha sonrasında tekrar sisteme login olarak endex
verilerini sisteme kaydeder. Akabinde program tamamlanır ve tekrar başa döner.

### Gerekli Kütüphaneler
Uygulamayı kullanabilmek için aşağıdaki kütphaneleri pip ile kurun.
```console
$ pip install selenium
```
Selenium kütüphanesi tarayıcıyı otomatik olarak kullanmaya yarar. Tarayıcıyı selenium ile kullanabilmek için
Chorme sürümünüzle uyumlu olan [Driverı](https://sites.google.com/chromium.org/driver/) indirmelisiniz.

```console
$ pip install xlrd
```
xlrd ile .xls uzantılı excel dosyasından veri okunur.

```console
$ pip install xlwt
```
xlwt ile .xls uzantılı excel dosyasına veri yazılır.

```console
$ pip install logging
```
Son olarak logging kütüphanesi ile log dosyasına log kayıtları yazılır.

## License

Ytbs is released under the [MIT License](LICENSE).
