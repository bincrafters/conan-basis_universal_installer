from conans import ConanFile, tools
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch"

    def test(self):
        if not tools.cross_building(self.settings):
            file_path = os.path.join(self.source_folder, "conan_small.png")
            self.run("basisu {}".format(file_path), run_environment=True)
