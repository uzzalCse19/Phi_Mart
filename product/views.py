# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category, Review
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
 
from product.models import Product, Category, Review, ProductImage
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer, ProductImageSerializer
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer,CategorySerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review
from .serializers import ReviewSerializer
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from product.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from product.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly, FullDjangoModelPermission
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from api.permissions import IsAdminOrReadOnly


# # Create your views here.


# # @api_view()
# # def view_specific_product(request, id):
# #     product = get_object_or_404(Product, pk=id)
# #     product_dict={'id':product.id, 'name':product.name, 'price':product.price}
# #     return Response(product_dict)

# # @api_view()
# # def view_specific_product(request, id):
# #     product = get_object_or_404(Product, pk=id)
# #     serializer = ProductSerializer(product)
# #     return Response(serializer.data)

# # @api_view()
# # def view_products(request):
# #     products = Product.objects.select_related('category').all()
# #     serializer = ProductSerializer(products, many=True)
# #     return Response(serializer.data)

# # @api_view()
# # def view_categories(request):
# #     categories = Category.objects.annotate(
# #         product_count=Count('products')).all()
# #     serializer = CategorySerializer(categories, many=True)
# #     return Response(serializer.data)



# # class ViewCategories(APIView):
# #     def get(self,request):
# #        categories = Category.objects.annotate(product_count=Count('products')).all()
# #        serializer = CategorySerializer(categories, many=True)
# #        return Response(serializer.data)
# #     def post(self,request):
# #         serializer=CategorySerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         return Response(serializer.data,status=status.HTTP_201_CREATED)

# class ListCategory(ListCreateAPIView):
#     queryset=Category.objects.annotate(product_count=Count('products')).all()
#     serializer_class=CategorySerializer


# # @api_view()
# # def view_specific_category(request, pk):
# #     category = get_object_or_404(Category, pk=pk)
# #     serializer = CategorySerializer(category)
# #     return Response(serializer.data)

# class ViewSpecificCategory(APIView):
#     def get(self,request,pk):
#         category=get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(),pk=pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         category=get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(),pk=pk)
#         serializer=CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self,request,pk):
#         category=get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(),pk=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

       



# # @api_view(['GET', 'PUT', 'DELETE'])
# # def view_specific_product(request, id):
# #     if request.method == 'GET':
# #         product = get_object_or_404(Product, pk=id)
# #         serializer = ProductSerializer(product)
# #         return Response(serializer.data)

# #     if request.method == 'PUT':
# #         product = get_object_or_404(Product, pk=id)
# #         serializer = ProductSerializer(product, data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data)

# #     if request.method == 'DELETE':
# #         product = get_object_or_404(Product, pk=id)
# #         copy_of_product = product
# #         product.delete()
# #         serializer = ProductSerializer(copy_of_product)
# #         return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

# class ViewSpecificProducts(APIView):
#     def get(self,request,id):
#         product=get_object_or_404(Product,pk=id)
#         serializer=ProductSerializer(product)
#         return Response(serializer.data)
#     def put(self,request,id):
#         product=get_object_or_404(Product,pk=id)
#         serializer=ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self,request,id):
#         product=get_object_or_404(Product,pk=id)
#         copy_of_product=product
#         product.delete()
#         seriaalizer=ProductSerializer(copy_of_product)
#         return Response(seriaalizer.data,status=status.HTTP_204_NO_CONTENT)

# # @api_view(['GET', 'POST'])
# # def view_products(request):
# #     if request.method == 'GET':
# #         products = Product.objects.select_related('category').all()
# #         serializer = ProductSerializer(
# #             products, many=True)
# #         return Response(serializer.data)

# #     if request.method == 'POST':
# #         serializer = ProductSerializer(
# #             data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# # class ViewProducts(APIView):
# #      def get(self, request):
# #          products = Product.objects.select_related('category').all()
# #          serializer = ProductSerializer(
# #              products, many=True)
# #          return Response(serializer.data)
 
# #      def post(self, request):
# #          serializer = ProductSerializer(
# #              data=request.data)
# #          serializer.is_valid(raise_exception=True)
# #          serializer.save()
# #          return Response(serializer.data, status=status.HTTP_201_CREATED)



# class ProductList(ListCreateAPIView):
#     queryset=Product.objects.select_related('category').all()
#     serializer_class=ProductSerializer


from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category, Review
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from product.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly, FullDjangoModelPermission
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from product.permissions import IsReviewAuthorOrReadonly


from drf_yasg.utils import swagger_auto_schema


class ProductViewSet(ModelViewSet):
    """
    API endpoint for managing products in the e-commerce store
     - Allows authenticated admin to create, update, and delete products
     - Allows users to browse and filter product
     - Support searching by name, description, and category
     - Support ordering by price and updated_at
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'updated_at']
    permission_classes = [IsAdminOrReadOnly]

    @swagger_auto_schema(
        operation_summary='Retrive a list of products'
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the products"""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a product by admin",
        operation_description="This allow an admin to create a product",
        request_body=ProductSerializer,
        responses={
            201: ProductSerializer,
            400: "Bad Request"
        }
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create product"""
        return super().create(request, *args, **kwargs)


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.annotate(
        product_count=Count('products')).all()
    serializer_class = CategorySerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadonly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs.get('product_pk'))

    def get_serializer_context(self):
        return {'product_id': self.kwargs.get('product_pk')}
    
class ProductImageViewSet(ModelViewSet):
     serializer_class = ProductImageSerializer
     permission_classes = [IsAdminOrReadOnly]
 
     def get_queryset(self):
         return ProductImage.objects.filter(product_id=self.kwargs.get('product_pk'))
 
     def perform_create(self, serializer):
         serializer.save(product_id=self.kwargs.get('product_pk'))