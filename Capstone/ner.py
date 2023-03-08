#!/usr/bin/env python
# coding: utf-8

import spacy
import pandas as pd

nlp_q = spacy.load(r"C:\Users\Admin\capstone\14-10-2022\quant_output/model-best")
nlp_i = spacy.load(r"C:\Users\Admin\capstone\14-10-2022\output/model-best")


def ner_model():
    
    output = pd.read_csv(r'label.csv')
    docs = output.loc[output['label']==1]
    
    docs = list(docs['Sentence'])
    result = []
    res = {}
    for i in range(0,len(docs)):
        s= docs[i]
        doc_q= nlp_q(docs[i])
        doc_i= nlp_i(docs[i])
        q_i=[]
        q = ""
        for ent in doc_q.ents:
            q = ent.text
            break
        ing = ""
        for ent_i in doc_i.ents:
            ing = ent_i.text
            break
        if ing:
            res[ing] = q
    #print(res)
    return res
