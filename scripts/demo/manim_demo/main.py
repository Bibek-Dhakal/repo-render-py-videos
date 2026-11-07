from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.22
config.frame_width = 8.0

class scene_1(Scene):
    def construct(self):
        title = Text("Repo Render Py", font_size=72, weight=BOLD).set_color(BLUE)
        subtitle = Text("Automated Python Pipeline", font_size=36, color=GRAY)
        group = VGroup(title, subtitle).arrange(DOWN, buff=0.5).scale_to_fit_width(7.0)

        self.play(FadeIn(group, shift=UP), run_time=1.5)
        self.wait(1.0)

class scene_2(Scene):
    def construct(self):
        features = VGroup(
            Text("✅ Zero-DB Filesystem", font_size=48),
            Text("✅ Auto Audio Muxing", font_size=48),
            Text("✅ AI Prompt Engine", font_size=48)
        ).arrange(DOWN, buff=0.5).set_color(WHITE).scale_to_fit_width(7.0)

        self.play(FadeIn(features, shift=UP), run_time=1.5)
        self.wait(1.0)
        self.play(features.animate.scale(1.1).set_color(YELLOW), run_time=1.0)
        
class thumbnail(Scene):
    def construct(self):
        title = Text("Repo Render Py", font_size=90, weight=BOLD).set_color(BLUE)
        badge = Text("AI Video", font_size=60).set_color(YELLOW).next_to(title, DOWN)
        group = VGroup(title, badge).scale_to_fit_width(7.0)
        self.add(group)
