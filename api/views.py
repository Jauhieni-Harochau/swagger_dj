from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from api.models import (Fab,
                        Lithography,
                        GPUArchitecture,
                        GPU,
                        Chipmaker,
                        GraphicsBoardSKU,
                        GraphicsBoard,
                        Manufacturer,
                        Image
                        )
from api.serializers import (FabSerializer,
                             LithographySerializer,
                             GPUArchitectureSerializer,
                             GPUSerializer,
                             ChipmakerSerializer,
                             GraphicsBoardSKUSerializer,
                             GraphicsBoardSerializer,
                             ManufacturerSerializer,

                             PostLithographySerializer,
                             ImageSerializer
                             )



class FabView(viewsets.ModelViewSet):
    serializer_class = FabSerializer
    queryset = Fab.objects.all()


class LithographyView(viewsets.ModelViewSet):
    serializer_classes = {
        'list': LithographySerializer,
        'create': PostLithographySerializer,
        'retrieve': LithographySerializer,
        'update': PostLithographySerializer,
        # 'partial_update': PostLithographySerializer

    }
    default_serializer_class = LithographySerializer
    queryset = Lithography.objects.all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)




class GPUArchitectureView(viewsets.ModelViewSet):
    serializer_class = GPUArchitectureSerializer
    queryset = GPUArchitecture.objects.all()


class GPUView(viewsets.ModelViewSet):
    serializer_class = GPUSerializer
    queryset = GPU.objects.all()


class ChipmakerView(viewsets.ModelViewSet):
    serializer_class = ChipmakerSerializer
    queryset = Chipmaker.objects.all()


class GraphicsBoardSKUView(viewsets.ModelViewSet):
    serializer_class = GraphicsBoardSKUSerializer
    queryset = GraphicsBoardSKU.objects.all()


class GraphicsBoardView(viewsets.ModelViewSet):
    serializer_class = GraphicsBoardSerializer
    queryset = GraphicsBoard.objects.all()


class ManufacturerView(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ImageView(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()