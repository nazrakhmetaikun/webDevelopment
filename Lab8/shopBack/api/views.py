from django.http.response import JsonResponse

# part for simulation without DB --------------------------------------------------
# products = [
#     {
#         'id': i,
#         'name': f'Product {i}',
#         'description': 'Some description',
#         'count': 2 * i,
#         'is_active': True
#     }
#     for i in range(1, 10)
# ]
#
# categories = [
#     {
#         'id': i,
#         'name': f'Category {i}'
#     }
#     for i in range(1, 6)
# ]
#
#
# def product_list(request):
#     return JsonResponse(products, safe=False)
#
#
# def product_detail(request, product_id):
#     for product in products:
#         if product['id'] == product_id:
#             return JsonResponse(product)
#     return JsonResponse({'message': 'Product not found'}, status=400)
#
#
# def category_list(request):
#     return JsonResponse(categories, safe=False)
#
#
# def category_detail(request, category_id):
#     for category in categories:
#         if category['id'] == category_id:
#             return JsonResponse(category)
#     return JsonResponse({'message': 'Category not found'}, status=400)


# Main working part ----------------------------------------------------------
from api.models import Product, Category


def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message:': str(e)}, status=400)
    return JsonResponse(product.to_json())


def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message:': str(e)}, status=400)
    return JsonResponse(category.to_json())
