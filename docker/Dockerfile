FROM nvidia/cuda:11.8.0-base-ubuntu22.04

RUN apt-get update \
    && apt-get --assume-yes upgrade \
    && apt-get clean

RUN apt-get install -y git wget ffmpeg vim make

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-py38_23.11.0-2-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-py38_23.11.0-2-Linux-x86_64.sh -b \
    && rm -f Miniconda3-py38_23.11.0-2-Linux-x86_64.sh 

RUN conda --version
RUN conda init
RUN conda create -yn "waymo-motion-prediction" python=3.8