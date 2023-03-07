import numpy as np
from vispy import app, gloo
from vispy.util.transforms import perspective, translate, rotate

# Vertex shader
vert = """
attribute vec3 a_position;
attribute vec4 a_color;

uniform mat4 u_model;
uniform mat4 u_view;
uniform mat4 u_projection;

varying vec4 v_color;

void main() {
    gl_Position = u_projection * u_view * u_model * vec4(a_position, 1.0);
    v_color = a_color;
}
"""

# Fragment shader
frag = """
varying vec4 v_color;

void main() {
    gl_FragColor = v_color;
}
"""

# Create vertex data
n = 100000
pos = np.random.normal(size=(n, 3), scale=0.2).astype(np.float32)
color = np.random.uniform(size=(n, 4), low=0, high=1).astype(np.float32)
data = np.zeros(n, [('a_position', np.float32, 3), ('a_color', np.float32, 4)])
data['a_position'] = pos
data['a_color'] = color

# Create canvas
canvas = app.Canvas(keys='interactive', size=(800, 600))

# Create program
program = gloo.Program(vert, frag)
program.bind(gloo.VertexBuffer(data))

# Set up view transform
view = translate((0, 0, -5))
model = np.eye(4, dtype=np.float32)
projection = perspective(45.0, canvas.size[0] / float(canvas.size[1]), 0.1, 100.0)

program['u_model'] = model
program['u_view'] = view
program['u_projection'] = projection

# Draw function
@canvas.connect
def on_draw(event):
    canvas.context.clear('white')
    program.draw('points')

# Show canvas
canvas.show()
app.run()
