
import bpy
import math
from . import AxisType
from . import PaddingType
from . import SpreadOperator
from . import SimpliUtilitiPanel

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

def register():
    bpy.utils.register_class(SpreadOperator.SpreadOperator)
    bpy.utils.register_class(SimpliUtilitiPanel.SimpliUtilitiPanel)


def unregister():
    bpy.utils.unregister_class(SpreadOperator.SpreadOperator)
    bpy.utils.unregister_class(SimpliUtilitiPanel.SimpliUtilitiPanel)