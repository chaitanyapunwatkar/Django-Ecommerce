from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from ecommerce.serializers import OutletSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import IsSupervisor, IsSalesPerson
from rest_framework import generics
from ecommerce.models import Product, Outlet
import csv
from rest_framework.parsers import FileUploadParser


class EditProductDetails(APIView):
    '''
        This API updates the units of Product. Restricted to Admin, Supervisor and salesperson
    '''
    permission_classes = [IsAuthenticated, IsSalesPerson]
    
    def post(self, request):
        name = request.data.get('name')
        units = request.data.get('units')
        try:
            product = Product.objects.get(name=name)
        except Product.DoesNotExist:
            return Response({"error": "Product with the given name does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        product.units = units
        product.save()
        return Response({"success": "Product units updated successfully"}, status=status.HTTP_200_OK)
    
        
class AddProductDetails(APIView):
    '''
        This API writes Product details enterned by Supervisor/Admin. It is restricted to Admin and Supervisor users only
    '''
    permission_classes = [IsAuthenticated, IsSupervisor]
    def post(self, request):
        data = request.data
        name = data.get('name')
        type = data.get('type')
        manufacturer = data.get('manufacturer')
        unit = data.get('units')
        price = data.get('price')
        
        product_data = {
            "name": name, "type": type,
            "unit": unit, "price": price,
            "manufacturer": manufacturer
        }
        
        serializer = ProductSerializer(data=product_data)
        
        if serializer.is_valid():   
            serializer.save()
            return Response({'data':serializer.data, 'msg': "Product Details stored Successfully"}, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        

class BulkProductUpload(APIView):
    
    '''
        This API stores Product details in DB entered in CSV file using form-data method. 
    '''
    permission_classes = [IsAuthenticated]
    parser_classes = [FileUploadParser]
    
    def post(self, request):
        file_obj = request.FILES['file']
        decoded_file = file_obj.read().decode('utf-8').splitlines()
        
        # Skip header row
        csv_reader = csv.DictReader(decoded_file)
        next(csv_reader)

        for row in csv_reader:
            # Create a new Product instance for each row in the CSV file
            product_serializer = ProductSerializer(data=row)
            if product_serializer.is_valid():
                product_serializer.save()
            else:
                return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'Products uploaded successfully'}, status=status.HTTP_201_CREATED)


class AddStoreDetails(APIView):
    '''
        This API writes Store/outlet details enterned by Admin. It is restricted to Admin users only
    '''
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def post(self, request):
        data = request.data
        name = data.get('store_name')
        location = data.get('location')
        contact = data.get('contact')
        
        outlet_data = {
            "name": name,
            "location": location,
            "contact": contact
        }
        
        serializer = OutletSerializer(data=outlet_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'msg': "Outlet Details stored Successfully"}, status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetProduct(generics.ListAPIView):
    '''
        This API returns Products details based on requests send if product name given then Product details 
        of that name will be returned and if store name given then based on store name all Products of that store 
        name will be returned and if nothing is given in query params then all products based on stores will be returned.
    '''
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        store_name = data.get("store_name")
        product_name = data.get("product_name")
        
        if store_name:
            product_data = Product.objects.filter(store__name=store_name)
        elif product_name:
            product_data = Product.objects.filter(name=product_name)
        else:
            product_data = Product.objects.all()
            
        serializer = ProductSerializer(product_data)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class StoreListView(generics.ListAPIView):
    '''
        Returns all stores details present for the particular tenant
    '''
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    permission_classes = [IsAuthenticated]