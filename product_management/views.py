from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from product_management.models import ProductSku
from product_management.serializers import ProductSkuSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 100


@api_view(['GET'])
def list_product_skus(request):
    try:
        # Fetch all ProductSku instances
        skus = ProductSku.objects.all().select_related('brand').prefetch_related('listings')

        # Apply pagination
        paginator = CustomPagination()
        page = paginator.paginate_queryset(skus, request)

        # Serialize the data
        serializer = ProductSkuSerializer(page, many=True)

        # Construct the response
        response_data = {
            "sku": serializer.data,
            "page": int(request.GET.get('page', 1)),
            "limit": paginator.get_page_size(request),
            "total_page_count": paginator.page.paginator.num_pages,
            "total_record_count": paginator.page.paginator.count
        }

        return Response(response_data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "sku": [],
            "page": 1,
            "limit": 10,
            "total_page_count": 0,
            "total_record_count": 0,
            "error": f"An error occurred: {str(e)}"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)