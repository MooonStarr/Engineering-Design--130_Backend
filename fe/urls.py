from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('new/<str:new_plant_name>/<int:new_start_pct>/<int:new_stop_pct>'     , views.new_plant     , name='new'),
    path('json/new/<str:new_plant_name>/<int:new_start_pct>/<int:new_stop_pct>', views.json_new_plant, name='json_new'),

    path('list_plants'      , views.list_plants      , name='list_plants'),
    path('json/list_plants' , views.json_list_plants , name='json_list_plants'),

    path('get/<str:get_plant_name>'     , views.get_plant     , name='get_plant'),
    path('json/get/<str:get_plant_name>', views.json_get_plant, name='json_get_plant'),

    path('change/<str:change_plant_name>/<int:change_start_pct>/<int:change_stop_pct>'      , views.change_plant       , name='change_plant'),
    path('json/change/<str:change_plant_name>/<int:change_start_pct>/<int:change_stop_pct>' , views.json_change_plant  , name='json_change_plant'),
    
    path('list_pots'      , views.list_pots      , name='list_pots'),
    path('json/list_pots' , views.json_list_pots , name='json_list_pots'),

    path('delete/<str:delete_plant_name>', views.delete_plant, name='delete_plant'),
    path('json/delete/<str:delete_plant_name>', views.json_delete_plant, name='json_delete_plant'),

    path('program/<int:program_pot_id>/<str:program_plant_name>', views.program_pot, name='program_pot'),
    path('json/program/<int:program_pot_id>/<str:program_plant_name>', views.json_program_pot, name='json_program_pot'),
    
    path('get_pot/<int:get_pot_id>', views.get_pot, name='get_pot'),
    path('json/get_pot/<int:get_pot_id>', views.json_get_pot, name='json_get_pot'),

    path('mmeasurement/<int:m_pot_id>/<int:m_moisture_value>/<int:m_temperature_value>'     , views.mmeasurement     , name='mmeasurement'),
    path('json/mmeasurement/<int:m_pot_id>/<int:m_moisture_value>/<int:m_temperature_value>', views.json_mmeasurement, name='json_mmeasurement'),
    
    path('mirrigation/<int:i_pot_id>/<int:i_irrigation_value>/<int:i_irrigation_duration>'     , views.mirrigation     , name='mirrigation'),
    path('json/mirrigation/<int:i_pot_id>/<int:i_irrigation_value>/<int:i_irrigation_duration>', views.json_mirrigation, name='json_mirrigation'),
    
    path('mget_programming/<int:pot_id>'      ,views.mget_programming      , name='mget_programming'),
    path('json/mget_programming/<int:pot_id>' ,views.json_mget_programming , name='json_mget_programming'),
]
