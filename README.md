## Stock Checker

This stock checker is dedicated specifically to <code>Nvidia 30 Series GPUs</code>, <code>AMD 6000 Series GPUs</code> and <code>AMD 5000 Series CPUs</code> but it can be used for other products also. It comes with some common **United Kingdom** stores built in the <a href="stores.json">stores.json</a> file.

## Quick start

Stock Checker runs on Python 3.X.X:

```shell
git clone https://github.com/conorvenus/StockChecker
cd StockChecker
py main.py
```

## Customisation

⚠️ Customising this Stock Checker is primarily targeted at experienced programmers who understand the json file format.

Open the <a href="stores.json">stores.json</a> file and add a new store object to the array:

### Structure of the Store Object

```json
{
  "name": "",
  "url": "",
  "method": "",
  "card_name": "",
  "country": "",
  "webscraping": {
    "product": {
      "type": "",
      "data_type": "",
      "class": ""
    },
    "title": {
      "type": "",
      "data_type": "",
      "data-product": ""
    },
    "url": {
      "type": "",
      "data_type": "",
      "class": "",
      "append_base_url": false
    },
    "stock_identifier": {
      "type": "",
      "data_type": "",
      "class": "",
      "outofstock": true
    }
  }
}
```
