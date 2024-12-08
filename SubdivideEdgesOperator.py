import bpy
import bmesh

class SubdivideEdgesOperator(bpy.types.Operator):
    bl_idname = "experiment.subdivide_edges"
    bl_label = "Subdivide edges"
    def execute(self,context):
        obj = bpy.context.active_object
        bpy.ops.object.mode_set(mode='EDIT')
        mesh = bmesh.from_edit_mesh(obj.data)

        for edge in mesh.edges:
            edge.select = True

        bmesh.ops.subdivide_edges(mesh, edges=[e for e in mesh.edges if e.select],cuts=1)
        bmesh.update_edit_mesh(obj.data)

        return {"FINISHED"}