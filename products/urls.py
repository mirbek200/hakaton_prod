from django.urls import path
from .views import (ProductListApiView,
                    ProductCreateApiView,
                    ProductDetailApiView,
                    ProductUpdateApiView,
                    CategoryListApiView,
                    CategoryCreateApiView,
                    ProductDestroyApiView,
                    CategoryDestroyApiView,
                    CategoryApiView)

urlpatterns = [
    path('prod_list/', ProductListApiView.as_view(), name='prod-list'),
    path('prod_create/', ProductCreateApiView.as_view(), name='prod-create'),
    path('detail/<int:id>/', ProductDetailApiView.as_view(), name='detail'),
    path('update/<int:id>/', ProductUpdateApiView.as_view(), name='update'),
    path('delete/<int:id>/', ProductDestroyApiView.as_view(), name='delete'),
    path('cat_list/', CategoryListApiView.as_view(), name='cat-list'),
    path('cat_create/', CategoryCreateApiView.as_view(), name='cat_create'),
    path('cat_destroy/', CategoryCreateApiView.as_view(), name='cat_destroy'),
    path('filter/<slug:name>/', CategoryApiView.as_view(), name='filter_category'),
]