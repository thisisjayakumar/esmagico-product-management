from rest_framework import serializers
from product_management.models import Brand, ProductSku, ProductListing

class ProductListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductListing
        fields = ['status', 'marketplace']

class ProductSkuSerializer(serializers.ModelSerializer):
    # Rename 'name' to 'sku_name'
    sku_name = serializers.CharField(source='name')
    # Map 'marketplaces' to the related ProductListing objects
    marketplaces = ProductListingSerializer(many=True, source='listings', read_only=True)
    # Custom fields to match the desired structure
    epic_purchase_cost = serializers.SerializerMethodField()
    contracted_sell_price = serializers.SerializerMethodField()
    retail_price = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()
    dimensions = serializers.SerializerMethodField()
    # Add packaging_weight and packaging_dimensions (assuming these are stored in metadata or similar)
    packaging_weight = serializers.SerializerMethodField()
    packaging_dimensions = serializers.SerializerMethodField()
    # Add country (from ProductListing, we'll take the first one for simplicity)
    country = serializers.SerializerMethodField()

    class Meta:
        model = ProductSku
        fields = [
            'parentage', 'mfn_sku', 'sku_name', 'country', 'epic_purchase_cost',
            'contracted_sell_price', 'case_quantity', 'upc_gtin', 'retail_price',
            'asin', 'lead_time', 'weight', 'dimensions', 'packaging_weight',
            'packaging_dimensions', 'marketplaces'
        ]

    def get_epic_purchase_cost(self, obj):
        # Assuming epic_purchase_cost is stored as a JSON with 'value' and 'unit'
        return obj.epic_purchase_cost if obj.epic_purchase_cost else {"value": 0, "unit": "USD"}

    def get_contracted_sell_price(self, obj):
        return obj.contracted_sell_price if obj.contracted_sell_price else {"value": 0, "unit": "USD"}

    def get_retail_price(self, obj):
        if obj.retail_price:
            obj.retail_price = obj.retail_price['value'] + 20
            return obj.retail_price
        return {"value": 0, "unit": "USD"}

    def get_weight(self, obj):
        return obj.weight if obj.weight else {"unit": "lbs", "value": 0}

    def get_dimensions(self, obj):
        return obj.dimensions if obj.dimensions else {"unit": "in", "width": 0, "height": 0, "length": 0}

    def get_packaging_weight(self, obj):
        # Assuming packaging_weight might be in metadata or not exist
        return obj.metadata.get('packaging_weight', {"unit": "lbs", "value": 0}) if obj.metadata else {"unit": "lbs", "value": 0}

    def get_packaging_dimensions(self, obj):
        # Assuming packaging_dimensions might be in metadata or not exist
        return obj.metadata.get('packaging_dimensions', {"unit": "in", "width": 0, "height": 0, "length": 0}) if obj.metadata else {"unit": "in", "width": 0, "height": 0, "length": 0}

    def get_country(self, obj):
        # Take the country from the first ProductListing, if available
        first_listing = obj.listings.first()
        return first_listing.country if first_listing else "unknown"