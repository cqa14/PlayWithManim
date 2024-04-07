from manim import *


class PresAffine(Scene):
    def construct(self):
        axes = Axes((-10, 10), (-5, 5))
        axes.get_axis_labels(x_label="x", y_label="y")
        ex_graph = axes.plot(lambda x: 1/2*x-2, color=BLUE)
        ex_graph_lab = axes.get_graph_label(ex_graph, "f(x)=mx+h", direction=UP/2)

        self.play(Write(axes))
        self.play(Create(ex_graph), FadeIn(ex_graph_lab))
        self.wait()

        ex_h = axes.get_vertical_line(axes.i2gp(0, ex_graph), color=RED, line_func=Line)
        ex_h_lab = axes.get_graph_label(ex_graph, "h", 0, direction=LEFT+UP, color=RED)

        self.play(FadeIn(ex_h, ex_h_lab))

        ex_m_x = [3, 4, 4]
        ex_m_y = [-1/2, -1/2, 0]
        ex_m = axes.plot_line_graph(x_values=ex_m_x, y_values=ex_m_y)
        ex_m_1_lab = axes.get_graph_label(ex_graph, "1", 3, direction=RIGHT/2+DOWN/2, color=WHITE)
        ex_m_m_lab = axes.get_graph_label(ex_graph, "m", 4, direction=RIGHT/2+DOWN/2, color=YELLOW)

        self.play(FadeIn(ex_m, ex_m_1_lab, ex_m_m_lab))
        self.wait()

        lin = axes.plot(lambda x: 1/2 * x, color=GREEN)
        lin_lab = axes.get_graph_label(lin, "f(x)=mx", direction=UP/2, color=GREEN)
        lin_ti = Text("Si h=0")
        lin_ti.to_edge(LEFT+UP)

        self.play(
            FadeOut(ex_m, ex_m_1_lab, ex_m_m_lab, ex_h, ex_h_lab),
            FadeIn(lin_ti),
            FadeTransform(ex_graph, lin),
            FadeTransform(ex_graph_lab, lin_lab)
        )
        self.wait()

        upw = axes.plot(lambda x: 1/2*x-2, color=GREEN)
        upw_lab = axes.get_graph_label(upw, "f(x)=mx+h", direction=UP/2, color=GREEN)
        upw_ti = Text("Si m>0")
        upw_ti.to_edge(LEFT+UP)
        self.play(
            FadeTransform(lin, upw),
            FadeTransform(lin_lab, upw_lab),
            FadeTransform(lin_ti, upw_ti)
        )
        self.wait()

        dow = axes.plot(lambda x: -1/2*x+1, color=GREEN)
        dow_lab = axes.get_graph_label(dow, "f(x)=mx+h", direction=DOWN/2, color=GREEN)
        dow_ti = Text("Si m<0")
        dow_ti.to_edge(LEFT+UP)
        self.play(
            FadeTransform(upw, dow),
            FadeTransform(upw_lab, dow_lab),
            FadeTransform(upw_ti, dow_ti)
        )
        self.wait()

        const = axes.plot(lambda x: 3, color=GREEN)
        const_lab = axes.get_graph_label(const, "f(x)=h", direction=UP/2, color=GREEN)
        const_ti = Text("Si m=0")
        const_ti.to_edge(LEFT+UP)
        self.play(
            FadeOut(dow, dow_ti, dow_lab),
            FadeIn(const, const_lab, const_ti)
        )
        self.wait()


class AllQuad(Scene):
    def construct(self):
        axes = Axes((-10, 10), (-5, 5))
        self.play(Write(axes))

        quadup = axes.plot(lambda x: 10 * (x ** 2), color=RED)
        midquadup = axes.plot(lambda x: 0.01 * (x ** 2), color=YELLOW)
        midquadown = axes.plot(lambda x: -0.01 * (x ** 2), color=YELLOW)
        quadown = axes.plot(lambda x: -10 * (x ** 2), color=GREEN)

        text = VGroup(Tex("a<0"), Tex("a>0"))
        text.to_edge(UP+LEFT)

        self.play(FadeIn(quadown, text[0]))
        self.wait(0.5)
        self.play(FadeTransform(quadown, midquadown), run_time=2.5)
        self.remove(midquadown, text[0])
        self.add(midquadup, text[1])
        self.play(FadeTransform(midquadup, quadup), run_time=2.5)
        self.wait()
