#!/usr/bin/env python
# coding: utf-8

import gradio as gr
import glob
from fastai.vision.all import load_learner, PILImage


def get_x(x):
    return imgpath + f"{x[0]}"


def get_y(y):
    return y[1]


learn_inf = load_learner('models/res18-tcia.pth')

labels = ['Low Risk', 'High Risk']

sample_xrays = glob.glob("examples/*")


def predict(img):
    img = PILImage.create(img)
    pred, pred_idx, probs = learn_inf.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}


title = "AI Based COVID-19 Mortality Risk Assessment"
description = """This tool is designed to help assess the mortality risk
of a COVID-19 patient based on their chest X-ray. Mortality risk can be
defined as the likelihood of an individual dying. A ResNet-18 model was
trained and tested on datasets procured from Cohen et al. and Stony Brook
University. Just upload an image below and click "Submit" to obtain the
model's prediction."""
gr_interface = gr.Interface(fn=predict,
                            inputs=gr.inputs.Image(
                              shape=(224, 224)
                              ),
                            outputs=gr.outputs.Label(
                              num_top_classes=len(labels)
                            ),
                            interpretation="default",
                            title=title, description=description,
                            examples=sample_xrays)
gr_interface.launch(share=True)
gr_interface.launch()
