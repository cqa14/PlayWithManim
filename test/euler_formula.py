from manimlib import *
import numpy as np

class DemonstrationEulerIdentity(Scene):
    def construct(self):
        title = Text("Euler's Identity", font_size=90)
        identity = Tex("e^{i\pi}", "+", "1", "=", "0")
        VGroup(title, identity).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(FadeIn(identity, UP))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(identity, shift=DOWN))

        formula_pres_1 = Text('This identity is a particular case of the "Euler´s formula"')
        formula = Tex("e^{i\\theta}", "=", "cos\\theta", "+", "i","sin\\theta")
        formula_pres_2 = Text("But where those that come from ?")
        VGroup(formula_pres_1, formula, formula_pres_2).arrange(DOWN, buff=1)
        self.play(FadeIn(formula_pres_1, UP), FadeIn(formula, RIGHT), FadeIn(formula_pres_2, DOWN))
        self.wait()
        self.play(FadeOut(formula_pres_1, UP), FadeOut(formula, RIGHT), FadeOut(formula_pres_2, DOWN))

        taylor_pres_1 = VGroup(Text('The "Taylor´s series" for'), Tex('e^x'), Text('and the sin and cos of x')).arrange(RIGHT)
        taylor_e = Tex("e^x", "=", "1", "+","x", "+", "\\frac{x^2}{2!}", "+", "\\frac{x^3}{3!}", "+", "\\frac{x^4}{4!}", "+", "...")
        taylor_sin = Tex("sinx", "=", "x", "-", "\\frac{x^3}{3!}", "+", "\\frac{x^5}{5!}", "-", "\\frac{x^7}{7!}", "+", "...")
        taylor_cos = Tex("cosx", "=", "1", "-", "\\frac{x^2}{2!}", "+", "\\frac{x^4}{4!}", "-", "\\frac{x^6}{6!}", "+", "...")
        VGroup(taylor_pres_1, taylor_e, taylor_sin, taylor_cos).arrange(DOWN, buff=1)
        self.play(Write(taylor_pres_1), FadeIn(taylor_e, UP))
        self.wait()        
        self.play(FadeIn(taylor_sin, UP))
        self.wait()        
        self.play(FadeIn(taylor_cos, UP))
        self.wait(5)
        self.play(FadeOut(taylor_pres_1, DOWN), FadeOut(taylor_e, DOWN), FadeOut(taylor_sin, DOWN), FadeOut(taylor_cos, DOWN))

        imag_title = Text("What happens if we use an imaginary number as exponent ?")
        imag_num = VGroup(Text('Imaginary number : '), Tex('ix')).arrange(RIGHT)
        imag_i = VGroup(VGroup(Tex('i^2 = -1'), Tex('i^3 = -i')).arrange(RIGHT, buff=1), VGroup(Tex('i^4 = 1'), Tex('i^5 = i')).arrange(RIGHT, buff=1), Tex('...')).arrange(DOWN, buff=1)
        VGroup(imag_title, imag_num, imag_i).arrange(DOWN, buff=1)
        self.play(Write(imag_title), Write(imag_num))
        self.wait()
        self.play(FadeIn(imag_i, LEFT))
        self.wait(5)
        self.play(FadeOut(imag_i), FadeOut(imag_num), FadeOut(imag_title))

        imag_exp = VGroup(
            Tex("e^{ix} = 1 + ix + \\frac{(ix)^2}{2!} + \\frac{(ix)^3}{3!} + \\frac{(ix)^4}{4!} + \\frac{(ix)^5}{5!} + ...",
                isolate=["e^{ix}", "1", "\\frac{(ix)^2}{2!}", "\\frac{(ix)^3}{3!}","\\frac{(ix)^4}{4!}","\\frac{(ix)^5}{5!}", "..."]),

            Tex("e^{ix} = 1 + ix - \\frac{x^2}{2!} - \\frac{ix^3}{3!} + \\frac{x^4}{4!} + \\frac{ix^5}{5!} + ...",
                isolate=["e^{ix}", "1", "\\frac{x^2}{2!}", "\\frac{ix^3}{3!}","\\frac{x^4}{4!}","\\frac{ix^5}{5!}", "..."]),

            Tex("e^{ix} = (1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...) + i(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)",
                isolate=["e^{ix}", "1", "i", "\\frac{x^2}{2!}", "\\frac{x^3}{3!}","\\frac{x^4}{4!}","\\frac{x^5}{5!}", "..."])
        ).arrange(DOWN, buff=1)
        imag_exp_supp = Tex("e^{ix} = 1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ix - \\frac{ix^3}{3!} + \\frac{ix^5}{5!} + ...",
                            isolate=["e^{ix}", "1", "\\frac{x^2}{2!}", "\\frac{ix^3}{3!}","\\frac{x^4}{4!}","\\frac{ix^5}{5!}", "..."])
        formula_imag = Tex("e^{ix} = cosx + isinx", isolate=["e^{ix}", "cosx", "sinx"])
        play_kw = {"run_time": 2}
        self.add(imag_exp[0])
        self.play(
            TransformMatchingTex(
                imag_exp[0].copy(), imag_exp[1],
                transform_mismatches=True,
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                imag_exp[1], imag_exp_supp,
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                imag_exp_supp.copy(), imag_exp[2],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(3)
        self.play(FadeOut(imag_exp[0]), FadeOut(imag_exp_supp), FadeOut(imag_exp[2]))
        self.play(Write(formula_imag))
        self.wait(5)
        self.play(FadeOut(formula_imag))

        final_text = Text("So, the identity :")
        identity_calc = VGroup(
            Tex("e^{i\\theta} = cos\\theta + i sin\\theta"),
            Tex("e^{i\pi} = cos\pi + i sin\pi"),
            Tex("e^{i\pi} = -1"),
            Tex("e^{i\pi} + 1 = 0")
        ).arrange(DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(1)
        self.play(FadeOut(final_text, RIGHT))
        self.add(identity_calc[0])
        self.play(
            TransformMatchingTex(
                identity_calc[0].copy(), identity_calc[1],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.play(
            TransformMatchingTex(
                identity_calc[1].copy(), identity_calc[2],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.play(
            TransformMatchingTex(
                identity_calc[2].copy(), identity_calc[3],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(5)
        self.play(FadeOut(identity_calc, UP))

        self.play(Write(Text(
            """
            Romain Blondel
            December 2021
            """)))
        self.wait(2)


class DemonstrationEulerIdentityFrench(Scene):
    def construct(self):
        to_isolate = ["e", "1 + x + \\frac{x^2}{2!} + \\frac{x^3}{3!} + \\frac{x^4}{4!} + ...",
                      "1 + ix + \\frac{(ix)^2}{2!} + \\frac{(ix)^3}{3!} + \\frac{(ix)^4}{4!} + \\frac{(ix)^5}{5!} + ...",
                      "\pi", "i", "\\theta", "cos", "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...",
                      "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)", "sin", "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...",
                      "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)"]
        title = Text("L´identité d´Euler", font_size=90)
        identity = Tex("e^{i\pi} + 1 = 0", isolate=[*to_isolate]).set_color_by_tex_to_color_map({
            "e": GREEN,
            "i": YELLOW,
            "\pi": BLUE,
            "\\theta": BLUE,
            "cos": ORANGE,
            "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
            "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
            "sin": RED,
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
            "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
        })
        VGroup(title, identity).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(FadeIn(identity, UP))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(identity, shift=DOWN))

        formula_pres_1 = Text('C´est est un cas particulier de la "formule d´Euler"')
        formula = Tex("e^{i\\theta} = cos\\theta + i sin\\theta", isolate=[*to_isolate]).set_color_by_tex_to_color_map({
            "e": GREEN,
            "i": YELLOW,
            "\pi": BLUE,
            "\\theta": BLUE,
            "cos": ORANGE,
            "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
            "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
            "sin": RED,
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
            "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
        })
        formula_pres_2 = Text("Mais d´où cela vient-il ?")
        VGroup(formula_pres_1, formula, formula_pres_2).arrange(DOWN, buff=1)
        self.play(FadeIn(formula_pres_1, UP), FadeIn(formula, RIGHT), FadeIn(formula_pres_2, DOWN))
        self.wait(3)
        self.play(FadeOut(formula_pres_1, UP), FadeOut(formula, RIGHT), FadeOut(formula_pres_2, DOWN))

        taylor_pres_1 = VGroup(Text('"Séries de Taylor" de'), Tex('e^x'), Text('et de sin et cos de x')).arrange(RIGHT)
        taylor_e = Tex("e^x = 1 + x + \\frac{x^2}{2!} + \\frac{x^3}{3!} + \\frac{x^4}{4!} + ...", isolate=[*to_isolate]).set_color_by_tex_to_color_map({
            "e": GREEN,
            "1 + x + \\frac{x^2}{2!} + \\frac{x^3}{3!} + \\frac{x^4}{4!} + ...": GREEN,
            "i": YELLOW,
            "\pi": BLUE,
            "\\theta": BLUE,
            "cos": ORANGE,
            "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
            "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
            "sin": RED,
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
            "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
        })
        taylor_sin = Tex("sinx = x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...", isolate=[*to_isolate]).set_color_by_tex_to_color_map({
            "e": GREEN,
            "i": YELLOW,
            "\pi": BLUE,
            "\\theta": BLUE,
            "cos": ORANGE,
            "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
            "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
            "sin": RED,
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
            "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
        })
        taylor_cos = Tex("cosx = 1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...", isolate=[*to_isolate]).set_color_by_tex_to_color_map({
            "e": GREEN,
            "i": YELLOW,
            "\pi": BLUE,
            "\\theta": BLUE,
            "cos": ORANGE,
            "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
            "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
            "sin": RED,
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
            "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
        })
        VGroup(taylor_pres_1, taylor_e, taylor_sin, taylor_cos).arrange(DOWN, buff=1)
        self.play(Write(taylor_pres_1), FadeIn(taylor_e, UP))
        self.wait()
        self.play(FadeIn(taylor_sin, UP))
        self.wait()
        self.play(FadeIn(taylor_cos, UP))
        self.wait(5)
        self.play(FadeOut(taylor_pres_1, DOWN), FadeOut(taylor_e, DOWN), FadeOut(taylor_sin, DOWN), FadeOut(taylor_cos, DOWN))

        imag_title = Text("Que ce passe-t-il si l'on prend un exposant imaginaire ?")
        imag_num = VGroup(Text('Nombre imaginaire : '), Tex('ix', isolate=[*to_isolate]).set_color_by_tex_to_color_map({
            "e": GREEN,
            "i": YELLOW,
            "\pi": BLUE,
            "\\theta": BLUE,
            "cos": ORANGE,
            "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
            "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
            "sin": RED,
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
            "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
        })).arrange(RIGHT)
        imag_i = VGroup(VGroup(Tex('i^2 = -1', isolate=[*to_isolate]).set_color_by_tex_to_color_map({
            "e": GREEN,
            "i": YELLOW,
            "\pi": BLUE,
            "\\theta": BLUE,
            "cos": ORANGE,
            "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
            "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
            "sin": RED,
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
            "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
        }),
        Tex('i^3 = -i', isolate=[*to_isolate]).set_color_by_tex_to_color_map({
            "e": GREEN,
            "i": YELLOW,
            "\pi": BLUE,
            "\\theta": BLUE,
            "cos": ORANGE,
            "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
            "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
            "sin": RED,
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
            "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
        })).arrange(RIGHT, buff=1),
        VGroup(
            Tex('i^4 = 1', isolate=[*to_isolate]).set_color_by_tex_to_color_map({
                "e": GREEN,
                "i": YELLOW,
                "\pi": BLUE,
                "\\theta": BLUE,
                "cos": ORANGE,
                "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
                "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
                "sin": RED,
                "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
                "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
            }),
            Tex('i^5 = i', isolate=[*to_isolate]).set_color_by_tex_to_color_map({
                "e": GREEN,
                "i": YELLOW,
                "\pi": BLUE,
                "\\theta": BLUE,
                "cos": ORANGE,
                "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
                "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
                "sin": RED,
                "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
                "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
            })).arrange(RIGHT, buff=1),
            Tex('...')).arrange(DOWN, buff=1)
        VGroup(imag_title, imag_num, imag_i).arrange(DOWN, buff=1)
        self.play(Write(imag_title), Write(imag_num))
        self.wait()
        self.play(FadeIn(imag_i, LEFT))
        self.wait(5)
        self.play(FadeOut(imag_i), FadeOut(imag_num), FadeOut(imag_title))

        imag_exp = VGroup(
            Tex("e^{ix} = 1 + ix + \\frac{(ix)^2}{2!} + \\frac{(ix)^3}{3!} + \\frac{(ix)^4}{4!} + \\frac{(ix)^5}{5!} + ...",
                isolate=[*to_isolate]).set_color_by_tex_to_color_map({
                    "e": GREEN,
                    "i": YELLOW,
                    "1 + ix + \\frac{(ix)^2}{2!} + \\frac{(ix)^3}{3!} + \\frac{(ix)^4}{4!} + \\frac{(ix)^5}{5!} + ...": GREEN,
                    "\pi": BLUE,
                    "\\theta": BLUE,
                    "cos": ORANGE,
                    "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
                    "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
                    "sin": RED,
                    "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
                    "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
            }),

            Tex("e^{ix} = 1 + ix - \\frac{x^2}{2!} - \\frac{ix^3}{3!} + \\frac{x^4}{4!} + \\frac{ix^5}{5!} + ...",
                isolate=["1", "+ ix", "- \\frac{x^2}{2!}", "- \\frac{ix^3}{3!}", "+ \\frac{x^4}{4!}",
                         "+ \\frac{ix^5}{5!}", "+ ...", *to_isolate]).set_color_by_tex_to_color_map({
                    "e": GREEN,
                    "i": WHITE,
                    "\pi": BLUE,
                    "\\theta": BLUE,
                    "cos": ORANGE,
                    "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
                    "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
                    "sin": RED,
                    "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
                    "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
                    "1": WHITE,
                    "+ ix": WHITE,
                    "- \\frac{x^2}{2!}": WHITE,
                    "- \\frac{ix^3}{3!}": WHITE,
                    "+ \\frac{x^4}{4!}": WHITE,
                    "+ \\frac{ix^5}{5!}": WHITE,
                    "+ ...": WHITE,
            }),

            Tex("e^{ix} = (1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...) + i(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)",
                isolate=["(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)", "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)",
                         *to_isolate, ]).set_color_by_tex_to_color_map({
                    "e": GREEN,
                    "i": YELLOW,
                    "\pi": BLUE,
                    "\\theta": BLUE,
                    "cos": ORANGE,
                    "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
                    "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
                    "sin": RED,
                    "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
                    "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
            })
        ).arrange(DOWN, buff=1)
        imag_exp_supp = Tex("e^{ix} = 1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ix - \\frac{ix^3}{3!} + \\frac{ix^5}{5!} + ...",
                            isolate=["1", "- \\frac{x^2}{2!}", "+ \\frac{x^4}{4!}" "+ ix", "- \\frac{ix^3}{3!}",
                                     "+ \\frac{ix^5}{5!}", "+ ...", *to_isolate]).set_color_by_tex_to_color_map({
                                "e": GREEN,
                                "i": WHITE,
                                "+ ix": WHITE,
                                "\pi": BLUE,
                                "\\theta": BLUE,
                                "cos": ORANGE,
                                "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
                                "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
                                "sin": RED,
                                "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
                                "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
                                "1": WHITE,
                                "- \\frac{x^2}{2!}": WHITE,
                                "- \\frac{ix^3}{3!}": WHITE,
                                "+ \\frac{x^4}{4!}": WHITE,
                                "+ \\frac{ix^5}{5!}": WHITE,
                                "+ ...": WHITE,
                            })
        formula_imag = Tex("e^{ix} = cosx + isinx", isolate=[*to_isolate]).set_color_by_tex_to_color_map({
            "e": GREEN,
            "i": YELLOW,
            "\pi": BLUE,
            "\\theta": BLUE,
            "cos": ORANGE,
            "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
            "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
            "sin": RED,
            "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
            "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
        })
        play_kw = {"run_time": 2}
        self.add(imag_exp[0])
        self.play(
            TransformMatchingTex(
                imag_exp[0].copy(), imag_exp[1],
                transform_mismatches=True,
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                imag_exp[1], imag_exp_supp,
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait()
        self.play(
            TransformMatchingTex(
                imag_exp_supp.copy(), imag_exp[2],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(4)
        self.play(FadeOut(imag_exp[0]), FadeOut(imag_exp_supp), FadeOut(imag_exp[2]))
        self.play(Write(formula_imag))
        self.wait(5)
        self.play(FadeOut(formula_imag))

        final_text = Text("Donc l'identité :")
        identity_calc = VGroup(
            Tex("e^{i\\theta} = cos\\theta + i sin\\theta", isolate=[*to_isolate]).set_color_by_tex_to_color_map({
                "e": GREEN,
                "i": YELLOW,
                "\pi": BLUE,
                "\\theta": BLUE,
                "cos": ORANGE,
                "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
                "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
                "sin": RED,
                "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
                "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
            }),
            Tex("e^{i\pi} = cos\pi + i sin\pi", isolate=[*to_isolate]).set_color_by_tex_to_color_map({
                "e": GREEN,
                "i": YELLOW,
                "\pi": BLUE,
                "\\theta": BLUE,
                "cos": ORANGE,
                "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
                "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
                "sin": RED,
                "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
                "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
            }),
            Tex("e^{i\pi} = -1", isolate=[*to_isolate]).set_color_by_tex_to_color_map({
                "e": GREEN,
                "i": YELLOW,
                "\pi": BLUE,
                "\\theta": BLUE,
                "cos": ORANGE,
                "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
                "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
                "sin": RED,
                "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
                "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
            }),
            Tex("e^{i\pi} + 1 = 0", isolate=[*to_isolate]).set_color_by_tex_to_color_map({
                "e": GREEN,
                "i": YELLOW,
                "\pi": BLUE,
                "\\theta": BLUE,
                "cos": ORANGE,
                "1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + ...": ORANGE,
                "(1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} + ...)": ORANGE,
                "sin": RED,
                "x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...": RED,
                "(x - \\frac{x^3}{3!} + \\frac{x^5}{5!} + ...)": RED,
            })).arrange(DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(1)
        self.play(FadeOut(final_text, RIGHT))
        self.add(identity_calc[0])
        self.play(
            TransformMatchingTex(
                identity_calc[0].copy(), identity_calc[1],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.play(
            TransformMatchingTex(
                identity_calc[1].copy(), identity_calc[2],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.play(
            TransformMatchingTex(
                identity_calc[2].copy(), identity_calc[3],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(5)
        self.play(FadeOut(identity_calc, UP))

        self.play(Write(Text(
            """
            Romain Blondel
            Décembre 2021
            """)))
        self.wait(2)