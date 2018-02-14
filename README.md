# hangul-test
A hangul learning/testing app written in python

Works on the full unicode set from characters 44032 to 55203 ([hangul unicode table](http://jrgraphix.net/r/Unicode/AC00-D7AF)), which may contain obsolete characters. I need to investigate whether this is true and filter them out to only print those currently in use.

The script uses the [kroman](https://github.com/zhangkaiyulw/kroman-py) parsing library, which uses [a phonetic mapping table](https://github.com/zhangkaiyulw/kroman-py/blob/master/kroman/__init__.py) without any special considerations (e.g. 씨 is seen as "ssi" rather than "shi"). I think this is fine for the purposes of learning and revisions drills.

The resulting app is very simple and may mark some correct answers as incorrect. Hopefully you're OK knowing you were right when the app insists you weren't :blush:.

![hangul-test image](https://github.com/sharktamer/hangul-test/raw/master/hangul-test.gif)
