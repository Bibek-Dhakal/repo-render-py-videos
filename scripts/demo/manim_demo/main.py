from manim import *

class MyScene(Scene):
    def construct(self):
        config.pixel_height = 1920
        config.pixel_width = 1080
        
        # Scene 1: Intro
        title = Text("Repo Render Py", font_size=72, weight=BOLD).set_color(BLUE)
        subtitle = Text("Automated Python Video Pipeline", font_size=36, color=GRAY)
        group = VGroup(title, subtitle).arrange(DOWN, buff=0.5)

        self.play(FadeIn(group, shift=UP))
        self.wait(1)

        # Scene 2: Features
        features = VGroup(
            Text("✅ Zero-DB Filesystem", font_size=48),
            Text("✅ Auto Audio Muxing", font_size=48),
            Text("✅ AI Prompt Engine", font_size=48)
        ).arrange(DOWN, buff=0.5).set_color(WHITE)

        self.play(ReplacementTransform(group, features))
        self.wait(1)
        
        # Outro
        self.play(features.animate.scale(1.2).set_color(YELLOW))
        self.wait(1)
        self.play(FadeOut(features, shift=DOWN))
        self.wait(0.5)
