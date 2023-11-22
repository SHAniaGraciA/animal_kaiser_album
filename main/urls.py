from django.urls import path
from main.views import *
app_name = 'main'
urlpatterns = [
    path('', login_user, name='login'),
    path('main', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_amount_button/<int:item_id>/', add_amount_button, name='add_amount_button'),
    path('reduce_amount_button/<int:item_id>/', reduce_amount_button, name='reduce_amount_button'),
    path('remove_item/<int:item_id>/', remove_item, name='remove_item'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('remove_item_button/<int:item_id>/', remove_item_button, name='remove_item_button'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('create-flutter/', create_item_flutter, name='create_product_flutter'),
]