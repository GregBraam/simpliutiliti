
import bpy
import math
from . import PaddingType
from . import AxisType
from .SpreadOperator import SpreadOperator
from .SimpliUtilitiPanel import SimpliUtilitiPanel
from .SimpliStatisticsPanel import StatsDrawOperator
from .SubdivideEdgesOperator import SubdivideEdgesOperator

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

classes = (
    SpreadOperator,
    SimpliUtilitiPanel,
    StatsDrawOperator,
    SubdivideEdgesOperator
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    #bpy.types.VIEW3D_MT_view.append(SimpliStatisticsPanel.StatsMenuFunction)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    #bpy.types.VIEW3D_MT_view.remove(SimpliStatisticsPanel.StatsMenuFunction)