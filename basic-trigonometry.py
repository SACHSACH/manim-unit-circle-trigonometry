from big_ol_pile_of_manim_imports import *
from manim import *

class BasicTrigonometry(Scene):
    def construct(self):
        theta = ValueTracker(PI/4)
        theta_label = MathTex(r"\theta=").to_edge(UR, buff=2)
        theta_value = always_redraw(lambda: DecimalNumber().set_value(theta.get_value()).next_to(theta_label, RIGHT))
        
        plane = NumberPlane(background_line_style={"stroke_width": 0}).add_coordinates()

        circ = Circle(color=WHITE)

        line1 = Line((-1, 1.5, 0), (1, 1.5, 0))
        line2 = Line((-1, 1.5, 0), (1, 1.5, 0))
        line3 = Line((-1, 1.5, 0), (1, 1.5, 0))

        de = Tex("Depan").next_to(line2, UP)
        de_move = Tex("Depan", color=YELLOW).to_edge(UL, buff=1)

        divide1 = Line(ORIGIN, (2, 0, 0)).next_to(de_move, DOWN)
        equal1 = Tex("=", color=RED).next_to(divide1, RIGHT)
        sin_value = always_redraw(lambda: DecimalNumber().set_value(np.sin(theta.get_value())).next_to(equal1, RIGHT))

        mi = Tex("Miring").next_to(line1, UP)
        mi_move = Tex("Miring", color=GREEN).next_to(divide1, DOWN)
        mi_move2 = Tex("Miring", color=GREEN).to_edge(DL, buff=1)

        divide2 = Line(ORIGIN, (2, 0, 0)).next_to(mi_move2, UP)
        equal2 = Tex("=", color=RED).next_to(divide2, RIGHT)
        cos_value = always_redraw(lambda: DecimalNumber().set_value(np.cos(theta.get_value())).next_to(equal2, RIGHT))

        sa = Tex("Samping").next_to(line3, UP)
        sa_move = Tex("Samping", color=ORANGE).next_to(divide2, UP)
        
        sa_move2 = Tex("Samping", color=ORANGE).to_edge(DR, buff=1).shift(LEFT*2)

        divide3 = Line(ORIGIN, (2, 0, 0)).next_to(sa_move2, UP)
        equal3 = Tex("=", color=RED).next_to(divide3, RIGHT)
        tan_value = always_redraw(lambda: DecimalNumber().set_value(np.tan(theta.get_value())).next_to(equal3, RIGHT))

        de_move2 = Tex("Depan", color=YELLOW).next_to(divide3, UP)
        
        sin_label = MathTex(r"sin(\theta)", color=ORANGE).next_to(equal1, LEFT)
        cos_label = MathTex(r"cos(\theta)", color=YELLOW).next_to(equal2, LEFT)
        tan_label = MathTex(r"tan(\theta)", color=GREEN).next_to(equal3, LEFT)

        radius = always_redraw(lambda: Line(ORIGIN, (np.cos(theta.get_value()), np.sin(theta.get_value()), 0), color=GREEN))
        line_de = always_redraw(lambda: Line((np.cos(theta.get_value()), np.sin(theta.get_value()), 0), (np.cos(theta.get_value()), 0, 0), color=YELLOW))
        line_sa = always_redraw(lambda: Line((0, 0, 0), (np.cos(theta.get_value()), 0, 0), color=ORANGE))

        self.play(DrawBorderThenFill(plane))
        self.play(Write(circ), run_time=0.5, rate_func=linear)
        self.wait()
        self.play(Create(VGroup(line1, mi), run_time=0.25, rate_func=linear))
        self.wait()
        self.play(ReplacementTransform(line1, radius), ReplacementTransform(mi, mi_move))
        self.wait()
        self.play(Create(VGroup(theta_label, theta_value)))
        self.wait()
        self.play(Create(VGroup(line2, de), run_time=0.25, rate_func=linear))
        self.wait()
        self.play(ReplacementTransform(line2, line_de), ReplacementTransform(de, de_move))
        self.play(Write(divide1, run_time=0.25, rate_func=linear))
        self.play(Create(VGroup(equal1, sin_value)), run_time=0.25, rate_func=linear)
        self.wait()
        self.play(theta.animate.increment_value(TAU), rate_func=smooth, run_time=3)
        self.wait()
        self.play(Create(VGroup(line3, sa), run_time=0.25, rate_func=linear))
        self.wait()
        self.play(ReplacementTransform(line3, line_sa), ReplacementTransform(sa, sa_move), Write(mi_move2))
        self.play(Write(divide2, run_time=0.25, rate_func=linear))
        self.play(Create(VGroup(equal2, cos_value)), run_time=0.25, rate_func=linear)
        self.wait()
        self.play(theta.animate.increment_value(TAU), rate_func=smooth, run_time=3)
        self.wait()
        self.play(Create(VGroup(de_move2, sa_move2), run_time=0.25, rate_func=linear))
        self.play(Write(divide3, run_time=0.25, rate_func=linear))
        self.play(Create(VGroup(equal3, tan_value)), run_time=0.25, rate_func=linear)
        self.wait()
        self.play(theta.animate.increment_value(TAU), rate_func=smooth, run_time=3)
        self.wait()
        self.play(ReplacementTransform(Group(de_move, mi_move, divide1), sin_label), ReplacementTransform(Group(sa_move, mi_move2, divide2), cos_label), ReplacementTransform(Group(de_move2, sa_move2, divide3), tan_label))
        self.wait()
        self.play(theta.animate.increment_value(TAU), rate_func=smooth, run_time=3)
        self.wait()
