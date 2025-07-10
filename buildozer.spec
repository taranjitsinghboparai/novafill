##############################################################################
# NovaFill – Buildozer Specification
#
#   • Kivy + Pillow + PyTesseract + ReportLab
#   • Python-for-Android “develop” branch
#   • Python 3.10 recipe (stable with NDK r25b)
#   • ReportLab pure-Python (no native _rl_accel)
##############################################################################

[app]

# ---------------------------------------------------------------------------
# Basic metadata
# ---------------------------------------------------------------------------
title             = NovaFill
package.name      = novafill
package.domain    = org.novafill.app
version           = 1.1

# ---------------------------------------------------------------------------
# Source
# ---------------------------------------------------------------------------
source.dir        = .
source.include_exts = py,png,jpg,ttf,otf,pdf

# ---------------------------------------------------------------------------
# Runtime requirements (comma-separated, no spaces)
# ---------------------------------------------------------------------------
requirements      = python3,kivy,pillow,pytesseract,reportlab

# ---------------------------------------------------------------------------
# Orientation / Window
# ---------------------------------------------------------------------------
orientation       = portrait
fullscreen        = 1

# ---------------------------------------------------------------------------
# Python-for-Android tweaks
# ---------------------------------------------------------------------------
p4a.branch        = develop       # use latest recipes (fixes FreeType URL)
python_version    = 3.10          # avoids clang errors with 3.12
env.RL_NO_ACCEL   = 1             # disable ReportLab C speedups

# ---------------------------------------------------------------------------
# (Optional) include your custom fonts at runtime
# ---------------------------------------------------------------------------
# android.presplash_icon  = %(source.dir)s/assets/icons/presplash.png
# android.icon            = %(source.dir)s/assets/icons/icon.png


##############################################################################
# Buildozer global settings
##############################################################################
[buildozer]
log_level   = 2
warn_on_root = 1


##############################################################################
# Android-specific settings
##############################################################################
[android]

# APIs
android.api          = 33      # target
android.minapi       = 21      # min supported

# Architectures (arm64-v8a is standard; add armeabi-v7a if you need 32-bit)
android.arch         = arm64-v8a

# Permissions
android.permissions  = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# If you ever need to bundle the Tesseract traineddata files, uncomment ↓
# android.add_src    = assets/tessdata

##############################################################################
# End of file
##############################################################################
