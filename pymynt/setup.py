from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy
import subprocess

proc_libs = subprocess.check_output("pkg-config --libs opencv".split())
proc_incs = subprocess.check_output("pkg-config --cflags opencv".split())
# libs = [lib for lib in str(proc_libs, "utf-8").split()]
libs = [lib for lib in str(proc_libs).split()]
print("OPENCV LIBS=", libs)

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = cythonize(Extension("pymynt",
                                      sources = ["pymynt.pyx"],
                                      language = "c++",
                                      libraries=["mynteye_depth"],
                                      include_dirs=[numpy.get_include(), "/usr/include/"],
                                      extra_link_args=['-lopencv_shape', '-lopencv_stitching', '-lopencv_superres', '-lopencv_videostab', '-lopencv_aruco', '-lopencv_bgsegm', '-lopencv_bioinspired', '-lopencv_ccalib', '-lopencv_datasets', '-lopencv_dpm', '-lopencv_face', '-lopencv_freetype', '-lopencv_fuzzy', '-lopencv_hdf', '-lopencv_line_descriptor', '-lopencv_optflow', '-lopencv_video', '-lopencv_plot', '-lopencv_reg', '-lopencv_saliency', '-lopencv_stereo', '-lopencv_structured_light', '-lopencv_phase_unwrapping', '-lopencv_rgbd', '-lopencv_viz', '-lopencv_surface_matching', '-lopencv_text', '-lopencv_ximgproc', '-lopencv_calib3d', '-lopencv_features2d', '-lopencv_flann', '-lopencv_xobjdetect', '-lopencv_objdetect', '-lopencv_ml', '-lopencv_xphoto', '-lopencv_highgui', '-lopencv_videoio', '-lopencv_imgcodecs', '-lopencv_photo', '-lopencv_imgproc', '-lopencv_core']
                                      )
                            )
)