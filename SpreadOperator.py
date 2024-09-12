
import bpy
import math
from . import AxisType
from . import PaddingType

ONEAXIS = '1AXIS'
TWOAXIS = '2AXIS'
THREEAXIX = '3AXIS'

class SpreadOperator(bpy.types.Operator):
    bl_idname = "object.spread_operator"
    bl_label = "Spread"

    def execute(self, context):
        padding_type = context.scene.padding_options
        padding_value = context.scene.padding_value

        use_x = context.scene.use_x_axis
        use_y = context.scene.use_y_axis
        use_z = context.scene.use_z_axis

        number_of_axes = use_x + use_y + use_z

        if bpy.context.mode != "OBJECT":
            self.report({"WARNING"}, "Not in object mode.")
            return {"CANCELLED"}
        
        if len(bpy.context.selected_objects) <= 1:
            self.report({"WARNING"}, "Not enough objects selected. Select 2 or more objects.")
            return {"CANCELLED"}
        
        if number_of_axes == 0:
            self.report({"WARNING"}, "Select one or more axes")
            return {"CANCELLED"}

        # single axis
        if number_of_axes == 1:
            axis = self.getAxis(use_x,use_y,use_z)
            self.oneAxisSpread(bpy.context.selected_objects, padding_type, padding_value,axis)

        # 2 axis
        if number_of_axes == 2:
            self.report({"WARNING"}, "Not implemented.")
            return {"CANCELLED"}
            # self.twoAxisSpread(bpy.context.selected_objects, padding_type, padding_value)

        if number_of_axes == 3:
            self.report({"WARNING"}, "Not implemented.")
            return {"CANCELLED"}

        print(f"Spread on: {number_of_axes}, padding type: {padding_type}")
        return {'FINISHED'}
    
    def oneAxisSpread(self, objects, padding_type, padding_value, axis):
        self.resetLocation(objects)

        # If using largest, find largest object x dim
        # distribute with largest x dim + padding value
        if padding_type == PaddingType.LARGEST:
            largest_of_axis = self.largestOfAxis(objects,AxisType.AxisType.XAxis)
            self.distributeAlongAxisWithPaddingValue(objects,(largest_of_axis+padding_value),axis)
            return

        # padding type individual
        if padding_type == PaddingType.INDIVIDUAL:
            for index in range(1,len(objects)):
                obj = objects[index]
                previous_obj = objects[index-1]
                # previous location + half bounds + half bounds + padding
                obj.location[axis] = previous_obj.location[axis] + ((previous_obj.dimensions[axis])/2) + ((obj.dimensions[axis])/2) + padding_value
            return

        # If using value only
        if padding_type == PaddingType.VALUE:
            self.distributeAlongAxisWithPaddingValue(objects,padding_value,axis)
            return
        
    def twoAxisSpread(self, objects, padding_type, padding_value):
        #self.resetLocation(objects)
        axis_length = math.sqrt(len(objects))
        if not axis_length.is_integer():
            axis_length = math.ceil(axis_length)

        # Take n from objects list and spread it

        print("Two axis spread")

    def resetLocation(self, objects):
        for obj in objects:
            obj.location = (0,0,0)

    def distributeAlongAxisWithPaddingValue(self,objects,value,axis):
        for index, obj in enumerate(objects):
            obj.location[axis] = (index*value)

    def largestOfAxis(self,objects,axis):
        largest = 0
        for obj in objects:
            objDimension = obj.dimensions[axis]
            if largest <= objDimension:
                largest = objDimension
        return largest
    
    def getScenePropertyValues():
        print("Get scene property values not implemented.")
        pass

    def getAxis(self,use_x,use_y,use_z):
        if use_x:
            return AxisType.AxisType.XAxis
        if use_y:
            return AxisType.AxisType.YAxis
        if use_z:
            return AxisType.AxisType.ZAxis

