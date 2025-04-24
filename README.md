# Product Management API

A Django-based REST API project designed to manage product-related data, including brands, product SKUs, and product listings. The API provides endpoints to retrieve product SKU information with pagination support.

## Project Structure

```
project_folder
  |-- main_project_folder
  |   |-- settings.py
  |   |-- urls.py
  |-- product_management
  |   |-- __init__.py
  |   |-- models.py
  |   |-- views.py
  |   |-- urls.py
  |   |-- serializers.py
  |   |-- management
  |       |-- __init__.py
  |       |-- commands
  |           |-- __init__.py
  |           |-- seed.py
  |-- manage.py
  |-- requirements.txt
```

## Prerequisites

- Python 3.8+
- Django 4.x
- Django REST Framework

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd project_folder
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   
   Ensure requirements.txt includes:
   ```
   django>=4.0
   djangorestframework
   ```
   
   Update and install:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the project:**
   - Update `main_project_folder/settings.py` with your database settings (e.g., SQLite by default or PostgreSQL for JSONB support)
   - Ensure `INSTALLED_APPS` includes 'product_management' and 'rest_framework'

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Seed dummy data (optional):**
   ```bash
   python manage.py seed
   ```

## Running the Project

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the API:**
   - Endpoint: `http://127.0.0.1:8000/product_management/skus/`
   - Query parameters:
     - `page`: Page number (default: 1)
     - `limit`: Number of items per page (default: 10, max: 100)

## API Response Structure

The API returns a JSON response with the following structure:

```json
{
  "sku": [
    {
      "parentage": "string",
      "mfn_sku": "string",
      "sku_name": "string",
      "country": "string",
      "epic_purchase_cost": {
        "value": number,
        "unit": "string"
      },
      "contracted_sell_price": {
        "value": number,
        "unit": "string"
      },
      "case_quantity": number,
      "upc_gtin": "string",
      "retail_price": {
        "value": number,
        "unit": "string"
      },
      "asin": "string",
      "lead_time": number,
      "weight": {
        "unit": "string",
        "value": number
      },
      "dimensions": {
        "unit": "string",
        "width": number,
        "height": number,
        "length": number
      },
      "packaging_weight": {
        "unit": "string",
        "value": number
      },
      "packaging_dimensions": {
        "unit": "string",
        "width": number,
        "height": number,
        "length": number
      },
      "marketplaces": [
        {
          "status": "string",
          "marketplace": "string"
        }
      ]
    }
  ],
  "page": number,
  "limit": number,
  "total_page_count": number,
  "total_record_count": number
}
```

## Models

- **Brand**: Represents a brand entity with fields like name, onboarded_at, profile_pic_url, status, and metadata.
- **ProductSku**: Represents a product SKU with fields like brand, parentage, name, mfn_sku, case_quantity, upc_gtin, asin, and various JSON fields (e.g., epic_purchase_cost, weight).
- **ProductListing**: Represents a product listing with fields like epic_sku_id, product_sku_id, marketplace, country, status, and metadata.

## Seeding Dummy Data

The `seed.py` management command creates:

- 4 Brand records (e.g., Nike, Adidas, Puma, Reebok)
- 4 ProductSku records (e.g., Air Max 270, Ultraboost 21, RS-X Bold, Classic Leather)
- 5 ProductListing records linking SKUs to marketplaces (e.g., Amazon, Walmart)

Run `python manage.py seed` to populate the database.

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch`
3. Make changes and commit: `git commit -m "Description of changes"`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request

## Contact

For questions or support, contact jayagma032@example.com