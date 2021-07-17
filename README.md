
# Django School

This a small backend coding in Django

## Authors

- [@Ramcode23](https://github.com/Ramcode23)

  
## Tech Stack

**Server:** Python, Django REST framework

  
## ERD

![App Screenshot](https://github.com/Ramcode23/schoolApp/blob/main/doc/djangoschool2.png?text=App+Screenshot+Here)

  
## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

  
