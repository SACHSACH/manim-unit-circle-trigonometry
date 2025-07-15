from manim import *
from numpy import arctan2, degrees
class BasicTrigonometry(Scene):
    def construct(self):
        theta = ValueTracker(PI / 4)
        theta_label = MathTex(r"\theta=").to_edge(UR, buff=2)
        theta_value = always_redraw(
            lambda: DecimalNumber(
                degrees(arctan2(np.sin(theta.get_value()), np.cos(theta.get_value()))),
                num_decimal_places=2,
                include_sign=False
                ).next_to(theta_label, RIGHT)
) 
        
        plane = NumberPlane(background_line_style={"stroke_width": 0}).add_coordinates()

        circ = Circle(color=WHITE)

        line1 = Line(start=(-1, 1.5, 0), end=(1, 1.5, 0))
        line2 = Line(start=(-1, 1.5, 0), end=(1, 1.5, 0))
        line3 = Line(start=(-1, 1.5, 0), end=(1, 1.5, 0))

        opposite = Tex("Opposite").next_to(line2, UP)
        opposite_move = Tex("Opposite", color=YELLOW).to_edge(UL, buff=1)

        divide1 = Line(start=ORIGIN, end=(2, 0, 0)).next_to(opposite_move, DOWN)
        equal1 = Tex("=", color=RED).next_to(divide1, RIGHT)
        sin_value = always_redraw(lambda: DecimalNumber(np.sin(theta.get_value())).next_to(equal1, RIGHT))

        hypotenuse = Tex("Hypotenuse").next_to(line1, UP)
        hypotenuse_move = Tex("Hypotenuse", color=GREEN).next_to(divide1, DOWN)
        hypotenuse_move2 = Tex("Hypotenuse", color=GREEN).to_edge(DL, buff=1)

        divide2 = Line(start=ORIGIN, end=(2, 0, 0)).next_to(hypotenuse_move2, UP)
        equal2 = Tex("=", color=RED).next_to(divide2, RIGHT)
        cos_value = always_redraw(lambda: DecimalNumber(np.cos(theta.get_value())).next_to(equal2, RIGHT))

        adjacent = Tex("Adjacent").next_to(line3, UP)
        adjacent_move = Tex("Adjacent", color=ORANGE).next_to(divide2, UP)
        
        adjacent_move2 = Tex("Adjacent", color=ORANGE).to_edge(DR, buff=1).shift(LEFT * 2)

        divide3 = Line(start=ORIGIN, end=(2, 0, 0)).next_to(adjacent_move2, UP)
        equal3 = Tex("=", color=RED).next_to(divide3, RIGHT)
        tan_value = always_redraw(lambda: DecimalNumber(np.tan(theta.get_value())).next_to(equal3, RIGHT))

        opposite_move2 = Tex("Opposite", color=YELLOW).next_to(divide3, UP)
        
        sin_label = MathTex(r"sin(\theta)", color=ORANGE).next_to(equal1, LEFT)
        cos_label = MathTex(r"cos(\theta)", color=YELLOW).next_to(equal2, LEFT)
        tan_label = MathTex(r"tan(\theta)", color=GREEN).next_to(equal3, LEFT)

        radius = always_redraw(lambda: Line(start=ORIGIN, end=(np.cos(theta.get_value()), np.sin(theta.get_value()), 0), color=GREEN))
        line_opposite = always_redraw(lambda: Line(start=(np.cos(theta.get_value()), np.sin(theta.get_value()), 0), end=(np.cos(theta.get_value()), 0, 0), color=YELLOW))
        line_adjacent = always_redraw(lambda: Line(start=ORIGIN, end=(np.cos(theta.get_value()), 0, 0), color=ORANGE))

        self.play(DrawBorderThenFill(plane))
        self.play(Create(circ), run_time=0.5, rate_func=linear)
        self.wait()
        self.play(Create(VGroup(line1, hypotenuse), run_time=0.25, rate_func=linear))
        self.wait()
        self.play(ReplacementTransform(line1, radius), ReplacementTransform(hypotenuse, hypotenuse_move))
        self.wait()
        self.play(Create(VGroup(theta_label, theta_value)))
        self.wait()
        self.play(Create(VGroup(line2, opposite), run_time=0.25, rate_func=linear))
        self.wait()
        self.play(ReplacementTransform(line2, line_opposite), ReplacementTransform(opposite, opposite_move))
        self.play(Create(divide1, run_time=0.25, rate_func=linear))
        self.play(Create(VGroup(equal1, sin_value)), run_time=0.25, rate_func=linear)
        self.wait()
        self.play(theta.animate.increment_value(TAU), rate_func=smooth, run_time=3)
        self.wait()
        self.play(Create(VGroup(line3, adjacent), run_time=0.25, rate_func=linear))
        self.wait()
        self.play(ReplacementTransform(line3, line_adjacent), ReplacementTransform(adjacent, adjacent_move), Create(hypotenuse_move2))
        self.play(Create(divide2, run_time=0.25, rate_func=linear))
        self.play(Create(VGroup(equal2, cos_value)), run_time=0.25, rate_func=linear)
        self.wait()
        self.play(theta.animate.increment_value(TAU), rate_func=smooth, run_time=3)
        self.wait()
        self.play(Create(VGroup(opposite_move2, adjacent_move2), run_time=0.25, rate_func=linear))
        self.play(Create(divide3, run_time=0.25, rate_func=linear))
        self.play(Create(VGroup(equal3, tan_value)), run_time=0.25, rate_func=linear)
        self.wait()
        self.play(theta.animate.increment_value(TAU), rate_func=smooth, run_time=3)
        self.wait()
        self.play(ReplacementTransform(Group(opposite_move, hypotenuse_move, divide1), sin_label), ReplacementTransform(Group(adjacent_move, hypotenuse_move2, divide2), cos_label), ReplacementTransform(Group(opposite_move2, adjacent_move2, divide3), tan_label))
        self.wait()
        self.play(theta.animate.increment_value(TAU), rate_func=smooth, run_time=3)
        self.wait()
