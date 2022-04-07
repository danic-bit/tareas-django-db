from desafioadl.models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.exclude(eliminada= True)
    todas_las_tareas = []
    for tarea in tareas:
        tarea_items = {
            'tarea': tarea,
            'sub_tareas': tarea.subtarea_set.exclude(eliminada=True)
        }
        todas_las_tareas.append(tarea_items)
    return todas_las_tareas

def crear_nueva_tarea(descripcion_ingr=""):
    tarea = Tarea(descripcion=descripcion_ingr)
    tarea.save()
    print(f"se ha creado la nueva tarea {tarea.descripcion}\n")
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(ingresa_id_tarea, descripcion_subt):
    tarea = Tarea.objects.get(pk=ingresa_id_tarea)
    sub_tarea = SubTarea(descripcion=descripcion_subt, eliminada=False, tarea_id=tarea)
    sub_tarea.save()
    print(f"se ha creado la subtarea {sub_tarea.descripcion}\n")
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    tarea.eliminada = True
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(sub_tarea_id):
    sub_tarea = SubTarea.objects.get(pk=sub_tarea_id)
    sub_tarea.eliminada = True
    sub_tarea.save()
    return recupera_tareas_y_sub_tareas()


def imprimir_en_pantalla(tareas=[]):
    
    for elemento in tareas:
        print("[{0}] - {1}".format(elemento['tarea'].id, elemento['tarea'].descripcion))
        for s in elemento['sub_tareas']:
            print("...[{0}] - {1}".format(s.id, s.descripcion))
    
    #la shell se escribe >>> imprimir_en_pantalla(recupera_tareas_y_sub_tareas()) 
 