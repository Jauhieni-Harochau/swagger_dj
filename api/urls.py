from rest_framework import routers
from api.views import FabView, LithographyView, GPUArchitectureView, GPUView, ChipmakerView, GraphicsBoardSKUView, \
    GraphicsBoardView, ManufacturerView, ImageView

router = routers.DefaultRouter()
router.register(r'fabs', FabView)
router.register(r'lithographies', LithographyView)
router.register(r'gpu-architectures', GPUArchitectureView)
router.register(r'gpus', GPUView)
router.register(r'chipmakers', ChipmakerView)
router.register(r'skus', GraphicsBoardSKUView)
router.register(r'graphic-boards', GraphicsBoardView)
router.register(r'manufacturers', ManufacturerView)
router.register(r'image', ImageView)
urlpatterns = []
urlpatterns += router.urls
