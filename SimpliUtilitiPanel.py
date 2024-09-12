import bpy

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