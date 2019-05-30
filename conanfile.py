# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class BasisUnivesalConan(ConanFile):
    name = "basis_universal_installer"
    version = "1.00"
    description = "Basis Universal GPU Texture Codec "
    topics = ("conan", "basis_universal", "installer", "binomialllc", "gpu", "texture-codec")
    url = "https://github.com/bincrafters/conan-basis_universal"
    homepage = "https://github.com/BinomialLLC/basis_universal"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "Apache-2.0"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt", "0001-build.patch"]
    generators = "cmake"
    settings = "os_build", "arch_build", "compiler"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        sha256 = "1f56512265bd45f5fe40707e68a344537dfc5938890df564adb3e7aad5072bba"
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        extracted_dir = "basis_universal-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_X64"] = self.settings.arch_build == "x86_64"
        cmake.configure()
        return cmake

    def build(self):
        tools.patch(base_path=self._source_subfolder, patch_file="0001-build.patch")
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_id(self):
        del self.info.settings.compiler

    def package_info(self):
        bin_path = os.path.join(self.package_folder, "bin")
        self.output.info('Appending PATH environment variable: %s' % bin_path)
        self.env_info.PATH.append(bin_path)