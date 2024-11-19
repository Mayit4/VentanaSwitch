import flet as ft


def main(ventana:ft.Page):
    
    def cambiartitulo(e):  
        if sw.value==True:
            ventana.title="Prendido"
        else:
            ventana.title="Apagado"
        ventana.update()  
        
    def cambiarventana(e):
        if sw1.value==True:
            ventana.bgcolor="green"
        else:
            ventana.bgcolor="red"
        ventana.update()
        
       
    def restaurar(e):
        ventana.bgcolor="White"
        ventana.title="SWITCH"
        sw.value=False
        sw1.value=False
        sl.value=0
        an.value=250
        al.value=250
        ventana.update()
    
    def mostrarvalor(e):
        print(sl.value)  
    
    def ancho(e):
        ventana.window.width=an.value
        ventana.update()
    
    def alto(e):
        ventana.window.height=al.value
        ventana.update()
        
    
    sw=ft.Switch(value=False, label="Titulo de Apagado y Prendido", track_color=ft.colors.AMBER,active_color="green",inactive_thumb_color="red", on_change=cambiartitulo )
    ventana.add(sw)
    
    sw1=ft.Switch(value=False, label="Cambiar Color de la Ventana", track_color=ft.colors.AMBER,active_color="green",inactive_thumb_color="red", on_change=cambiarventana )
    ventana.add(sw1)
    
    sl=ft.Slider(min=0,max=100,value=0,width=400,on_change=mostrarvalor,divisions=100)
    ventana.add(sl)
    
    an=ft.Slider(min=250,max=1280,value=250,width=400,on_change=ancho,divisions=1000)
    ventana.add(an)
    
    al=ft.Slider(min=250,max=720,value=250,width=400,on_change=alto,divisions=1000)
    ventana.add(al)
    
    r=ft.ElevatedButton("Restaurar", width=400, bgcolor="black",color="white", on_click=restaurar)
    ventana.add(r)
    
    
    ventana.title="SWITCH"
    ventana.window.width=400
    ventana.window.height=400
    ventana.bgcolor="White"
    ventana.horizontal_alignment=ft.CrossAxisAlignment.CENTER # horizontal
    ventana.vertical_alignment=ft.MainAxisAlignment.CENTER # vertical
    ventana.update()    
 
      
ft.app(target=main)