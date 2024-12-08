import bpy
import blf

def draw_callback_px(self,context):
    blf.position(0,15,60,0)
    blf.size(0,20)
    blf.draw(0,"Custom stats: ")

class StatsDrawOperator(bpy.types.Operator):
    bl_idname = "view3d.draw_custom_stats"
    bl_label = "Simpli Statistics"
    bl_description = "Custom stats overlay on viewport"
    _handle = None

    def modal(self,context,event):
        if event.type == 'ESC':
            self.cancel(context)
            return {'CANCELLED'}
        
        return {'RUNNING_MODAL'}
    
    def invoke(self, context,event):
        if context.area.type == "VIEW_3D":
            args = (self, context)
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_PIXEL')

            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            return {'CANCELLED'}

    def draw(self, context):
        self.layout.label(text="Simpli Statistics")

def StatsMenuFunction(self,context):
    self.layout.operator(StatsDrawOperator.bl_idname,text = "Stats Draw Operator")

