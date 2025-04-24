from django.core.management.base import BaseCommand
from product_management.models import Brand, ProductSku, ProductListing
from datetime import datetime

class Command(BaseCommand):
    help = 'Seeds the database with dummy data for testing'

    def handle(self, *args, **kwargs):
        # Clear existing data
        ProductListing.objects.all().delete()
        ProductSku.objects.all().delete()
        Brand.objects.all().delete()

        # Create Brands
        brands = [
            Brand(
                name="Nike",
                onboarded_at=datetime(2023, 1, 1),
                profile_pic_url="https://example.com/nike.jpg",
                status="active",
                metadata={"description": "Sportswear brand"}
            ),
            Brand(
                name="Adidas",
                onboarded_at=datetime(2023, 2, 1),
                profile_pic_url="https://example.com/adidas.jpg",
                status="active",
                metadata={"description": "Athletic apparel"}
            ),
            Brand(
                name="Puma",
                onboarded_at=datetime(2023, 3, 1),
                profile_pic_url="https://example.com/puma.jpg",
                status="inactive",
                metadata={"description": "Footwear brand"}
            ),
            Brand(
                name="Reebok",
                onboarded_at=datetime(2023, 4, 1),
                profile_pic_url="https://example.com/reebok.jpg",
                status="active",
                metadata={"description": "Fitness gear"}
            ),
        ]
        Brand.objects.bulk_create(brands)
        self.stdout.write(self.style.SUCCESS('Successfully created 4 Brands'))

        # Create Product SKUs
        nike = Brand.objects.get(name="Nike")
        adidas = Brand.objects.get(name="Adidas")
        puma = Brand.objects.get(name="Puma")
        reebok = Brand.objects.get(name="Reebok")

        product_skus = [
            ProductSku(
                brand=nike,
                product_url="https://nike.com/air-max-270",
                parentage="shoes",
                name="Air Max 270",
                mfn_sku="AM270-BLK-10",
                case_quantity=60,
                upc_gtin="test12346",
                asin="testasin1",
                epic_purchase_cost={"value": 89.99, "unit": "USD"},
                contracted_sell_price={"value": 89.99, "unit": "USD"},
                retail_price={"value": 129.99, "unit": "USD"},
                lead_time=14,
                weight={"unit": "lbs", "value": 1.5},
                dimensions={"unit": "in", "width": 10, "height": 5, "length": 12},
                status="active",
                metadata={
                    "packaging_weight": {"unit": "lbs", "value": 2},
                    "packaging_dimensions": {"unit": "in", "width": 11, "height": 6, "length": 13}
                },
                is_active=True
            ),
            ProductSku(
                brand=adidas,
                product_url="https://adidas.com/ultraboost",
                parentage="shoes",
                name="Ultraboost 21",
                mfn_sku="UB21-WHT-9",
                case_quantity=50,
                upc_gtin="test12347",
                asin="testasin2",
                epic_purchase_cost={"value": 99.99, "unit": "USD"},
                contracted_sell_price={"value": 99.99, "unit": "USD"},
                retail_price={"value": 149.99, "unit": "USD"},
                lead_time=10,
                weight={"unit": "lbs", "value": 1.2},
                dimensions={"unit": "in", "width": 9, "height": 4, "length": 11},
                status="active",
                metadata={
                    "packaging_weight": {"unit": "lbs", "value": 1.8},
                    "packaging_dimensions": {"unit": "in", "width": 10, "height": 5, "length": 12}
                },
                is_active=True
            ),
            ProductSku(
                brand=puma,
                product_url="https://puma.com/rs-x",
                parentage="shoes",
                name="RS-X Bold",
                mfn_sku="RSX-BLD-8",
                case_quantity=40,
                upc_gtin="test12348",
                asin="testasin3",
                epic_purchase_cost={"value": 79.99, "unit": "USD"},
                contracted_sell_price={"value": 79.99, "unit": "USD"},
                retail_price={"value": 119.99, "unit": "USD"},
                lead_time=12,
                weight={"unit": "lbs", "value": 1.3},
                dimensions={"unit": "in", "width": 9, "height": 5, "length": 11},
                status="inactive",
                metadata={
                    "packaging_weight": {"unit": "lbs", "value": 1.9},
                    "packaging_dimensions": {"unit": "in", "width": 10, "height": 5, "length": 12}
                },
                is_active=False
            ),
            ProductSku(
                brand=reebok,
                product_url="https://reebok.com/classic-leather",
                parentage="shoes",
                name="Classic Leather",
                mfn_sku="CL-LTHR-11",
                case_quantity=30,
                upc_gtin="test12349",
                asin="testasin4",
                epic_purchase_cost={"value": 69.99, "unit": "USD"},
                contracted_sell_price={"value": 69.99, "unit": "USD"},
                retail_price={"value": 99.99, "unit": "USD"},
                lead_time=15,
                weight={"unit": "lbs", "value": 1.4},
                dimensions={"unit": "in", "width": 8, "height": 4, "length": 10},
                status="active",
                metadata={
                    "packaging_weight": {"unit": "lbs", "value": 1.7},
                    "packaging_dimensions": {"unit": "in", "width": 9, "height": 5, "length": 11}
                },
                is_active=True
            ),
        ]
        ProductSku.objects.bulk_create(product_skus)
        self.stdout.write(self.style.SUCCESS('Successfully created 4 Product SKUs'))

        # Create Product Listings
        sku1 = ProductSku.objects.get(name="Air Max 270")
        sku2 = ProductSku.objects.get(name="Ultraboost 21")
        sku3 = ProductSku.objects.get(name="RS-X Bold")
        sku4 = ProductSku.objects.get(name="Classic Leather")

        product_listings = [
            ProductListing(
                epic_sku_id="EPIC-AM270-001",
                product_sku_id=sku1,
                marketplace="amazon",
                country="usa",
                status="live",
                epic_status="active",
                metadata={}
            ),
            ProductListing(
                epic_sku_id="EPIC-AM270-002",
                product_sku_id=sku1,
                marketplace="walmart",
                country="usa",
                status="pending",
                epic_status="pending",
                metadata={}
            ),
            ProductListing(
                epic_sku_id="EPIC-UB21-001",
                product_sku_id=sku2,
                marketplace="amazon",
                country="canada",
                status="live",
                epic_status="active",
                metadata={}
            ),
            ProductListing(
                epic_sku_id="EPIC-RSX-001",
                product_sku_id=sku3,
                marketplace="ebay",
                country="usa",
                status="inactive",
                epic_status="inactive",
                metadata={}
            ),
            ProductListing(
                epic_sku_id="EPIC-CLLTHR-001",
                product_sku_id=sku4,
                marketplace="amazon",
                country="uk",
                status="live",
                epic_status="active",
                metadata={}
            ),
        ]
        ProductListing.objects.bulk_create(product_listings)
        self.stdout.write(self.style.SUCCESS('Successfully created 5 Product Listings'))