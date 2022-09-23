import vsketch


class {{cookiecutter.class_name}}(vsketch.SketchClass):
    # Sketch parameters:
    # radius = vsketch.Param(2.0)

    def draw(self, v: vsketch.Vsketch) -> None:
        v.size("{{cookiecutter.page_size}}", landscape={{cookiecutter.landscape}})
        v.scale("{{cookiecutter.preferred_unit}}")

        self.process(v)

    def process(self, v: vsketch.Vsketch):
        pass

    def finalize(self, v: vsketch.Vsketch) -> None:
        v.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    {{cookiecutter.class_name}}.display()
