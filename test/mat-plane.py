from manim import *


class SimpleTransform(Scene):
    def construct(self):
        grid = NumberPlane((-10, 10), (-5, 5))
        matrix = [[1, 1], [0, 1]]

        v_e1 = Vector([1, 0], color=BLUE)
        v_e2 = Vector([0, 1], color=BLUE)
        dot1 = Dot([1, 1, 0], color=BLUE)
        dot1_lab = Text('(1, 1)').next_to(dot1, UP)

        v_e1p = Vector([1, 0], color=RED)
        v_e2p = Vector([1, 1], color=RED)
        dot2 = Dot([2, 1, 0], color=RED)
        dot2_lab = Text('(2, 1)').next_to(dot2, UP)

        intro_word = VGroup(Text("Voici un plan avec un point"))
        intro_word.arrange(RIGHT)
        intro_word.to_edge(UP)

        self.add(grid)
        self.play(
            Write(intro_word),
            FadeIn(v_e1, v_e2),
            FadeIn(dot1, dot1_lab)
        )
        self.wait()

        epl_trans = VGroup(Text("Et en y applicant la matrix"),
                           Tex("$\\begin{pmatrix} 1 & 1 \\\\ 0 & 1 \end{pmatrix}$"))
        epl_trans.arrange(RIGHT)
        epl_trans.to_edge(UP)
        back_grid = NumberPlane((-10, 10), (-5, 5)).set_opacity(0.3)

        self.play(FadeTransform(intro_word, epl_trans))
        self.add(back_grid)
        self.play(
            FadeOut(v_e1, v_e2, dot1, dot1_lab),
            grid.animate.apply_matrix(matrix),
            FadeIn(v_e1p, v_e2p),
            FadeIn(dot2, dot2_lab)
        )
        self.wait()
