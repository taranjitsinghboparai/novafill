##############################################################################
# NovaFill – Buildozer Specification
##############################################################################

[app]
# ── Metadata ────────────────────────────────────────────────────────────────
title            = NovaFill
package.name     = novafill
package.domain   = org.novafill.app
version          = 1.1

# ── Source ──────────────────────────────────────────────────────────────────
source.dir       = .
source.include_exts = py,png,jpg,ttf,otf,pdf

# ── Runtime requirements ────────────────────────────────────────────────────
# Pin Python 3.10.8 so p4a uses that recipe, avoiding the struct _frame error
requirements     = \
    python3==3.10.8,\
    kivy,\
    pillow,\
    pytesseract,\
    reportlab

# ── Window / Orientation ───────────────────────────────────────────────────
orientation      = portrait
fullscreen       = 1

# ── python-for-android tweaks ───────────────────────────────────────────────
p4a.branch       = develop        # latest recipes
env.RL_NO_ACCEL  = 1              # build ReportLab pure-Python

[buildozer]
log_level        = 2
warn_on_root     = 1

[android]
android.api      = 33
android.minapi   = 21
android.arch     = arm64-v8a
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
# android.add_src = assets/tessdata   # ← if you bundle traineddata files

##############################################################################
# End of file
##############################################################################
