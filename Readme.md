

## clone the repo

get the repo from github

```bash
git clone 

```

## install dependencies

```bash
pip install -r requirements.txt
```

## make migrations

```bash
python manage.py makemigrations
```

## migrate

```bash
python manage.py migrate
```

## run server

```bash
python manage.py runserver
```

## create superuser

```bash
python manage.py createsuperuser
```

## get the swagger d


```bash
http://127.0.0.1:8000/swagger/
```
You should see the swagger documentation for the api



For the authentication, you need to get the token from the login endpoint(/api-token-auth), if you have not create a super user you can till use /register to register account.

You shoud see the token in the response body, copy the token and click the authorize button on the top right corner of the swagger page, paste the token in the value field and click authorize. You should be able to access the other endpoints now. (paste the token with the word "Token" in front of it. for example "Token 1234567890abcdefg" )

There are inventorty-items api , you can create , update , delete and get the items.

Thre is supplier api, you can create , update , delete and get the suppliers.

and there is supplier-items api, you can create , update , delete and get the supplier-items.
You should have the supplier and inventory items created before you can create the supplier-items.
You can list inventory items by supplier id
 http://127.0.0.1:8000/api/v1/supplier-items/1/get_all_items_by_supplier/

ther response should be like this
```bash
[
  {
    "item": {
      "id": 1,
      "name": "shope",
      "description": "This shope is unique",
      "price": "23.00",
      "date_added": "2024-01-16T03:56:59.178160Z"
    }
  },
  {
    "item": {
      "id": 3,
      "name": "string",
      "description": "string",
      "price": "5.00",
      "date_added": "2024-01-16T06:17:55.665049Z"
    }
  }
]
```

you can also list suppliers by inventory item id
http://127.0.0.1:8000/api/v1/supplier-items/1/get_all_suppliers_of_item/

the response should be like this
```bash
[
  {
    "id": 1,
    "supplier": {
      "id": 1,
      "name": "sagar",
      "contact_information": "9841924580"
    }
  }
]

```





