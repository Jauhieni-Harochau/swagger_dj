from rest_framework import serializers

from api.models import Fab, Lithography, GPUArchitecture, Chipmaker, GPU, GraphicsBoardSKU, GraphicsBoard, Manufacturer, Image


class FabSerializer(serializers.ModelSerializer):
    processes = serializers.StringRelatedField(many=True)
    class Meta:
        model = Fab
        fields = '__all__'
        # fields = ['name', 'processes']


class LithographySerializer(serializers.ModelSerializer):
    # fab = FabSerializer()
    class Meta:
        model = Lithography
        fields = '__all__'
        depth = 1



class PostLithographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lithography
        fields = '__all__'
        depth = 0



class GPUArchitectureSerializer(serializers.ModelSerializer):
    gpus = serializers.StringRelatedField(many=True)
    class Meta:
        model = GPUArchitecture
        fields = '__all__'
        # fields = ['']


class ChipmakerSerializer(serializers.ModelSerializer):
    gpus = serializers.StringRelatedField(many=True)
    architectures = serializers.StringRelatedField(many=True)
    subsidiaries = serializers.StringRelatedField(many=True)
    class Meta:
        model = Chipmaker
        fields = '__all__'
        depth = 1


class GPUSerializer(serializers.ModelSerializer):

    class Meta:
        model = GPU
        fields = '__all__'



class GraphicsBoardSKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphicsBoardSKU
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class GraphicsBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphicsBoard
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    file_name = serializers.CharField(source='img.name')
    class Meta:
        model = Image
        fields = '__all__'

