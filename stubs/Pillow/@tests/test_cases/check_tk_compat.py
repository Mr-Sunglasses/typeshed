# Verify that ImageTK images are valid to pass to TK code.
from __future__ import annotations

# The following tests don't work on pyright at the moment, due to it getting
# confused by the existence of these stubs and annotations in the actual
# Pillow package.
# https://github.com/python/typeshed/issues/11688
# pyright: reportArgumentType=false
import tkinter

from PIL import ImageTk

photo = ImageTk.PhotoImage()
bitmap = ImageTk.BitmapImage()

tkinter.Label(image=photo)
tkinter.Label(image=bitmap)

tkinter.Label().configure(image=photo)
tkinter.Label().configure(image=bitmap)
