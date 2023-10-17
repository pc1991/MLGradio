#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 19:57:01 2023

@author: christian
"""

import gradio as gr
import numpy as np

def dough(input_img):
    dough_filter = np.array([[.4, .8, .2],
                             [.3, .7, .2],
                             [.3, .5, .1]])
    dough_img = input_img.dot(dough_filter.T)
    dough_img /= dough_img.max()
    return dough_img

imask = gr.Interface(dough, gr.inputs.Image(shape=(200, 200)), "image")

imask.launch()