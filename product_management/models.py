from django.db import models

# Model for the 'brand' table
class Brand(models.Model):
    id = models.AutoField(primary_key=True)  # INTEGER (Primary Key)
    name = models.CharField(max_length=255)  # varchar
    onboarded_at = models.DateTimeField()  # timestamp
    profile_pic_url = models.CharField(max_length=255)  # varchar
    status = models.CharField(max_length=50)  # ENUM
    metadata = models.JSONField(null=True, blank=True)  # jsonb

    def __str__(self):
        return self.name

# Model for the 'product_sku' table
class ProductSku(models.Model):
    id = models.AutoField(primary_key=True)  # INTEGER (Primary Key)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="product_skus")  # Foreign Key to Brand
    product_url = models.CharField(max_length=255)  # varchar
    parentage = models.CharField(max_length=50)  # varchar
    name = models.CharField(max_length=255)  # varchar
    mfn_sku = models.CharField(max_length=100)  # varchar
    case_quantity = models.IntegerField()  # integer
    upc_gtin = models.CharField(max_length=50)  # varchar
    asin = models.CharField(max_length=50)  # varchar
    epic_purchase_cost = models.JSONField(null=True, blank=True)  # jsonb
    contracted_sell_price = models.JSONField(null=True, blank=True)  # jsonb
    retail_price = models.JSONField(null=True, blank=True)  # jsonb
    lead_time = models.JSONField(null=True, blank=True)  # jsonb
    weight = models.JSONField(null=True, blank=True)  # jsonb
    dimensions = models.JSONField(null=True, blank=True)  # jsonb
    status = models.CharField(max_length=50)  # ENUM
    metadata = models.JSONField(null=True, blank=True)  # jsonb
    is_active = models.BooleanField(default=True)  # boolean

    def __str__(self):
        return self.name

# Model for the 'product_listing' table
class ProductListing(models.Model):
    id = models.AutoField(primary_key=True)  # INTEGER (Primary Key)
    epic_sku_id = models.CharField(max_length=100)
    product_sku_id = models.ForeignKey(ProductSku, on_delete=models.CASCADE, related_name="listings")  # Foreign Key to ProductSku
    marketplace = models.CharField(max_length=50)  # ENUM
    country = models.CharField(max_length=100)  # varchar
    status = models.CharField(max_length=50)  # ENUM
    epic_status = models.CharField(max_length=50)  # ENUM
    metadata = models.JSONField(null=True, blank=True)  # jsonb

    def __str__(self):
        return f"{self.product_sku_id.name} - {self.marketplace}"