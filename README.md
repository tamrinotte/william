# WILLIAM
![WilliamLogo](https://raw.githubusercontent.com/tamrinotte/william/main/app_images/William%20Logo.png)

A command line tool to create a word list from combination of words.

<br>

## INSTALLATION

1) Download the installer.

       curl -L https://github.com/tamrinotte/william/releases/download/debian_v1/william.deb -o william.deb

2) Start the installer.

       sudo dpkg -i william.deb

<br>

## OPTIONS

__-h, --help:__ Show the help page.

__-v, --version:__ Show the app version.

__-min, --minimum:__ Minimum number of words in a combination.

__-max, --maximum:__  Maximum number of words in a combination.

__-c, --capitalize:__ Capitalize the first letter of each word in a combination.
		
__-f, --firstword:__ Capitalize the first letter of the first word in each combination.

<br>

## Examples

1)
       william -min 2 -max 3 wordlist.txt output.txt

2)
       william -min 2 -max 3 -c wordlist.txt output.txt

3)
       william -min 2 -max 3 -f wordlist.txt output.txt

---

<br>

# WILLIAM
![WilliamLogo](https://raw.githubusercontent.com/tamrinotte/william/main/app_images/William%20Logo.png)

Kelimelerin kombinasyonlarından kelime listesi oluşturmak için bir komut satırı uygulaması.

<br>

## YÜKLEME

1) Yükleyiciyi indir.

       curl -L https://github.com/tamrinotte/william/releases/download/debian_v1/william.deb -o william.deb

2) Yükleyiciyi başlat.

       sudo dpkg -i william.deb

<br>

## ARGÜMANLAR

__-h, --help:__ Yardım saysfasını görüntüle.

__-v, --version:__ Uygulama versiyonunu görüntüle.

__-min, --minimum:__ Kombinasyondaki her kelimenin ilk harfini büyük yapın.

__-max, --maximum:__  Bir kombinasyondaki maksimum kelime sayısı.

__-c, --capitalize:__ Herbir alt kelimenin ilk harfini büyük harfle yaz.
		
__-f, --firstword:__ Capitalize the first letter of the first word in each combination.

<br>

## Örnekler

1)
       william -min 2 -max 3 wordlist.txt output.txt

2)
       william -min 2 -max 3 -c wordlist.txt output.txt

3)
       william -min 2 -max 3 -f wordlist.txt output.txt