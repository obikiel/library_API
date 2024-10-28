## Library Management API Documentation

### Base URL:
`https://obiomalibrary-azdxdsgfhde7hhfe.canadacentral-01.azurewebsites.net/crudfunction/api/v1/books/`

---

## 1. Get All Books
- **Endpoint:** `GET /api/v1/books`
- **Description:** Retrieve a list of all books in the library.
- **Request Parameters:** None
- **Response Example:**
  ```json
  {
    "status": "success",
    "code": 200,
    "message": "Books retrieved successfully",
    "data": {
      "books": [
        {
          "id": 1,
          "title": "Django for Beginners",
          "author": "John Doe",
          "genre": "Programming",
          "publication_date": "2021-05-15",
          "availability": true,
          "edition": "1st",
          "summary": "An introductory guide to Django."
        },

      ]
    }
  }
  ```

## 2. Add a New Book
- **Endpoint:** `POST /api/v1/books`
- **Description:** Add a new book to the library collection.

### Request Body Parameters:
- **title** (string): The title of the book. **Required**
- **author** (string): The author of the book. **Required**
- **genre** (string): Genre or category of the book. **Required**
- **publication_date** (string, date format YYYY-MM-DD): Publication date of the book. **Required**
- **availability** (boolean): Availability status of the book (default is true). **Optional**
- **edition** (string): Edition of the book. **Optional**
- **summary** (string): A brief summary of the book. **Optional**

#### Example Request Body:
```json
{
  "title": "Learning Django",
  "author": "Jane Smith",
  "genre": "Educational",
  "publication_date": "2021-05-15",
  "availability": true,
  "edition": "2nd",
  "summary": "A book for mastering Django."
}
```

## 3. Get Book Details by ID
- **Endpoint:** `GET /api/v1/books/<book_id>`
- **Description:** Retrieve detailed information for a specific book by its ID.

### URL Parameter:
- **book_id** (integer): ID of the book to retrieve.

#### Response Example:
```json
{
  "status": "success",
  "code": 200,
  "message": "Book details retrieved successfully",
  "data": {
    "book": {
      "id": 1,
      "title": "Django for Beginners",
      "author": "John Doe",
      "genre": "Programming",
      "publication_date": "2021-05-15",
      "availability": true,
      "edition": "1st",
      "summary": "An introductory guide to Django."
    }
  }
}
```
## 4. Update a Book
- **Endpoint:** `PUT /api/v1/books/<book_id>`
- **Description:** Update the details of a specific book, including its availability status.

### URL Parameter:
- **book_id** (integer): ID of the book to update.

### Request Body Parameters:
Any of the fields used in creating a new book can be updated.

#### Example Request Body:
```json
{
  "title": "Advanced Django",
  "availability": false
}
```
## 5. Delete a Book
- **Endpoint:** `DELETE /api/v1/books/<book_id>`
- **Description:** Delete a specific book from the library when it is lost, damaged, or no longer available.

### URL Parameter:
- **book_id** (integer): ID of the book to delete.

#### Response Example:
```json
{
  "status": "success",
  "code": 204,
  "message": "Book deleted successfully",
  "data": {}
}

