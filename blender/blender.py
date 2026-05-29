import bpy
import math

# Очистка сцены
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# -------------------------
# Параметры сцены
# -------------------------
baseline = 0.1  # расстояние между камерами (метры, 10 см)
camera_height = 0.8  # высота камеры (80 см)
box_height = 0.2  # высота коробки (20 см)

# -------------------------
# Плоскость (пол)
# -------------------------
bpy.ops.mesh.primitive_plane_add(size=2, location=(0, 0, 0))

# -------------------------
# Коробка
# -------------------------
bpy.ops.mesh.primitive_cube_add(size=0.3, location=(0, 0, box_height / 2))

# -------------------------
# Камера левая
# -------------------------
bpy.ops.object.camera_add(location=(-baseline/2, -1, camera_height))
cam_left = bpy.context.object
cam_left.name = "Camera_Left"

# -------------------------
# Камера правая
# -------------------------
bpy.ops.object.camera_add(location=(baseline/2, -1, camera_height))
cam_right = bpy.context.object
cam_right.name = "Camera_Right"

# -------------------------
# Точка, на которую смотрят камеры
# -------------------------
target = bpy.data.objects.new("Target", None)
target.location = (0, 0, box_height/2)
bpy.context.collection.objects.link(target)

# -------------------------
# Функция "смотреть на"
# -------------------------
def look_at(obj, target):
    direction = target.location - obj.location
    rot_quat = direction.to_track_quat('-Z', 'Y')
    obj.rotation_euler = rot_quat.to_euler()

look_at(cam_left, target)
look_at(cam_right, target)

# -------------------------
# Свет
# -------------------------
bpy.ops.object.light_add(type='SUN', location=(2, -2, 2))

# -------------------------
# Настройки рендера
# -------------------------
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.render.resolution_x = 640
scene.render.resolution_y = 480

# -------------------------
# Рендер левой камеры
# -------------------------
scene.camera = cam_left
scene.render.filepath = "//left.png"
bpy.ops.render.render(write_still=True)

# -------------------------
# Рендер правой камеры
# -------------------------
scene.camera = cam_right
scene.render.filepath = "//right.png"
bpy.ops.render.render(write_still=True)

print("Готово! Сохранены left.png и right.png")