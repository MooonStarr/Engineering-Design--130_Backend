from datetime import datetime
from email.policy import HTTP
import json
from pydoc import plain
from django.shortcuts import render
from django.http import JsonResponse              

# Create your views here.

from django.http import HttpResponse
from django.utils.dateparse import parse_datetime

from fe.models import Irrigation, Measurement, Plant, Pot

def index(request):
    return HttpResponse("Hello, world. You're at the front-end index. My name is Dimitrios.")

def new_plant(request, new_plant_name, new_start_pct, new_stop_pct):
    if Plant.objects.filter(plant_name=new_plant_name).exists():
        return HttpResponse('ERROR: %d' %(1))
    elif new_start_pct>new_stop_pct:
        return HttpResponse('ERROR: %d' %(2))
    elif new_start_pct<0:
        return HttpResponse('ERROR: %d' %(2))
    elif new_stop_pct>100:
        return HttpResponse('ERROR: %d' %(2))
    else:
        p=Plant(plant_name=new_plant_name, start_pct=new_start_pct, stop_pct=new_stop_pct)
        p.save()
        return HttpResponse('ERROR: %d' %(0))

def json_new_plant(request, new_plant_name, new_start_pct, new_stop_pct):
    if Plant.objects.filter(plant_name=new_plant_name).exists():
        rsp = { 'ERROR'   : 1 }
    elif new_start_pct>new_stop_pct:
        rsp = { 'ERROR'   : 2 }
    elif new_start_pct<0:
        rsp = { 'ERROR'   : 2 }
    elif new_stop_pct>100:
        rsp = { 'ERROR'   : 2 }
    else:
        p=Plant(plant_name=new_plant_name, start_pct=new_start_pct, stop_pct=new_stop_pct)
        p.save()
        rsp = { 'ERROR'   : 0 }
    
    return JsonResponse(rsp)


def list_plants(request):
    plist=Plant.objects.filter().values_list('plant_name', flat=True)
    s=', '.join(plist)
    if len(plist)==0:
        return HttpResponse('ERROR: %d, NPLANTS: %d' %(1, 0))
    else:
        return HttpResponse('ERROR: %d, NPLANTS: %d, %s' %(0, len(plist), s))

def json_list_plants(request):
    plist=Plant.objects.filter().values_list('plant_name', flat=True)
    if len(plist)==0:
        rsp = { 
           'ERROR'   : 1, 
           'NPLANTS' : 0, 
           'plist'   : []
        } 
    else:
        rsp = { 
           'ERROR'   : 0, 
           'NPLANTS' : len(plist), 
           'plist'   : list(plist)
        } 
    return JsonResponse(rsp)


def get_plant(request, get_plant_name):
    if Plant.objects.filter(plant_name=get_plant_name).exists():
        p=Plant.objects.filter(plant_name=get_plant_name)[0]
        return HttpResponse('ERROR: %d, START: %d, STOP: %d' %(0, p.start_pct, p.stop_pct))
    else:
        return HttpResponse('ERROR: %d, START: %d, STOP: %d' %(1, 0, 0))

def json_get_plant(request, get_plant_name):
    if Plant.objects.filter(plant_name=get_plant_name).exists():
        p=Plant.objects.filter(plant_name=get_plant_name)[0]
        rsp = { 
           'ERROR'   : 0, 
           'START'   : p.start_pct, 
           'STOP'    : p.stop_pct,
        }
    else:
        rsp = { 
           'ERROR'   : 1, 
           'START'   : 0, 
           'STOP'    : 0,
        }
    return JsonResponse(rsp)

def change_plant(request, change_plant_name, change_start_pct, change_stop_pct):
    if change_start_pct<0:
        return HttpResponse('ERROR: %d' %(2))
    elif change_stop_pct>100:
        return HttpResponse('ERROR: %d' %(2))
    elif change_start_pct>change_stop_pct:
        return HttpResponse('ERROR: %d' %(2))
    elif Plant.objects.filter(plant_name=change_plant_name).exists():
        p=Plant.objects.filter(plant_name=change_plant_name)[0]
        p.start_pct=change_start_pct
        p.stop_pct=change_stop_pct
        p.save()
        return HttpResponse('ERROR: %d' %(0))
    else:
        return HttpResponse('ERROR: %d' %(1))

def json_change_plant(request, change_plant_name, change_start_pct, change_stop_pct):
    if change_start_pct<0:
        rsp = { 
           'ERROR'   : 2
        }
    elif change_stop_pct>100:
        rsp = { 
           'ERROR'   : 2
        }
    elif change_start_pct>change_stop_pct:
        rsp = { 
           'ERROR'   : 2
        }
    elif Plant.objects.filter(plant_name=change_plant_name).exists():
        p=Plant.objects.filter(plant_name=change_plant_name)[0]
        p.start_pct=change_start_pct
        p.stop_pct=change_stop_pct
        p.save()
        rsp = { 
           'ERROR'   : 0,
        }
    else:
        rsp = { 
           'ERROR'   : 1
        }
    return JsonResponse(rsp)

def list_pots(request):
    plist=Pot.objects.filter().values_list('pot_id', flat=True)
    s=', '.join(map(str,plist))
    if len(plist)==0:
        return HttpResponse('ERROR: %d, NPOTS: %d' %(1, 0))
    else:
        return HttpResponse('ERROR: %d, NPOTS: %d, %s' %(0, len(plist), s))

def json_list_pots(request):
    plist=Pot.objects.filter().values_list('pot_id', flat=True)
    if len(plist)==0:
        rsp = { 
           'ERROR'   : 1,
           'NPOTS'   : 0
        }
    else:
        rsp = { 
           'ERROR'   : 0,
           'NPOTS'   : len(plist),
           'PLIST'   : list(plist)
        }
    return JsonResponse(rsp)
  
def delete_plant(request, delete_plant_name):
    if Plant.objects.filter(plant_name=delete_plant_name).exists():
        p=Plant.objects.filter(plant_name=delete_plant_name)[0]
        p.delete()
        return HttpResponse('ERROR: %d' %(0))
    else:
        return HttpResponse('ERROR: %d' %(1))

def json_delete_plant(request, delete_plant_name):
    if Plant.objects.filter(plant_name=delete_plant_name).exists():
        p=Plant.objects.filter(plant_name=delete_plant_name)[0]
        p.delete()
        rsp = { 
           'ERROR'   : 0 
        }
    else:
        rsp = { 
           'ERROR'   : 1 
        }
    return JsonResponse(rsp)

def program_pot(request, program_pot_id, program_plant_name):
    ERROR=0
    if not Pot.objects.filter(pot_id=program_pot_id).exists():
        ERROR=ERROR+1
    if not Plant.objects.filter(plant_name=program_plant_name).exists():
        ERROR=ERROR+2
    if ERROR>0:
        return HttpResponse('ERROR: %d' %(ERROR))
    else:
        pot=Pot.objects.filter(pot_id=program_pot_id)[0]
        plant=Plant.objects.filter(plant_name=program_plant_name)[0]
        pot.plant_name=plant.plant_name
        pot.save()
        return HttpResponse('ERROR: %d' %(ERROR))

def json_program_pot(request, program_pot_id, program_plant_name):
    ERROR=0
    if not Pot.objects.filter(pot_id=program_pot_id).exists():
        ERROR=ERROR+1
    if not Plant.objects.filter(plant_name=program_plant_name).exists():
        ERROR=ERROR+2
    if ERROR>0:
        rsp = { 'ERROR'   : ERROR }
    else:
        pot=Pot.objects.filter(pot_id=program_pot_id)[0]
        plant=Plant.objects.filter(plant_name=program_plant_name)[0]
        pot.plant_name=plant.plant_name
        pot.save()
        rsp = { 'ERROR'   : ERROR }
    return JsonResponse(rsp)

def get_pot(request, get_pot_id):
    if Pot.objects.filter(pot_id=get_pot_id).exists():
        p=Pot.objects.filter(pot_id=get_pot_id)[0]
        return HttpResponse('ERROR: %d, PNAME: %s, ILAST: %s, IDUR: %d, IAMOUNT: %d, MLAST: %s, MVAL: %d, TVAL: %d'
        %(0, 
          p.plant_name, 
          p.irrigation_last,
          p.irrigation_duration, 
          p.irrigation_amount, 
          p.measurement_last,
          p.moisture_value, 
          p.temperature_value))
    else:
        return HttpResponse('ERROR: %d' %(1))
    
def json_get_pot(request, get_pot_id):
    if Pot.objects.filter(pot_id=get_pot_id).exists():
        p=Pot.objects.filter(pot_id=get_pot_id)[0]
        rsp = { 
            'ERROR'   : 0,
            'PNAME'   : p.plant_name,
            'ILAST'   : p.irrigation_last,
            'IDUR'    : p.irrigation_duration,
            'IAMOUT'  : p.irrigation_amount,
            'MLAST'   : p.measurement_last,
            'MVAL'    : p.moisture_value,
            'TVAL'    : p.temperature_value            
        }
    else:
        rsp = { 
            'ERROR'   : 1
        }
    return JsonResponse(rsp)

def mmeasurement(request, m_pot_id, m_moisture_value, m_temperature_value):
    if Pot.objects.filter(pot_id=m_pot_id).exists():
        new_datetime = datetime.now()
        m=Measurement(pot_id=m_pot_id, moisture_value=m_moisture_value, measurement_time=new_datetime, temperature_value=m_temperature_value)
        m.save()
        p=Pot.objects.filter(pot_id=m_pot_id)[0]
        p.measurement_last=new_datetime
        p.moisture_value=m_moisture_value
        p.temperature_value=m_temperature_value
        p.save()
        return HttpResponse('ERROR: %d' %(0))
    else:
        return HttpResponse('ERROR: %d' %(1))

def json_mmeasurement(request, m_pot_id, m_moisture_value, m_temperature_value):
    if Pot.objects.filter(pot_id=m_pot_id).exists():
        new_datetime = datetime.now()
        m=Measurement(pot_id=m_pot_id, moisture_value=m_moisture_value, measurement_time=new_datetime, temperature_value=m_temperature_value)
        m.save()
        p=Pot.objects.filter(pot_id=m_pot_id)[0]
        p.measurement_last=new_datetime
        p.moisture_value=m_moisture_value
        p.temperature_value=m_temperature_value
        p.save()
        rsp = { 
            'ERROR'   : 0
        }    
    else:
        rsp = { 
            'ERROR'   : 1
        } 
    return JsonResponse(rsp)

    
def mirrigation(request, i_pot_id, i_irrigation_value, i_irrigation_duration):
    if Pot.objects.filter(pot_id=i_pot_id).exists():
        new_datetime = datetime.now()
        i=Irrigation( pot_id              = i_pot_id, 
                      irrigation_value    = i_irrigation_value, 
                      irrigation_time     = new_datetime, 
                      irrigation_duration = i_irrigation_duration)
        i.save()
        p =Pot.objects.filter(pot_id=i_pot_id)[0]
        p.irrigation_last=new_datetime
        p.irrigation_amount=i_irrigation_value
        p.irrigation_duration=i.irrigation_duration
        p.save()
        return HttpResponse('ERROR: %d' %(0))
    else:
        return HttpResponse('ERROR: %d' %(1))

def json_mirrigation(request, i_pot_id, i_irrigation_value, i_irrigation_duration):
    if Pot.objects.filter(pot_id=i_pot_id).exists():
        new_datetime = datetime.now()
        i=Irrigation( pot_id              = i_pot_id, 
                      irrigation_value    = i_irrigation_value, 
                      irrigation_time     = new_datetime, 
                      irrigation_duration = i_irrigation_duration)
        i.save()
        p =Pot.objects.filter(pot_id=i_pot_id)[0]
        p.irrigation_last=new_datetime
        p.irrigation_amount=i_irrigation_value
        p.irrigation_duration=i.irrigation_duration
        p.save()
        rsp = { 
            'ERROR'   : 0
        }
    else:
        rsp = { 
            'ERROR'   : 1
        }
    return JsonResponse(rsp)

def mget_programming(request, pot_id):
    if Pot.objects.filter(pot_id=pot_id).exists():
        plant_name=Pot.objects.filter(pot_id=pot_id)[0].plant_name
        plant=Plant.objects.filter(plant_name=plant_name)[0]
        return HttpResponse('ERROR: %d, START: %d, STOP: %d'
        %(0, plant.start_pct, plant.stop_pct))
    else:
        return HttpResponse('ERROR: %d' %(1))

def json_mget_programming(request, pot_id):
    if Pot.objects.filter(pot_id=pot_id).exists():
        plant_name=Pot.objects.filter(pot_id=pot_id)[0].plant_name
        plant=Plant.objects.filter(plant_name=plant_name)[0]
        rsp = { 
            'ERROR'   : 0,
            'START'   : plant.start_pct,
            'STOP'    : plant.stop_pct
        }
    else:
        rsp = { 
            'ERROR'   : 1
        }
    return JsonResponse(rsp)



### Alternative functions
#def mirrigation(request, i_pot_id, i_irrigation_time, i_irrigation_value, i_irrigation_duration):
#    if Pot.objects.filter(pot_id=i_pot_id).exists():
#        new_datetime = parse_datetime(i_irrigation_time)
#        i=Irrigation( pot_id              = i_pot_id, 
#                      irrigation_value    = i_irrigation_value, 
#                      irrigation_time     = new_datetime, 
#                      irrigation_duration = i_irrigation_duration)
#        i.save()
#        p =Pot.objects.filter(pot_id=i_pot_id)[0]
#        p.irrigation_last=new_datetime
#        p.irrigation_amount=i_irrigation_value
#        p.irrigation_duration=i.irrigation_duration
#        p.save()
#        return HttpResponse('ERROR: %d' %(0))
#    else:
#        return HttpResponse('ERROR: %d' %(1))
#
#
#def mmeasurement(request, m_pot_id, m_measurement_time, m_moisture_value, m_temperature_value):
#    if Pot.objects.filter(pot_id=m_pot_id).exists():
#        new_datetime = parse_datetime(m_measurement_time)
#        m=Measurement(pot_id=m_pot_id, moisture_value=m_moisture_value, measurement_time=new_datetime, temperature_value=m_temperature_value)
#        m.save()
#        p=Pot.objects.filter(pot_id=m_pot_id)[0]
#        p.measurement_last=new_datetime
#        p.moisture_value=m_moisture_value
#        p.temperature_value=m_temperature_value
#        p.save()
#        return HttpResponse('ERROR: %d' %(0))
#    else:
#        return HttpResponse('ERROR: %d' %(1))
