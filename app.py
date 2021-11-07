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

gr_interface = gr.Interface(fn=predict, inputs=gr.inputs.Image(shape=(512, 512)),outputs=gr.outputs.Label(num_top_classes=len(labels)), interpretation="default")
gr_interface.launch()




