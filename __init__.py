
import bpy
import math
from . import AxisType
from . import PaddingType
from . import SpreadOperator

bpy.types.Scene.padding_options = bpy.props.EnumProperty(
    name = "Padding type",
    description = "Choose padding type",
    items=[
        (PaddingType.LARGEST, "Largest", "Spread objects based off largest objects' size"),
        (PaddingType.INDIVIDUAL, "Individual", "Spread objects per object"),
        (PaddingType.VALUE, "Value", "Spread objects based off padding value"),
    ]
)

bpy.types.Scene.padding_value = bpy.props.FloatProperty(name = "Padding value")

bpy.types.Scene.use_x_axis = bpy.props.BoolProperty(name = "X")
bpy.types.Scene.use_y_axis = bpy.props.BoolProperty(name = "Y")
bpy.types.Scene.use_z_axis = bpy.props.BoolProperty(name = "Z")

class SimpliUtilitiPanel(bpy.types.Panel):
    bl_idname = "OBEJCT_PT_simpli_utiliti"
    bl_label = "Simpli Utiliti" # header
    bl_space_type = 'VIEW_3D' # Of the 3d view
    bl_region_type = 'UI' # N menu
    bl_category = "Simpli Utiliti" # Name on N menu

    def  draw(self, context):
        layout = self.layout
        
        layout.operator("object.spread_operator", text="Spread")
        layout.prop(context.scene, "padding_options")
        layout.prop(context.scene, "padding_value")

        row = layout.row()

        row.prop(context.scene, "use_x_axis", toggle=True)
        row.prop(context.scene, "use_y_axis", toggle=True)
        row.prop(context.scene, "use_z_axis", toggle=True)

def register():
    bpy.utils.register_class(SpreadOperator.SpreadOperator)
    bpy.utils.register_class(SimpliUtilitiPanel)


def unregister():
    bpy.utils.unregister_class(SpreadOperator.SpreadOperator)
    bpy.utils.unregister_class(SimpliUtilitiPanel)