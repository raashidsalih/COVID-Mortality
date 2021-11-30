#!/usr/bin/env python
# coding: utf-8

from fastai.vision.all import load_learner, PILImage

def get_x(x):
  return imgpath + f"{x[0]}"

def get_y(y):
  return y[1]

learn_inf = load_learner('res18-orig-cw.pth')

import gradio as gr
labels = ['Low Risk', 'High Risk']
def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn_inf.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}
title="AI Based COVID-19 Mortality Risk Assessment"
description="""This app allows you to find the mortality risk of a COVID-19 patient by just using a chest X-Ray. Just drop your image below and click "Submit"."""
gr_interface = gr.Interface(fn=predict, inputs=gr.inputs.Image(shape=(224, 224)),outputs=gr.outputs.Label(num_top_classes=len(labels)), interpretation="default",
                            title=title, description=description)
gr_interface.launch(share=True)
gr_interface.launch()




