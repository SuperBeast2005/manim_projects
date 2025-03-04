from manim import *
import math

class Create3DAxes(ThreeDScene):
    def construct(self):
        #Plane
        axes: ThreeDAxes = ThreeDAxes(
            x_range=[-5,5,1],
            y_range=[-5,5,1],
            z_range=[-5,5,1],
            x_length=10,
            y_length=10,
            z_length=10,
        )
        labels =  axes.get_axis_labels(
            Text("X").scale(0.42),
            Text("Y").scale(0.42),
            Text("i").scale(0.42),
        )
        self.set_camera_orientation()
        
        #Graph
        exp = FunctionGraph(
            lambda x: math.exp(x),
            x_range = [-5,5],
            color = GREEN
        )
        #Animation
        self.add(axes, labels)
        self.add(exp)
        self.wait(10)
        self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, gamma=0 * DEGREES)
        self.wait(10)

        
if __name__ == "__main__":
    pass